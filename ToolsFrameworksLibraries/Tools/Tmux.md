```bash
# Split window
bind | split-window -h
bind - split-window -v

# Select pane
bind h select-pane -L
bind l select-pane -R
bind j select-pane -D
bind k select-pane -U

# Select pane witout prefix
bind -n M-h select-pane -L
bind -n M-l select-pane -R
bind -n M-j select-pane -D
bind -n M-k select-pane -U

# Close Pane without prompt
bind x kill-pane
bind X kill-session

# swap windows with shift+arrow with prefix
bind-key S-Left swap-window -t -1
bind-key S-Right swap-window -t +1

# Count windows from one instead of zero
set -g base-index 1

# Enable mouse support
set -g mouse on

# -------------------------
# Plugin configuration
# -------------------------
# restore vim sessions
set -g @resurrect-strategy-vim 'session'
# restore neovim sessions
set -g @resurrect-strategy-nvim 'session'
# restore panes
set -g @resurrect-capture-pane-contents 'on'
# restore last saved environment (automatically)
set -g @continuum-restore 'on'
```



## Useful commands

### Panes

| Command | What it does? |
|---|---|
|`<prefix> !` | Break out the pane into a new window |
|`<prefix> z` | Zoom the pane. Toggle switch. |

### Windows

|Command|What it does?|
|---|---|
|`<prefix> 0-9` | Switch between windows 0 to 9 |
|`<prefix> c` | Create a new window |
|`<prefix> ,` | Rename the window |
| `<prefix> w` | Choose window from a menu |
| `<prefix> n`  | Choose the next window |
| `<prefix> p`  | Choose the previous window |

### Session

| Command | What it does? |
|---|---|
| `<prefix> (` | Switch to previous session |
|`<prefix> )`| Switch to next session |
|`<prefix> s` | Choose from a list of sessions |
|`<prefix> $`| Rename the session |
|`<prefix> d`| Detach from the session |

### Copy Mode

|Command | What it does? |
|---|---|
| `<prefix> [`  | Enter Copy mode |
| `<prefix> ]` | Paste Current Buffer |
| `<prefix> =`  | List all buffers and choose one from which to paste |
| `<space>` | Start selection in copy mode |
| `<enter>` | Exit copy mode and copy selection to buffer |


## Plugins
1. Clone the github [repo](git clone https://github.com/tmux-plugins/tpm) to the folder  `~/.tmux/plugins/tpm)`  
 
```
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

2. Edit the tmux conf and add the following to the bottom 

``` bash
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com:user/plugin'
# set -g @plugin 'git@bitbucket.com:user/plugin'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```

3. Source the tmux conf or restart tmux
4. Install plugins with the command `<prefix> I`


## Copy Mode
* Command to enter Copy mode is `<prefix> [` 
* Press `<enter>` to exit the copy mode.
* Select text from buffer in copy mode using the `space` key. Press `<enter>` to exit copy mode. Now if you press `<prefix> ]` , the selected text will be pasted to tmux session.
* `<leader> : show-buffer<enter>`  Willl show the text copied in the copy mode buffer.
* `<leader> : choose-buffer<enter>`  Will show list of all the current buffers, navigate select by presseing `<enter>` to select one of the buffers. Or use `<prefix> =`
* Set the following the `.tmux.conf` to enable vim keys for navigating in copy mode: `setw -g mode-keys vi`
* To capture the contents of the pane to a text file do the following
	* Enter command mode `<prefix>:`
	* Type `caputer-pane; save-buffer ~/buffer.txt<enter>`
* Or may be add a short cut 
	* `bind C-s run "tmux capture-pane && save-buffer ~/buffer.txt"

