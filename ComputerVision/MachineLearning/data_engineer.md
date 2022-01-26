## What is Data Engineering?
engineering and operational tasks involved in providing data to the end user for analytics, modeling, app development etc.

Data science heirarchy of needs.

AI / Deep learning -> A/B Testing, experimentation, ML algos -> Analytics, metrics, data aggregation -> cleaning, prep -> etl -> instrumentation, external data etc.

Bottom layer (software dev)
4th and 5th layer from top -> data engineer
2nd and 3rd layer from top -> data analysts
Top most layer -> Research scientist


Software dev -> system architecture
Data eng -> store and process data
Data analyst -> reports and analytics
Data scientist -> modeling and ml and ai

Data Engineer <- Software Engineer + Data Scientist

## Activities of Data Engineer

* Ingest data from a data source
* Build and maintain a data warehouse
* Create a data pipeline
* Create an analytics table for a specific use case
* Migrate data to the cloud
* Schedule and automate pipelines.
* Backfill data
* Debug data quality issues
* Optimize queries
* Design a database

## Data Modeling

Objective -> strengths and weakness of different types of databases and modeling techniques.

> ".. an abstraction that orgainzes elements of data and how they are related...."

data modelling -> end state database modelling.

orgainize data -> database -> persisitence.

support business , support users.

gather requirements -> conceptual data modelling (mapping of the concepts of the data) -> logical data modeling (map concepts to tables etc) -> physical data modeling (data defenition language)



Why data modelling is important?

if data organization is not well thought out, it will lead to complicated queries. it is an iterative process. it should be done before developing the application.

Who does the data modelling?
everyone who is dealing with the data -> software eng, data eng, data analyst, data scietist

Relational Model

Orgainizes data into one more tables( relations ) of columns and rows with a unique key identifying each row.

Invented by Edga Codd. (1970)


## Advantages of using a relational database
* ease of use
* ability to do joins
* ability to do aggregations and analytics
* smaller data volumes
* easier to change business requirements.
* flexibility for queries
* modeling the data not modeling queries
* secondary indexes available.
* acid transactions -- data integrity

### ACID
Atomicity - The whole transaction is processed or nothing is processed
Consistency - Only transaction that abide by constraints and rules is written into the database otherwise database keeps the previous state
Isolation - Transactions are processed independently and securely order doesnt matter.
Durability - Completed transactions are saved to database even of cases of system failure.

## When not to use a relational database?
* have large amounts of data
* need to store different data type formats
* need high throughpouts
* need flexible schema
* need high availability
* need horizontal scalability.

## PostgreSQL

* Open source
* object relational database system
* syntax different from other sql

## Common types of nosql dbs
* apache cassandra (partition row store)
* Mongodb (document store)
* dynamodb (key value store)
* apache hbase (wide column store)
* neo4j (graph db)

## Basics of apache cassandra
Some of the terminology that is specific to Apache Cassandra

* Keyspace - Collection of tables
* Table - A group of partitions
* Rows - A single item
* Partition - Fundamental unit of access
    * Collection of rows
    * defines how the data is distributed.
* Primary key - a combination of partition key and clustering columns
* Columns - clustering columns and data columns


> It uses its own query language called CQL (Cassandra query language)

## When to use nosql db
* Large amounts of data
* Need horizontal scalability
* Need high throughput -- fast reads
* Need a flexible schema
* Need high availability
* Need to be able to store different data type
* Users are distributed (low latency)


> NoSQL databases and Relational databases do **not replace** each other for all tasks
> Both do different tasks extremely well and should be utilized for the use cases they fit best

# Lesson 2 - Relational Data Models

Database - A set of related data and the way it is orgainzed.

Database Management System - computer software that allows the users to interact with the database and provide access to the data.

12 rules that makes a database management system  a true relational system (From Edgar R. Codd)

* Rule 1 - Information rule - All information in a relational database is represented explicitly at the logical level and in exactly one way - by values in tables.

Other rules were not covered....


## OLAP vs OLTP
Online Analytical Processing OLAP - complex analytical and ad hoc queries - optimized for reads.
Online Transactioansl Processing OLTP - less complex queries in large volume - read, insert, update and delete

