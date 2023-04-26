from kafka import KafkaConsumer
import json
import hashlib

if __name__=="__main__":
    consumer = KafkaConsumer(
        "nature",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
        )
    print("starting the consumer")
    authors=[]
    R=0
    for msg in consumer:
        auth = json.loads(msg.value)
        print("author received ={}".format(auth))
        authors.append(auth)       
        s = str(bin(int.from_bytes(hashlib.shake_128(auth.encode()).digest(4),'little')))
        # print(s)
        r=0
        n=len(s)
        while((r<n) and (s[n-1-r]=='0')):
            r+=1
        R=max(r,R)
        print("No. of unique authors: ",(pow(2,R)))