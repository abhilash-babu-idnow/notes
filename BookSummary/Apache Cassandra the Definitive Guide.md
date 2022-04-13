**Chapter 1 - Beyond relational databases**

> If I had asked people what they wanted, they would have said faster horses - Henry Ford

*A Relational Model of Data for Large Shared Data Banks* , by Dr. Edgar F. Codd paper on Relational database. 

Problems with relational databases. 

* Scalability problems.
* Joins can be slow
* Not suitable for high availability, particularly if the load is very high

@todo - read rest of the chapter which is mainly history of RDBMs and their disadvantages etc... 

**Chapter 2 - Introducing Cassandra** 

> Distributed
> - Capable of running on multiple machines 
> - You will need multiple machines to really realize any benefit from running Cassandra 
> - It is designed and optimized for running on multiple data center racks or even geographically dispersed data centers. 

> Decentralized
> - Every node is identical. There are no primary and secondary nodes. 
> - Peer to peer architecture with a gossip protocol to sync the nodes. 
> - So there is no single point failure, hence the high availability

> Elastic Scalability


> Row Oriented
> Partitioned Row Store
> Data in Cassandra is stored in sparse multidimensional hash tables. ie. for any given row there can be one or more columns, but each row doesn't need to have the same columns
> Though Cassandra started of as a schema less database, but since version 3, option to dynamically adding columns was deprecated. One can still add columns but as a new variable to collections like sets and lists in CQL. So the best way to describe would be that Cassandra supports "flexible schema"

> High Performance.