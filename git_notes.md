
## Notes from the book - A Hackers guide to git.

> Git doesn't work like Subversion.
> Intention of the book is to look under the hood and see how git works internally.

### Repositories.

* A git repo is just a key-value store and it stores
  * Blobs - usually a binary representation of the file
  * Tree - like dictionaries - contains pointers to blobs and other tree objects
  * Commits - points to a single tree and also contains some meta data like commit author, comments and parent commit etc
  * Tag - points to a single commit and contains meta data
  * References - pointers to single object (commit or tag object)

> exists entirely in single **.git** directory
> no central repository ( hence distributed version control system )

> initialize a git repo with the command **git init**

Important directories in .git

* .git/objects - where objects are stored :smirk:
* .git/refs - where references are stored :bowtie:

### Tree Objects

* Like a directory
  * with a list of directories (read blobs)
  * subdirectories (read other tree objects)

### Commits
> git show --format=raw partial_hash
> Above command will show the commit's metadata

### References
A **reference** is just a file in .git/refs that contains the hash of a commit object.

> branches are just references
> HEAD is the reference to the current branch.

Switching to a new branch

> cat .git/HEAD
> ref: refs/heads/master
> git checkout test-branch
> Switched to branch 'test-branch'
> cat .git/HEAD
> ref: refs/heads/test-branch

### Tags
There are two types of tags in git
* lightweight tags
  * Default type of tag created.
  * Just a reference to the commit object.
* annotated tags
  * created with the command `git tag -a -m "Tagged 1.0" 1.0`
  * tag object, a reference to a commit obj.
  * contains other meta infomation like author of the tag.
  * timestamp of the tag creation etc.


### Merging.

> Joining of two histories (branches) together. 


### Cherry Picking. 
Takes one or more commits and replays them on the top of the current commit. 

![[Pasted image.png]]
becomes  

![[Pasted image 1.png]] when the following command is executed. 

`git cherry-pick F`

### Rebasing. 
> Hey, I want to pretend that <target> was actually branched from <base> . Take all the commits from <target> and pretend that they happened after <base>.