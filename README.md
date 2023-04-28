# BDA_A4

## Instructions:

* make sure topic is fresh:
    * bin/kafka-topics.sh --delete --topic nature --bootstrap-server localhost:9092
    * bin/kafka-topics.sh --create --topic nature --bootstrap-server localhost:9092
    
* **DGIM**
    * producer : python3 DGIM_producer.py <no of topics> (1-22151)
    * consumer : python3 DGIM_consumer.py <topic name> >consumer_output_DGIM_<topic>.txt
        * python3 DGIM_producer.py 2
        * python3 DGIM_consumer.py nature >nature_test
        * python3 DGIM_consumer.py journal_of_machine_learning_research >journal_of_machine_learning_research_test


* **FM** 
    * 