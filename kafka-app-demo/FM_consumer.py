from kafka import KafkaConsumer
import json
import hashlib
import sys

if __name__=="__main__":

    VEN = sys.argv[1]
    consumer = KafkaConsumer(
        VEN,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a",
        consumer_timeout_ms=5000
        )
    print("starting the consumer")
    authors=[]
    R=0
    i=0
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
        print("i:",i," No. of unique authors: ",(pow(2,R)))
        i+=1