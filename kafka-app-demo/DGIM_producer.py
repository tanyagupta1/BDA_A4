from kafka import KafkaProducer
import json
import data_proc
import time
from data import get_registered_user
import numpy as np
import sys

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)

if __name__=="__main__":

    VEN = sys.argv[1]
    venues_authors, selected_venues = data_proc.return_input_data()
    print(len(selected_venues))
    c=0
    
    venue_stream={}
    venue_short=selected_venues
    for v in venue_short:
        venue_stream[v]=[]
    
    for paper in venues_authors:
        for venue in venue_short:
            if(venue==VEN):
                if( (venue in venues_authors[paper].keys())):
                    venue_stream[venue].append(1)
                    producer.send(venue,"1")
                else:
                    venue_stream[venue].append(0)
                    producer.send(venue,"0")
                print("sent: ", venue_stream[VEN][-1])
                producer.flush()
                time.sleep(0.01)
    
    # print(venue_stream['nature'])
    
    # n=600
    # S= np.random.randint(0,2,n)
    # i=0
    # while (i<n):
    #     producer.send("nature", str(S[i]))
    #     # time.sleep(1)
    #     i+=1
    # print(i)