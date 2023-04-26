from kafka import KafkaConsumer
import json

freq_map={}
def merge(l,size):
  n = len(l)
  i=n-1
  new_l=[]
  while(i>=0):
    if(l[i][2]==size):
      new_l.insert(0,l[i])
      new_l.insert(0,[l[i-2][0],l[i-1][1],2*size])
      freq_map[size]=1
      if((size*2) not in freq_map.keys()):
        freq_map[2*size]=0
      freq_map[2*size]+=1
      i-=3
    else:
      new_l.insert(0,l[i])
      i-=1
  # print("old: ",l, " new: ",new_l)
  return new_l

def handle_list(b):
  maxi  = b[0][2]
  i=1
  while(i<=maxi):
    # print(i,freq_map[i])
    # print(b)
    if(freq_map[i]>2):
      b = merge(b,i)
    i*=2
  return b

if __name__=="__main__":
    consumer = KafkaConsumer(
        "nature",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
        )
    print("starting the consumer")
    received_buffer=[]
    last_size=0
    buckets=[]
    first_one=True
    i=0
    for msg in consumer:
        bit = json.loads(msg.value)
        print("bit received ={}".format(bit))
        if(bit=='1'):
            if(first_one):
                freq_map[1]=1
                buckets.append([0,i,1])
                first_one=False
            else:
                buckets.append([i,i,1])
                freq_map[1]+=1
                buckets = handle_list(buckets)
        elif(not first_one):
            buckets[-1][1]+=1
        i+=1
        ones=0
        start_idx=i-500
        window=[]
        for b in buckets:
            if(b[0]<=start_idx):
                if(b[1]>=start_idx):
                    ones+=b[2]//2
                    window.append(b)
            else:
                ones+=b[2]
                window.append(b)
        print("window: ", window)
        print("ones: ", ones, " i: ",i)
            
