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