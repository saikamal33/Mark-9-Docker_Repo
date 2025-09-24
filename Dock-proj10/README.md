# A fully Dockerized log aggregation system:

we are building below in this project

- Multiple microservices logging to stdout
- Filebeat collecting logs from Docker containers
- logstash parsing and forwarding logs
- elasticsearch indexing logs
- kibana visualizing logs


## elasticsearch configuration in dockercompose

      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:7.17.0
        environment:
          - discovery.type=single-node
          - bootstrap.memory_lock=true
          - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
        ulimits:
          memlock:
            soft: -1
            hard: -1
        ports:
          - "9200:9200"

### environment:
This section set the env variables in the container

1.discovery.type=single-node   ---> This tells elastic search to run in single node mode and Prevents it from looking for other nodes to form a cluster.
2.bootstrap.memory_lock=true   --->Tells Elasticsearch to lock its memory in RAM. improves performance and stability. dependent on memlocks ulimit.
3."ES_JAVA_OPTS=-Xms512m -Xmx512m"  ---> This Sets JVM heap size to 512 MB. this ensures Elasticsearch doesn’t exceed allocated memory limits.

### ulimits:

ulimits is Linux resource limits applied to the container. and memlock controls how much memory a process can lock in RAM.

soft: -1 and hard: -1 = no memory lock limit.

This is required as the memory locking works when bootstrap.memory_lock=true