## Structuring your database

Normalization - reduce data redundancy and increase data integrity
Denormalization - must be done in read heavy workloads to increase performance.

> Normalization is the process of structuring a relational database in accordance with a series of normal forms in order to reduce data redundancy and increate data integrity.

## Objectives of Normal form.


# Lesson 4 - NoSQL Data models


When to use?
* Need high availability
* have large amounts of data
* linear scalability
* low latency
* fast reads and write


## Distributed databases design
In a distributed database in order to have high availability you will need copies of your data

### Eventual consistency

A consistency model used in distributed computing to achieve high availability that informally guarantees that, if no new updates are made to a given data item, eventually all access to that item return the last updated value.

### CAP Theorem

A theorem in computer science that states that it is impossible for a distributed data store to simultaneously provide more than two out of the following three guarantees of **consistency**, **availability**, **partition tolerance**.

#### Consistency
Every read from the database gets the latest and correct piece of data or an error

#### Availability
Every request is received and a response is given without a guarantee that the data is the latest update

#### Partition Tolerance
The system continues to work regardless of losing network connectivity between nodes.

Apache Cassandra is an AP database.

> Denormailization in Apache Cassandra
> The biggest take away when doing data modeling in Apache Cassandra is to think about your queries first. There are no JOINS in Apache cassandra
>

* Data modelling in Apache Cassandra
    ** Denormalization is not just okay --its a must
    ** Denormalization must be done for fast reads
    ** Apache Cassandra has been optimized for fast writes
    ** ALWAYS thinik Queries first
    ** One table per query is a great strategy
    ** Apache Cassandra does not allow for JOINs between tables.

### Cassandra Query Language (CQL)

```
import cassandra
from cassandra.cluster import Cluster

# Connect to the db
try:
cluster = Cluster(["127.0.0.1"])
session = cluster.connect()
except Exception as e:
print(e)

# Create a keyspace to work in
try:
session.execute("""
CREATE KEYSPACE IF NOT EXISTS udacity
WITH REPLICATION =
{
    'class' : 'SimpleStrategy', 'replication_factor' : 1
}
""")

query = """CREATE TABLE IF NOT EXISTS music_library
(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"""

try:
session.execute(query)
except Exception as e:
print(e)


```

### Primary key

* The primary key is how each row can be uniquely identified and how the data is distributed across the nodes or servers in our system
* The first element of the primary key is the **partition key** which will determine the distribution
* The primary key is made up of either just the partition key or with the addition of clustering columns.

#### Partition key
The patition keys row value will be hashed and stored on the node in the system that hold that range of values

> Primary key simple
>
> Primary key is same as the partition key.


> **Primary key must be unique**

#### Clustering Columns







# Data Warehouses

> A data warehouse is a copy of transaction data specifically structured for query and analysis
>
> A data warehouse is a subject oriented integrated non volatile and time variant collection of  data in support of management's decisions
>
> A data warehouse is a system that retrieves and consolidates data periodically from the source systems into a dimensional or normalized data store. It usually keeps years of history and is queried for business intelligence or other analytical activities. It is typically updated in batches not every time a transaction happens in the source system.
>

**DATA IN -> ETL -> DIMENSIONAL MODEL -> DATA OUT**

Goals of Data warehouse

* Simple to understand
* Performant
* Quality assured
* Handle new questions well
* Secure

Dimensional Modelling

Facts and Dimensions

> Fact tables - record business events, like an order, a phone call, a book review
> records events in a quantifiable metrics like quantity of an item, duration of a call a book ration
>
> Dimension tables - records the context of the business events. eg. who, what where and why
> Dimension tables columns contain attributes like the store at which an item is purchased or the customer who made the call etc.

Examples:

* Date and time are always a dimension
* Physical locaions and their attributes are good candidates dimensions
* Human roles like customers and staff always good candidates for dimensions.
* Goods sold always good candidates for dimensions
* Facts are usually numeric and additive
* Invoice number though numeric is not a good fact
* A comment on an article is not a good fact.




