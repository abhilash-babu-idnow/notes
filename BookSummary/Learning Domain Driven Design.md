> Software Crisis
> Coined in 1968
> Refers to the fact that a vast majority of the software projects fail.

- Effective Communication is the central theme of the domain driven design.
- DDD divided into
	- Strategic
		- Analyze business domain and strategy.
		- Shared understanding of the business between stakeholders
		- What software are we building?
		- Why are we building it?
	- Tacticlal
		- Write code in a way that reflects the business needs and goals
		- Speaks the language of the Business.
		- How the software is being built.

## Part 1 - Strategic Design
### Chapter 1 - Analyzing Business Domains
- In order to build an effecitive solution it is very important to know the Business Strategy of the organization, understand the problem context and what value is gained by building the software. 
- Business Domain - Defines the main area of activity of the company. eg. Fedex - delivery, Walmart - retail and Starbucks - Coffee
- Companies can have multiple business domains. eg. Amazon.
- Sub Domain - Fine grained area of business activity. 
	- Sum of all the sub domains represents the org's business domain. 
	- Sub domains have to communicate and interact with each other to provide the service to the customer (Business Domain)
- Types of Sub domains :
	- Core
	- Generic
	- Supporting
- Core Sub domains: 
	- What a company does different from its competitors
	- eg. Ride share of Uber, Page ranking of Google etc
	- Core sub domain is generally complex. 
	- 