What is Data Engineering?
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
