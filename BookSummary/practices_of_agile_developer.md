% Practices of Agile Developer
% Abhilash's notes
% 23.01.2022

## Agile Manifesto
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
-  Customer collaboration over contract negotiation
-  Responding to change over following a plan

---

- Anything substantive that you leave until later won't happen, won't happen well or will grow and become unmanageable. Continous development, not episodic. Tackle small problems when they are still small. 

- Agile development uses feedback to make constant adjustments in a highly collaborative environment. 

---

## Beginning agility
### Work for outcome
	- Fixing the problem is top priority and not what and who caused the problem. 
	- Blame doesn't fix bugs. 
	- Instead of pointing figures point to possible solutions. 
	- Agile teams value outcome over process
	- Measuring compliance to process doesn't measure outcome.

---

###  Quickfix becomes quicksand
	*  Each quick fix will pile up and eventually the code base becomes a landmine
	*  Don't code in isolation (bus factor), code reviews, collective ownership.
	*  Use unit tests. 
	*  Invest energy to keep code clean and out in the open
	*  You need to understand how a piece of code works but no need to become an expert. 
	*  Fix the problem not the symptom ( +1/-1 syndrome)

---

### Criticize ideas, not people
	* Ask a leading question that allows someone to figure out the problem themselves. 
	* **Negativity kills innovation**
	* All have some good ideas and some bad ideas and everyone in the team should feel free to express them. 
	* >You don't have to be great to get started but you need to get started to be great -- Les Brown. 
	* Being unemotional doesn't mean to blindly accept all ideas but to choose the right words and reasons to explain why the idea doesn't fit and ask clarifying questions. 

---

### Damn the Torpedoes, Go ahead
	* You have been asked to fix some code written by someone else and it is very difficult to understand. Should you leave it in a mess or inform your boss that it should be removed? Show and reason about why the code should be rewritten. 
	* If you implement something incorrectly. Should you cover up the issue or standup and ask for time/help and suggest ideas to fix? Latter as you will not only have a proper solution you will earn the trust of the team. 
	* Do what's right. Be honest and have the courage to communicate the truth. It may be difficlut at times. 
	* Don't start rejecting and rewriting simply because you can't understand rightaway. That's not courage, its impatience. 

---

## Feeding agility

---

### Keeping up with change
		- Technology changes very fast and it is our responsibility to keep up.
		- Learn iteratively and incrementally, allocate daily some time for study.
		- Get the latest buzz from the internet, mailing lists, twitter feeds etc
		- Improve networking by participating in local meetups.
		- Attend conferences. 
		- Read books.
---
### Invest in your team
		- Use "Brown bag sessions" to share knowledge with the team
		- Pick up a topic, tool or book and one of the team members can present it. 
		- Raise the bar for you and for your team. 
		- Stick to a reguar schedule. 
		- Use not just technical books and topics but also non technical stuff
---
### Know when to Unlearn
		- Like learning new stuff it is equally important to let go old techniques which are not relevant. 
		- Example compilers now are very efficient and smart and can do optimization way better. So no point in doing the optimization like loop unrolling etc by hand. One should just leave it to the compoiler to sort it out.
---
## Agile Feedback
### Put Angels on Your Shoulders
		- Coding feedback through testing. 
		- Automate the unit tests.
---
### Use it buid you build it
		- Eat your own dog food
		- Use TDD

---
### Different makes a difference

---
### Automate acceptance Testing

---
### Measure Real Progress

---
### Listen to Users

---
## Agile Coding
		- blah blah
---
### Program intently and expressively
		- add more content
---
### Communicate in Code
		- todo
---
### Actively evaluate trade offs
		- todo
---
### Code in increments
		- Write code in short edit build test cycles
		- Helps to refine and structure the code better.
		- Refactor the code as well as the tests.
---
### Keep it simple
		- Try to make the design as simple as possible.
		- Don't try to use patterns and principle just for the sake of using them. 
		- "A good design makes you feel comfortable"
		- Terse is not simple. 
		- What is simple might not be simple for others. 
---
### Write Cohesive code
		- High cohesion and low coupling. Software architecture 101.
		- A module should have only one reason to change.
		- Don't take it too far with breaking down code into components just to satisfy the rule of each component doing just one thing. 
---

### Tell Don't Ask

		- Command Query Separation
		- Categorize the functions as either commands and queries. 
		- Queries should be side effect free
		- Command changes the state of the objet. 
---

### Substitute by Contract
		- todo