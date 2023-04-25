from kafka import KafkaConsumer
import json

if __name__=="__main__":
    consumer = KafkaConsumer(
        "nature",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
        )
    print("starting the consumer")
    for msg in consumer:
        print("bit received ={}".format(json.loads(msg.value)))