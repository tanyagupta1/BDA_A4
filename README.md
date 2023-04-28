# BDA_A4

## Instructions:

* make sure topic is fresh:
    * bin/kafka-topics.sh --delete --topic nature --bootstrap-server localhost:9092
    * bin/kafka-topics.sh --create --topic nature --bootstrap-server localhost:9092
    
* **DGIM**
    * producer : python3 DGIM_producer.py nature
    * consumer : python3 DGIM_consumer.py nature>consumer_output_DGIM.txt

* **FM** 
    * 