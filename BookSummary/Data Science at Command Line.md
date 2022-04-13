[BOOK URL](https://datascienceatthecommandline.com/2e/)

![[Datascience_process.png]]

Data science is awesome (OSEMN) 
- Obtain
	- Download from some url
	- Query some database
	- Extract from some file format
	- Generate manually
- Scrub
	- Filter lines
	- Extract columns
	- Fill missing values
	- Convert from one format to another
	- Extract words
	- Replace numbers
	
	> 
	> In Data Jujitsu - the author says
	> In any Data project 80% work is data cleaning
	> 
- Explore
	- Look at the data
	- Derive Statistics
	- Draw insightful visualizations 
- Model
- Interpret
	- Draw conclusions from data
	- Evaluate what your results mean
	- Communicating your results

---

### Chapter 2 - Getting Started

__Five types of Command line tools__
1. Binary executable
2. Shell builtin
3. Interpreted script
4. Shell function
5. Alias

Example of a shell function

```bash
fac() { (echo 1; seq $1) | paste -s -d\* - | bc; }

$ fac(5)
120
```

---

__Combining commands__

![[standard_streams.png]]

```bash
$ curl -s "https://www.gutenberg.org/files/11/11-0.txt" |
> grep " CHAPTER" |
> wc -l
12
```

---

__Redirecting input output__

```bash
cat greetings.txt | wc -l
```

is equivalent to 

```bash
< greetings.txt wc -l
```


> Redirect stderr to /dev/null to suppress errors

```bash
cat movies.txt 404.txt 2 > /dev/null
```

2 refers to the stderr



![[use_of_sponge.png]]

![[read_file_update_write_same_file.png]]


### Chapter 3 - Obtaining Data
### Chapter 6 - Project Management with make
Why make?
- formalize your data workflow steps in terms of input and output dependencies
- run specific steps of your workflow
- use inline code
- store and retrieve data from external sources.

Running tasks
- Configuration file - Makefile
- If the file name is different use the `-f`  option

```Makefile
numbers:
	seq 7
```

In the example above `numbers` is a target and the next line is the rule

If there is no file called numbers, make will call the rule on invocation.

If the targets have to be run even if the file exists or not then at the top of the makefile add an entry called `.PHONY: target1 target2 ...`  This will make sure that make create these targets every time make is called. 

Automatic varialbes

- $@  - expands to the name of the target

```Makefile

numbers:
	seq 7 > $@
```

Willl write the sequence of numbers in to a file called numbers.


![[makefile_example_2.png]]

- Default shell is sh. SHELL := bash tells make to use bash shell
- By default every line in a rule is sent seperately to shell. With special target .ONESHELL we can override this so the rule top10 works.
- .SHELLFLAGS makes bash more strict. 
- $< expands to the nae of the first prerequisite.

### Chapter 7 - Exploring Data
Three perspectives
- Inspect data and its properties - number of features, number of observations etc
- Descriptive stats - features stats, mean, std etc.
- Visualizations of the data - plots

### Chapter 8 - Parallel Pipelines

