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

-  Undo and Redo
	- `u`
	- `5u` undo last five changes. 
	- `U` undo all changes
	- `Ctrl - r`  redo changes

- Add bullet point style to list of items
	1. Select the text in Visual mode. 
	2. Press `I`  and then press `Tab * Space`
	3. Press `Esc Esc`

- Scrolling 

	| Key       |       Description|
	|---          | ---|
	| `Ctrl F`  | Scroll down the full page |
	| `Ctrl B`  | Scroll up a full page |
	| `Ctrl D`  | Scroll down half page |
	| `Ctrl U`  | Scroll up half page |
	| `Ctrl E`  | Scroll down one line |
	| `Ctrl Y`  | Scroll up one line | 

- Word Navigation 

	|  Key | Description |
	| --- | --- |
	| `w`  / `W` | Beginning of next word/Word | 
	| `e`  / `E` | End of next word / Word |
	| `b`  / `B` | Beginning of previous word/Word |

- Screen Navigation 

	| Key | Description | 
	| --- | --- |
	| `H`  | Go to line 1 of the screen | 
	| `M`  | Go to  middle of the screen | 
	| `L`  | Go to tthe last line of the screen | 

- Redraw screen with current line at top, bottom or middle

	| Key | Description |
	| --- | --- | 
	| `z<Enter>` | top |
	| `z-` | bottom |
	| `z.` | middle | 
	
	
- Source code navigation

	| Key | Description |
	|---| ---|
	| `%` | Jump to matching pair |
	| `[(` | Go to previous unmatched ( |
	| `[)` | Go to previous unmatched ) |
	| `[{` | Go to previous unmatched { |
	| `[}` | Go to previous unmatched } |

- Insert mode navigaion 

	| Key | Description |
	| --- | --- |
	| `Shift ->`  | Go right word by word |
	| `Shift <-`  | Go left word by word |

- 