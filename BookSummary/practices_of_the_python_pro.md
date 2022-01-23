# Practices of the Python Pro (Notes)

> Provides a set of principles for producing shareable, reusable software.

## Part 1 - Why it all matters
### The bigger picture

## Part 2 - Foundations of design
### Separation of concerns
clear code - segregate distinct behaviours (concerns) - simpler to reason 

#### Namespacing
avoids name collision - helps guess location of code - will help guide where to add new code - part of **zen of python** - *Namespaces are one honking great idea - let's do that more of those!* - built-in namespace contains all that is built into python - no need to explicitly create namespaces 

> built-in namespace -> module namespace -> local namespace (classes, functions etc)

@todo - lookup difference between namespace and scope in the context of python. both sounds the same from the above explanation. 

### Abstraction and Encapsulation
### Designing for high performance
### Testing your software

## Part 3 - Nailing down large systems
### Separation of concerns in practice
Helps in _code reuse, improved maintainability and ease of extension and generalization_ - A typical way to achieve seperation of concern is to use a layered architecture - for example an application could be split up into having a presentation layer (UI), a business logic layer and a persistence layer (DB) - Example patterns MVC, MVVM etc
### Extensibility and flexibility
### The rules of inheritence
### Keeping things lightweight
### Achieving loose coupling

## Part 4 - What's next?