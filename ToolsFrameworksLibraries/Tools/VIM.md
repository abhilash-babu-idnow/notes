Notes from the book VIM 101 hacks and VIM 

- Sort the file content
	- `:sort` command
	- Select the text you want to sort in visual mode, then press `:`  which will show `:'<,>'`  at the bottom. Then type `!sort` -> `:'<,>'!sort`
	- `sort!` to sort in descending order
	- `sort i` to ignore case
	- `sort u` to remove duplicate lines
	- `sort ui`  a combination of above two
	
- Recover Deleted text
	- `"1p`  Recovers the last delete
	- `"2p`  Recovers the second last delete
	- `"3p`  Recovers the third last delete
	- `"1pu.u.u.`  Browse all the delete buffers 

- Change Case
	- `~`  Changes the case of the character under the cursor
	- `5~` Changes the case of 5 characters
	- `g~(motion key)` Changes the case of the characters covered by the motion. eg `g~$` Changes the case of all the characters until the end of the line.
	- `g~~` Changes the case of the entire line
	- `gUU` Changes the case of the entire line to upper case
	- `guu` Changes the case of the entire line to lower case
	- `gUaw` Changes the current word to Upper case
	- `guaw` Changes the current word to lower case
	- `U` Visual mode change to upper case
	- `u` Visual mode change to lower case
	- `guG` current position to end of the file lower case
	- `gUG` current position to end of the file upper case.

