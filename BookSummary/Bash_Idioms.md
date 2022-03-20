title: Bash Idioms
start date: 18-03-2022

---

- If  -- This bash idiom provides the conditional execution of second command. The second command is run only if the first doesn't fail. 

```bash
[[ -n "$DIR" ]] && cd "$DIR"
```

> If the length of the value of the variable DIR is non zero then cd to that directory

```bash
if [[ -n "$DIR" ]]; then
	cd $DIR
fi
```

---

- else -- Similar to the previous one. But in this case the second command is executed if the first command fails.

```bash
[[ -Z "$DIR" ]] || cd "$DIR"
```

> Check if the length of the variable DIR is zero. If it fails then cd  to that directory

```bash

if [[ -Z "$DIR" ]]; then
	:
else
	cd "$DIR"
fi
```

> `:` is a null statement

---

- More than one

```bash
cd /tmp || { echo "cd to /tmp failed" ; exit ; }
```

> Without the curly braces exit will be considered as next statement and will be executed even if the first command execution doesn't fail.

---

- 