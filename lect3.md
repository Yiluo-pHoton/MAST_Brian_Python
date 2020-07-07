**Importing from a Module**  

* Suppose the `drawSquare` function is in a file on your computer called `ds.py`
* We have two basic choices to use this function:
	1. Import the whole module, and specify the part of the module to use
	2. Import part(s) of the module, then just use the part(s)

```
>>> import ds
>>> ds.drawSquare(t, 20)
```

```
>>> from ds import drawSquare
>>> drawSquare(t, 20)
```

* Of course, Python must be told where `ds.py` is on the computer
	* Store the file in the same directory where you are running Python
	* In Python IDLE, go to **File -> Open** and open `ds.py`

	
**Conditional Statements**

```python
if conditional_statement:
	# block of code
elif:
	# block of code
else:
	# block of code
```

Conditional statements follow **Boolean logic**, that is, they are either `True` of `False`

* Less than `<`
* Greater than `>`
* Less or equal `<=`
* Greater or equal `>=`
* Equals `==`
* Not equal `!=`

**Boolean logic**

* AND: true if all the conditions are true
* OR: true if any of the conditions is true
* NOT: true if condition is false; false if condition is true


**Nested if statements**

```python
a = 10
b = 15

if (b == a):
	print("They are equal")
else:
	if a > b:
		print("a is greater than b")
	else:
		print("a is smaller than b")
```

**for loops**

```python
for ref in list:
	#block of code
```

`for` and `in` are mandatory

Example:  

```python
for number in (0,1,2,3,4,5):
	print(number)
```
Using `range()` built-in function provides a handy list:
Simplest use: `range(n)` creates a list with n items `[0, 1, 2, 3, 4..., n-1]`

```python
for number in range(6):
	print(number)
```

`range()` with start and stop:

```python
for number in range(5, 8):
	print(number)
```

`range()` with start, stop, and step parameters:

```python
for i in range(1, 11, 4):
	print(i)
```
will print 1, 5, 9

**Turtle and for loop**

Remember we wrote a `drawSquare()` last time, where we copied and pasted many lines that we wrote, but now we can write a for loop to save the work:

```python
def drawSquare2(my_turtle, side_length):
	for i in range(4):
		my_turtle.forward(side_length)
		my_turtle.right(90)
```

Small variation draws a spiral:

```python
def drawSpiral(my_turtle, max_side):
	for side_length in range(1, max_side + 1, 5):
		my_turtle.forward(side_length)
		my_turtle.right(90)
```