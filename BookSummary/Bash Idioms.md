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

> Without the curly braces exit will be considered as next statement and will be executed even if the first command execution doesn't fail

> If parantheses are used instead of the curly braces then the commands will be executed in a subshell.

---

- Closing Compound Commands

> Compund Commands should end with a semi-colon or a new line before the closing brace. If semicolon is used then there should be a space between the semicolon and closing brace.

---

- More than one again

> `&&` and `||` operators have the same precedence and are left associative.

```bash
$ echo 1 && echo 2 || echo 3
```

prints 1 and 2

```bash
$ echo 1 || echo 2 && echo 3
```

prints 1 and 3

> Simple left to right associativity

---

- Don't do this

Instead of this

```bash
if [ $VAR"X" = X ]; then
	echo empty
fi;
```

Use this

```bash
if [[ -Z "$VAR" ]]; then
	echo empty
fi;
```

---
