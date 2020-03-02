# The Python Environment

## Syllabus
  * Environment: Command Line, REPL, Scripting
  * Environment: PyCharm
  * Python: print(), Expressions, comments
    - Chapter 1: 1, 2, 3, 4
    - Chapter 2: 4, 5, 7

## OS Basics

You need to know a bit about the OS you are working on:
  - How to open a command prompt
  - DIR, CD, MKDIR, CP, DEL (different in linux, Mac)
  - Do these things from the file explorer
  - Desktop, pycharm

## Python Interactive
```
C:\Users\tophe>
C:\Users\tophe>py
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> asdf
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'asdf' is not defined
>>> print
<built-in function print>
>>> print "Hello"
  File "<stdin>", line 1
    print "Hello"
                ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello")?
>>>
```

In python2 you didn't need the parens. The interpreter is being helpful.

```
>>> print("Hello")
Hello
>>> a = 5 + 2
>>> print(a)
7
>>> 5 + 2
7
>>> None
>>> a
7
>>> quit
Use quit() or Ctrl-Z plus Return to exit
>>> quit()
```

Nice help system built in

```
C:\Users\tophe>py
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit()
No Python documentation found for 'quit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>>
```

## Scripts

When you leave the interpreter, everything you typed is gone. You can put commands in a text file
and then "run" that file over and over.

Use notepad to make "hello.py"
```
print("Hello")
print("World")
a = 5 + 2
print(a)
```

Then
```
py hello.py
```

You can copy this and email to a friend and edit it and re-run it. This is called programming!

## PyCharm

Pycharm is an IDE. Lets you edit/run/browse all in one place. Editor makes the code easier to understand. Shows
errors right inline.

Launch the desktop icon.

- Create a project
- Hello world
- Pycharm maintains a directory structure

- Files are automatically saved
- Show syntax errors
- Run
- Debug (breakpoints, variables, step-over, step-into)

Definitely worth learning the debugger.

## Downloading the Tools at Home

Show how to install python at home.

Show how to download pycharm at home (free). 



