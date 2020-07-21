**Homework and Lab**

Code from last time

```python
def drawSpiral(my_turtle, max_side):
	for side_length in range(1, max_side + 1, 5):
		my_turtle.forward(side_length)
		my_turtle.right(90)
```
* Github
* Lab 1

**String**
Strings are basically sequences of characters    
A string is enclosed in quotes, either `''` or `""` in Python  
Strings are objects of a Python class named `str`  
This is not the case for other variables, like integers  

```python
type('kitty')
type(13)
type(13.3)
```

We can assign names to these variables like any other type of objects

```python
message = 'Need to practice!'
print(message)
```


**Operations on Strings**
There are a lot of built-in functions that work for string, and `class str` has many useful operators and methods too

* Concatenation
	* Merging multiple strings into 1
	* Use the `+` operator
	* `"string1 " + "string2"` will become `"string1 string2"`

* Repetition
	* Use the `*` operator
	* `"ja " * 3` will become `"ja ja ja "`

* Indexing
	* Every character in a string has an index associated with it
	* The index starts from 0
	* `name = "Brian"`
	* `name[0]` will give `'B'`
	* `name[5]` will give error `index out of bound`

* Functions for String
	* `len(string)`: `len("Python")` will give 6
	* Slicing: use `[i:j]`
		* Where i = starting index, j = ending index (NOT included)
		* Example: `"Gaucho"[2:4]` is `"uc"`
	* You can combine all these operations
		* `( ("o" + "Gaucho"[2:5] + " " ) * 3 ) + "!"`
	* `in` and `not in` operators
		* `'fun' in 'functions'` is `True`
		* `'fun' in 'Functions'` is `False`
		* `'Fct' not in 'Functions'` is `True`
	* `find()`
		* `"hello".find("h")` gives 1
		* `"hello".find("g")` gives -1 (meaning no such substring)

* Functions `chr()` and `ord()` 
	* Characters are stored as numbers in computer memory
	* There are standard codes for characters, e.g. ASCII, UTF-8, etc
	* For example, `'A'` has code 65 in ASCII
		* Use the `ord()` function to verify this: `ord('A')`
		* Notice `'A'` is not same as `'a'`: `ord('a')` is 97
	* Use `chr()` to find corresponding chracter given a code
		* For example, `chr(65)` will give `A`
	* You can manipulate numbers in order to process characters
		* `chr( ord('a') + 3)` is `chr(97)`, which is `'d'`
	* Notice digit characters have codes too!
		* `ord('6')` is 54
	* Examples
		* How can I find out what’s 13 letters after `‘e’`?
			* `chr( ord('e') + 13 )`
		* What’s the ASCII code for the hashtag character?
			*  `ord('#')`, which is 35 