# BDA_A4

## Instructions:

* make sure topic is fresh:
    * ```bin/kafka-topics.sh --delete --topic nature --bootstrap-server localhost:9092```
    * ``` bin/kafka-topics.sh --create --topic nature --bootstrap-server localhost:9092 ```
    
* **DGIM**
    * producer : ```python3 DGIM_producer.py <no of topics>``` 
    * consumer : ```python3 DGIM_consumer.py <topic name> > DGIM_<topic>.txt```
        * eg: ```python3 DGIM_consumer.py nature >DGIM_nature.txt```
        * run  ``` bash -x  ./consumer_script_DGIM.sh```


* **FM** 
    * producer : ```python3 FM_producer.py <no of topics>```
    * consumer : ```python3 FM_consumer.py <topic> > FM_<topic>.txt```
        * eg: ```python3 FM_consumer.py nature >FM_nature.txt```
        * run ``` bash -x  ./consumer_script_FM.sh ```

* Consumer script generator
    * ``` python3 consumer_script_generator.py <no of topics> ```
    