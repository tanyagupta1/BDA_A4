from kafka import KafkaProducer
import json
import data_proc
import time


def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)

if __name__=="__main__":


    venues_authors, selected_venues = data_proc.return_input_data()
    print(len(selected_venues))
    c=0
    
    venue_stream={}
    venue_short=selected_venues
    for v in venue_short:
        venue_stream[v]=[]
    
    for paper in venues_authors:
        for venue in venue_short:
            if( (venue in venues_authors[paper].keys()) and(venue=="nature")):
                venue_stream[venue].append(1)
                producer.send(venue,1)
            else:
                venue_stream[venue].append(0)
                producer.send(venue,0)
    
    print(venue_stream['nature'])
