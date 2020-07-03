Python Tutoring Notes
========
Week 3
-----
* Homework go through
	* Lab
	* Homework sheet

**Overview**  

* Function and function call
* Module and object
* Turtle module
* Function call with module
* Defining your own function

**Function**

* Function is a self contained module that accomplish a specific task.  
* It always "carry" braces.  
	* Example: `sqrt(25)` will give 5

* It can have no input or some inputs.
* It can have no output or some outputs.
	* Example: `moveForward()`, `append()`, `sum()`
* Function can be used over and over again

**Module**

* You can think about a module as a block of code that contains definitions for certain things
* It can contain many variables and functions that describes the module
	* Example: Piano

~~~python
def Piano():
	...
	color = "black"
	num_of_keys = 88
	num_of_pedals = 3
	
	def play_C4():
		# Make the central C sound of a piano
		...
	
	def rest(length):
		# Rest for the amount of time specified by length
		...
	
	def set_color(color):
		# Set the piano color to the one specified by "color" parameter
	
	...
	
	def play_chopin():
		# Use the previous definitions to play Chopin
		...
~~~

Then in my `main` block of code, I can create multiple "instances" or "objects" of the module `Piano`

~~~python
my_first_piano = new Piano()
my_second_piano = new Piano()

my_first_piano.set_color("red")
my_second_piano.set_color("green")
~~~

**Turtle module**  

* A `turtle` is similar to the `Piano` module
* It is graphic module that is created for you to use
* To use it in Python, first "import" it 

`>>> import turtle`

* To create an instance of the turtle, do the following and don't worry about what it means for now

`>>> t = turtle.Turtle()`

~~~python
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
>>> t.right(90)
>>> t.forward(50)
~~~

**Function call with module**

* Recall that we call/invoke a function by `function_name(some arguments)`
* There can be no argument `function_name()`
* There can be multiple `function_name(first_param, second_param, third_param)`
* When you call a function that is defined inside a module, you use the `.` operator
* The syntax of it looks like this

`module_name.function_name(...)`

* Or it could be like this when you are using a function inside an object

`object_reference_name.function_name(...)`

**Defining your own function**

~~~python
def function_name(list of parameters):
	# a block of statements and operations appear here
	# all of them MUST be *indented* (with tabs)
~~~

`def` - a mandatory keyword that **defines a function**  
`function_name` - any legal Python identifier  
`():` - a mandatory set of parentheses AND colon  
`list of parameters` - object names to be used only inside this function; they are only local reference (not global)  

~~~python
def distance(x, y):
	return (x ** 2 + y ** 2) ** 0.5
~~~

**Combine function definition with module**  

~~~python
def draw_square(my_turtle, side_length):
	my_turtle.forward(side_length)
	my_turtle.right(90)
	my_turtle.forward(side_length)
	my_turtle.right(90)
	my_turtle.forward(side_length)
	my_turtle.right(90)
	my_turtle.forward(side_length)
~~~
Then to call this function:

~~~python
draw_square(t, 100)
~~~