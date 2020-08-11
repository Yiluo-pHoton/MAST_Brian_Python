Goals for this lab
----------

By the time you have completed this lab, you should be able to:
<ol>
<li>Use Python strings and string variables </li>
<li>Create test-cases for your programs </li>
</ol>

Step by Step Instructions
-----------
**Step 0:** Create a lab2 directory, and remember to work in this directory.

**Step 1:** Bring up IDLE as usual, and open a new window for function definitions

Start IDLE. Then, select &quot;File-&gt;New File&quot; and add a comment at the top of this new file like the following (with the proper substitutions of course): 

<pre>
# lab2.py
# YOUR NAME, today's date
# a cipher function and test cases
</pre>

Then, save it under the name lab2.py inside your lab2 directory.

**Step 2:** Design rot13 cipher. 
You have been hired as a programmer! Your mission is to write a program that encrypts a string of text (rot is short for rotate):

> Encryption often involves the Caesar cipher - named after Julius Caesar, who used the system to encrypt military messages.  
Many early Internet users also adopted this cipher. Called rot13, the cipher encrypts a message by rotating the plaintext character by 13 positions in the alphabet. For example, "a" becomes "n" and likewise "b" becomes "o". 
The nice thing about rot13 is that the same function can be used to encrypt and decrypt a message (why?).

Write function rot13 - it takes a message as a parameter, and it returns an encrypted string in which all the characters in the message are rotated by 13 places. You may assume that all characters in the message are lower case letters (no upper case letters, spaces, digits or anything else). Here is a skeleton of the function. We have initialized an important variable, and given in-line comments to help you out.

```
def rot13(message):
    result = ""   # starts empty; add one character at a time below

	# loop through each character
    # shift it by 13 places (may wrap around to front of alphabet)
    # add it to the result string
```
Of course you should return the result at the end too.

Hints: Remember the chr() and ord() functions from lecture. Find a mathematical formula that will take the number of one character and transform it to the number of the desired character. You may find the '%' (modulus) operator helpful in your formula.

**Step 3:** Test rot13 cipher

Switch roles between pilot and navigator. The job of the new pilot is to create test strings to test the function. What characters should be in each string in order to fully test the encryption function? How can you test that the function will encrypt a string, and then accurately decrypt the resulting string?

Write the test code below the function definition - not as an indented part of the function itself. This way by running the module, your test cases will execute automatically. Make sure you print to the screen both the original string and the encrypted string.

Be ready to demonstrate your function and test cases to a TA.

**Step 4:** Design and test a more flexible rot cipher
Write and test an encryption function that shifts by a variable number of positions rather than always 13. Just name it rot, but have it take two arguments:

```
def rot(n, string):
```

The first parameter, n is the number of positions by which to shift. So if if n is 13, then rot produces the same result as rot13. The results are different for other values of n though. Here are two example runs from our solution:

```
>>> rot(1,'apple')
'bqqmf'
>>> rot(2,'apple')
'crrng'
```

By the way, with our solution, a string that was previously encrypted by shifting n positions can be decrypted by passing -n to rot:

```
>>> rot(-2,'crrng')
'apple'
```

**Step 5:** Write unit tests for your code.

Now, write at least four tests like in lab1 to test if your function is working as expected. It should somewhat look like:

```python
def test_rot2_apple():
   assert rot(2, 'apple')=='crrng'
```

**Step 6:** Push your code to Github

Use the steps in lab1.5 to push your code to Github. And you are done!

