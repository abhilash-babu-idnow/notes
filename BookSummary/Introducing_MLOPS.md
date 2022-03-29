# Part 1 - What and Why?

> MLOps vs ModelOps vs AIOps
> __MLOps__ and __ModelOps__ are the same, but some might argue that __ModelOps__ is bit more generic in the sense that it also includes rule based models in addition to the ML models. __AIOps__ is a different thing altogether and deals with using AI for operations like AI for Devops solviing problems like predictive maintenance, predicting newtork failures etc in advance. 

### Definition and Challenges
- It is the standardization and streamlining of the Machine learning life cycle management. 

![[Simplistic_ML_Model_Life_Cycle.png]]

![[Realistic_ML_Model_Life_Cycle.png]]

Challenges 

- Changing Business needs and Changing Data. It is important to make sure that the model represents the actual Business requirements. 
- Different tools and language is used by Business Leaders, Data scientists, Analysts, Data Engineers, DevOps engineers etc. 
- Data scientists have to often juggle between many roles and often end up with maintaining and deploying a lot of models and sometime models that they didn't even develop. The whole situation then become very complex and chaotic. 


## People of MLOps

![[People_of_MLOps.png]]

### Subject Matter Experts
- ML Model life cycle starts and ends with Subject Matter Experts
- Define Business goals, questions and KPIs (Key performance Indidcators)
- Without inputs from SMEs the models developed by Data Scientits might not bring a lot of value to the business
- Which would lead to less business outcomes which would mean that there wouldn't be more budget for ML projects
- SMEs close the feedback loop by making sure that the model is working as expected. The model metrics will only tell you if the model is working with respect to the data. But SMEs can provide feedback whether the model is answering the business questions and serving the business goals. 
- MLOps should be designed in such a way that
	- SMEs should be able to flag in a scalable way if the model performance drifts.
	- It is transparent to SMEs how the model works, what data processes are being used. 
	- It should be easy for the SMEs to make sure that ML models cater to the internal and external regulations audits etc. 
	- It works as a medium of communication between SMEs and Data scientists.
	- It helps the SMEs understand why the model arrived at a particular outcome (Responsible AI)

### Data Scientists

# Part 2 - MLOps How?
## Developing Models
![[Pasted image 20220329221757.png]]

