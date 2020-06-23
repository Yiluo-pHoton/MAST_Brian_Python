Python Tutoring Notes
========
Week 2
-----
* Homework go through
	* Lab
	* `pip` and `pytest`
	* Programming languages

* Outline for this session
	* Numbers and arithmetics in Python
	* Commenting in Python
	* Variables in Python

* Numbers are **objects** to Python
	* Each **objects** has: data and related operations
	* Example: 2 basic number types and 1 derived type
		* **Integers** (like 1, 2, -2): add, subtract, multiply, divide, etc.
		* **Floating point** numbers (like 0.1, 0.2, -3.3): similar operations like integers but not exactly the same
			* Can use *Scientific Notation*: `1e4` means 1 * 10<sup>4</sup>
		* **Complex** numbers (like 1.1 + 5.5j): have two floating point parts, and have operations specific to complex numbers
		* Of course, there are many non-number object types

* Arithmetic Summary
	* Operators
		* `+  -  *  /` add, subtract, multiply, (ordinary) divide
		* `%` modulus operator - ramainder
		* `()` evaluate whatever inside first
		* `**` exponential
		* `//` truncated divide: `7 // 2` will give `3` instead of `3.5`
	* Order of evaluation
		1. `()`
		2. `**`
		3. `*  /  %  //`
		4. `+  -`  
		5. `=`

* Commenting in Python
	* Line commenting: anything placed after `#`
	* Block commenting
	* Sometimes you want to add descriptions to your code
	* Comments are completely ignored by the compilers so you can write whatever that helps you the best
	* Very Important!

* Variables
	* A variable is a symbolic reference to data (It is a name for a piece of your information)
	* You can assign information (such as number or sentence or some other objects to a variable)
	* Variables are reusable
	* We assign a **value** to a variable with the assignment operator `=`
		* `a = 3`
	* We can change the value stored in a variable by just re assigning it a new value (can be a different type, but preferably we keep it consistent)
		* `a = 3.3`
		* `a = 5`
		* `a = "Changed to a string"`
	* You can think of variable names as "pointers" to different objects
		* `x = 5`
		* `y = x`
		* Then `y` would have the value that `x` points to, which is `5` 
* Variable names in Python
	* Can ONLY use letters, digits, and _(underscore)
	* Must NOT begin with a digit or non-alphabet character (except for underscore)
	* CANNOT use Python **keywords**
		* Example: `def`, `False`, `True`, `print`, `abs`, `sum`, etc.
	* Choose brief but meaningful names
	* Camel case style
		* `NumOfCats`, `ExampleFunction`, `WeatherReport`
	* Underscore style
		* `num_of_cats`, `example_function`, `weather_report`
	* Be consistent: use one or the other