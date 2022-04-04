
# TDD MOOC from University of Helsinki
[URL](https://tdd.mooc.fi/)

![[tdd.png]]


## Chapter 1 - What is TDD
- idea from Kent Beck.
- Three rules of TDD
	- *You shall not write any production code, unless required by a failing Unit test*
	- *You shall not write more of a unit test, than is required to fail*
	- *You shall not write more production code ,than is sufficient to make the one failing test pass*
- Red Green Refactor
	- Red - Write a failing test case
	- Green - Make the test pass
	- Refactor - Improve the design of the code without changing its behaviour

---

- Direct and Indirect effects of TDD
	- Direct
		- Guarantees code coverage
		- Amplifies pain caused by bad code.
	- Indirect
		- Improves quality of code
		- Enable chaning code without breaking it.

## Chapter 2 - Refactoring and design
- Four elements of simple design
	- Priority order
		- Passes its tests
		- Minimizes duplication
		- Maximizes clarity
		- Has fewer elements
- Duplication
	- DRY 
	> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system. 
	> - Andy Hunt and Dave Thomas, The Pragmatic Programmer (1999)
	- Rule of three - Three strikes and you refactor
		- Wait until code is repeated in three places and then refactor
	- Naive duplication 
		- Not all code that looks similar is duplicated knowledge. Even if chairs and dogs have four legs they are not related. 
- Naming Things.
	- Quote
	> There are only two hard things in Computer Science: cache invalidation and naming things. 
	> Phil Karlton


	- Naming is a process -> nonsense -> accurate-but-vague -> precise -> meaningful.
- Composed Method
	-  Code should read like a newspaper article. First the high-level overview, then dig deeper into more details. 
	
	__Composed Method Pattern__ [source](https://farenda.com/patterns/composed-method-pattern/)

	-> Purpose
		Extend and maintain low quality code
	-> How?
		Apply Extract Method refactoring on logically coherent blocks of code until all are in separate methods. Names of method tell what they do.
	-> SLA Principle (Single Level of Abstraction)
		All steps of processing in a method should not expose their details but move the details to separate methods that give them intent-revealing names. 
	-> Pros
		- Helps find duplicate code
		- Helps to identify responsibilities
		- Makes unit testing easy
		- Makes code readable
	-> Cons 
		 - Creates more small methods
		 - Logic is spread across a lot of methods. 
- Small safe steps