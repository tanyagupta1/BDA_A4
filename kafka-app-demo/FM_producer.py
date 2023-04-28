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

    
    venues_authors, selected_venues = data_proc.return_input_data()
    print(len(selected_venues))

    n = int(sys.argv[1])

    venue_stream={}
    venue_short=selected_venues[0:n]
    for v in venue_short:
        venue_stream[v]=[]
    print("Selected venues: ",venue_short)
    for paper in venues_authors:
        for venue in venue_short:
            if(venue in venue_short):
                if((venue in venues_authors[paper].keys())):
                    for auth in venues_authors[paper][venue]:
                        producer.send(venue,auth)
                        # print("sent: ", auth)
                producer.flush()
                time.sleep(0.0001)
    
    # print(venue_stream['nature'])
    
    # n=600
    # S= np.random.randint(0,2,n)
    # i=0
    # while (i<n):
    #     producer.send("nature", str(S[i]))
    #     # time.sleep(1)
    #     i+=1
    # print(i)