# Chapter 1 - Probably approximately correct software. 

## Writing software right 
Write the software right by following the SOLID, TDD and Refactoring principles. 
### SOLID 
> Single Responsibility Principle
Have a piece of software do one thing and only one thing.

> Open Closed Principle
Open for extending but closed for modification.  (Encapsulation of objects)

> Liskov Substitution Principle
Any subtype should be easily substituted out from underneath a object tree without side effect

> Interface Segregation Principle
Having many client specific interfaces is better than a general interface for all clients

> Dependency Inversion Principle
Depend on abstractions and not concretions. We should build a layer or inheritance tree of objects. 

### TDD 
> Write a test to record what you want to achive -> Test to make sure that the test fails first -> Write the code to fix the test -> Refactor -> Test 

### Refactoring
Should be followed to reduce the *technical debt* 
> Technical debt is a metaphor for poor system design that happens over time with software projects. It accrues interest and eventually blocks future feature development. 

## Writing the Right Software
> In theory, theory and practice are the same. In practice they are not. -- *Albert Einstein*

Best approach is to craft specification first and then code to fit that spec. Downfall is the our assumtions made during the modelling can be wrong. 

## Writing the Right Software with Machine Learning.
> Deduction = complex logic models -> conclusion
> Induction = collect ground truth data -> fit a model to the data

### SOLID applied to Machine Learning. 
* SRP 
	* Data and code are dependent on each other. CACE (Chaning Anything Changes Everything) also called *Entaglement*
	* Glue code overtime tends to solve all problems instead of just one. 
* OCP 
	* Hidden feedback loops e.g. predicitive policing.
* LSP
	> Ockhams Razor -> The simplest solution is the best one. 

# Chapter 2 - A quick introduction to Machine learning. 

> Machines making sense out of data. Extract patterns from data
> Supervised, Unsupervised and Reinforcement learning. 

## Supervised Learning. 
Function approximation - fitting data to a function
## Unsupervised Learning.
Clustering 
## Reinforcement Learning
Learning throught rewards and payoffs. 

# Chapter 3 - K Nearest Neighbors

> Things are worth as much as someone is willing to pay.  - Old Saying. 

## Hedonic Regression
> Real life hedonic regression example - CPI index (index of inflation)

**Instead of focussing on fitting a curve to a bag of attributes, it focuses on the components** For example hedonic method can be used to estimate how much a bedroom costs. 

# Chapter 4 - Naive Bayesian Classification

## Conditional Probability

**P(A|B) = P(AB) / P(B)**

## Bayes Theorem 

**P(B | A) = P(A | B) * P(B) / P(A)**
