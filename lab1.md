Lab 1
---------
In this lab, you will get familiar with the basic commands in terminal.

# Step 1: Making and removing folders
1. Open up a terminal. You can find it through typing "terminal" in the Spotlight, or go to the "Application" folder and find it there.
2. Type in `cd Desktop` and hit the return button. This should take you to the "Desktop" folder in the terminal.
3. Type `mkdir new_folder`. You should see a folder on your desktop called "new_folder" now.
4. Type `mv new_folder renamed_folder` to rename this folder.
5. Type `mkdir another_folder` to create another folder.
6. Type `mv another_folder renamed_folder` to see the `another_folder` moved into the `renamed_folder`.
7. Type `cd renamed_folder` to get into the directory of `renamed_folder` in terminal.
8. Type `pwd`. This means "path to the working directory". It will tell you where you are at in the terminal. You should see something very similar to this: `Users/<your_computer_name>/Desktop/renamed_folder`
9. Now type `cd ..`, where `../` means the parent directory of current directory, so this command will take you back to the `Desktop` directory.
10. Type `ls` to see a list of folders for your current directory (so for this case, you should see a list of file and folder names that are on your desktop). You should see `renamed_folder` among the list as well.
4. Type `rm -r renamed_folder` to remove this folder.
5. Type `ls` to list the files and folders. Now you should see that the `renamed_folder` is gone.
6. Type `cd` to return to the home directory. Now if you type `pwd` you should see something like `/Users/<your_computer_name>`. This is your home directory. You can do this in any directory, and typing `cd` will take you back home. Note that if you type `cd ~` in any directory, it will have the same effect.

To sum up, we have tried the following:

* `cd` returns you to your home directory (e.g. `/Users/<your_computer_name>`)
* `pwd` prints your current working directory
* `cd some_folder` changes into the some_folder directory under the current directory
* `cd ~/some_folder ` changes into the cs8 directory under your home directory regardless of the current working directory (because `~` is a shortcut for the absolute path of
   your home directory.)
* `cd ..` will move you up one directory from your current directory (i.e. if you are in `/Users/Brian/Desktop/some_folder`, using `cd ..` will take you to `/Users/Brian/Desktop`). 
* `mkdir folder_name` will create a directory called `folder_name`under your current working directory
* `ls` lists the files and folders in your current directory
* `rm -r folder` will remove the `folder`
* `rm filename` will remove a file named `filename`. Note the difference between file and folder. Things like `homework.md` and `application_form.txt` are files. They are different from folders.

# Step 2: Do it yourself
* In this step, you will create a folder that will contain all of your future lab code. 
* You can name it something like `Python_tutor`. 
* Inside this folder, you will create another folder called `lab1`. 
* Go into this `lab1` folder through your terminal, and type `pwd`. Once you are done, take a screenshot to turn in as the result for this lab.

------
**IMPORTANT**: If you find the following content challenging, you could stop here. We could do the rest of this lab next week after we cover the idea of function and function call in Python.

------

# Step 3: `convert.py`
* Create a file in your `lab1` folder, and call it `convert.py`
	* Choose "File => New File" in IDLE to bring up an "untitled" window, then copy and paste this code into that window, and save it in the `lab1` folder.

```python
def fToC(fTemp):
    return fTemp - 32  # TODO: Fix this line of code

def cToF(cTemp):
    return cTemp + 32 # TODO: Fix this line of code
``` 

Note that the formulas for converting between Celsius and Fahrenheit are incorrect.  That's deliberate, so just go with it for now.  We'll fix those at a later step.

# Step 4: Test your code by hand

To test this code, we'll first do what many programmers do: test the code by hand.  

That is, we'll run the file in IDLE, and then enter some function calls in the Python shell to see what results we get.  These two functions are supposed to convert between Fahrenheit where water freezes at 32 degrees, and Celsius where it freezes at 0 degrees.  Let's see if they work properly.

Use the Run Module command to run the code, and then try entering these function calls at the Python Shell prompt.  You should see output similar to what is shown below:

```
>>> fToC(32)
0
>>> cToF(0)
32
>>> 
```

As you can see, for those two particular values, the function appears to return the correct answer&mdash;32 degrees fahrenheit is indeed 0 degrees celsius, and 0 degrees celsius is indeed 32 degrees fahrenheit.  

So clearly, testing with a single value is not enough.  Indeed, if we test with another well known value, 212 Fahrenheit and 100 Celsius (the boiling point of water), we see that the output is incorrect:

```
>>> fToC(212)
180
>>> cToF(100)
132
>>> 
```

One of the problems with testing by hand is that it is tedious, and folks have a tendency to skip it.  So, experienced programmers have learned that its generally a better idea to automate the process of testing.     We'll learn how to do that next.   We'll see that when we set up these four tests, two of them will pass, and two of them will fail.

# Step 5: Setting up automated tests

Add this line at the top of your convert.py file:

```
import pytest
```

Then, add the following code to your `convert.py` file after the function definitions for `ftoC` and `cToF` that defines four automated tests:

```
def test_fToC_freezing():
   assert fToC(32.0)==pytest.approx(0.0) 

def test_cToF_freezing():
   assert cToF(0.0)==pytest.approx(32.0) 

def test_fToC_boiling():
   assert fToC(212.0)==pytest.approx(100.0) 

def test_cToF_boiling():
   assert cToF(100.0)==pytest.approx(212.0) 
```

These are automated tests that use a module known as `pytest`.  When defining tests using the `pytest` module, we typically define functions that:

* have names that start with `test_` or end with `_test`
* end with exactly one `assert` statement&mdash;that is, the keyword `assert` followed by a boolean expresssion.  

If the expresssion after `assert` is true, the test passes, otherwise it fails

We are using `pytext.approx()` here because any time you are testing with floating point numbers, we have to be aware that there may be some inaccuracy, as we discussed earlier.  

(Recall our discussion of what happens when you multiple `math.sqrt(2.0)` by itself.  Here, its probably overkill since we aren't using any irrational numbers, but it is still safer to always use some way of approximating equality when dealing with floating point.)

You can click the plus to open a dropdown showing what your entire file should look like at this point:


**Contents of `convert.py` so far**

```
import pytest

def fToC(fTemp):
    return fTemp - 32  # TODO: Fix this line of code

def cToF(cTemp):
    return cTemp + 32  # TODO: Fix this line of code
    
def test_fToC_freezing():
   assert fToC(32.0)==pytest.approx(0.0) 

def test_cToF_freezing():
   assert cToF(0.0)==pytest.approx(32.0) 

def test_fToC_boiling():
   assert fToC(212.0)==pytest.approx(100.0) 

def test_cToF_boiling():
   assert cToF(100.0)==pytest.approx(212.0) 

```


After entering this, save the file and use "Run Module" to make sure there are no error messages (red output in the Python Shell Window.).  If not, then you are ready for the next step.
            
# Step 6: Running the test cases
        
Running the test cases requires us to go <em>outside of IDLE</em> back to the terminal shell prompt.  

Your current directory needs to be the same one that your convert.py file is stored in.    That means you should be in `lab1` directory, but if it isn't, then fix things so that the `convert.py` file is in that directory, and you are in that directory.   If you need help, ask me for assistance.

You should be able to type the `ls` command at the terminal shell prompt and see the `convert.py` file listed:

```
lab1 $ ls
convert.py
lab1 $ 
```

When that's the case, try this command:

```
python3 -m pytest convert.py
```

You should see output like this.  It may be a little overwhelming at first, but don't let it intimidate you. Once you know what you are looking for, it is very easy to read.    After the output, there is a guide to understanding it.


```text
169-231-175-204:lab01 photon$ python3 -m pytest convert.py
==================================== test session starts ====================================
platform darwin -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/photon/Desktop/MAST_python/lab01, inifile:
collected 4 items                                                                            

convert.py ..FF

========================================= FAILURES ==========================================
_____________________________________ test_fToC_boiling _____________________________________

    def test_fToC_boiling():
>      assert fToC(212.0)==pytest.approx(100.0)
E      assert 180.0 == 100.0 ± 1.0e-04
E       +  where 180.0 = fToC(212.0)
E       +  and   100.0 ± 1.0e-04 = <function approx at 0x1026c40d0>(100.0)
E       +    where <function approx at 0x1026c40d0> = pytest.approx

convert.py:16: AssertionError
_____________________________________ test_cToF_boiling _____________________________________

    def test_cToF_boiling():
>      assert cToF(100.0)==pytest.approx(212.0)
E      assert 132.0 == 212.0 ± 2.1e-04
E       +  where 132.0 = cToF(100.0)
E       +  and   212.0 ± 2.1e-04 = <function approx at 0x1026c40d0>(212.0)
E       +    where <function approx at 0x1026c40d0> = pytest.approx

convert.py:19: AssertionError
============================ 2 failed, 2 passed in 0.03 seconds =============================
169-231-175-204:lab01 zmatni$ 
```

Ok, let's now break down this output.

# Step 7: Understanding the output of pytest

Here's how to understand `pytest` output. 

1. <b>Get the big picture first from the <tt>convert.py ..FF</tt> line</b>. 

   Look for a line near the beginning that has the name of your file, followed by a list of either dots, 
   letter 'E' or letter 'F' characters, like this one:

   ```
   convert.py ..FF
   ```
   
   In this case, the `.` characters are tests that passed.  If you have four tests, the ideal thing you'd want to see is <tt>convert.py&nbsp;....</tt> which means that four tests for <tt>convert.py</tt> all passed. 
   
   Instead, here, we see `..FF`, which means we had two test failures.   Later in the output, we'll see more detail about
   each of those failures.
   
2. **Understand the overall structure of the output.**

   The rest of the output will be divided into sections, one for each
   failure.  Here is what it look like with the
   details taken out so that you can see the big picture more easily:
   

   ```text
   ==================================== test session starts ====================================
   (blah blah here that you can ignore)
   
   convert.py ..FF
   ========================================= FAILURES ==========================================
   _____________________________________ test_fToC_boiling _____________________________________

   ...
   (details about the first test case failure are here)
   ...
   
   _____________________________________ test_cToF_boiling _____________________________________

   ...
   (details about the second test case failure are here)
   ...
   
   ========================= 2 failed, 2 passed in 0.03 seconds =============================
   ```
   
   Note that the last line gives us a nice summary: `2 failed, 2 passed in 0.03 seconds`.   We now know that 
   we need to focus on the two failures.   And the headers tell us which test cases failed, namely `test_fToC_boiling`
   and `test_cToF_boiling`.   So let's focus on those next, by first looking in detail at the first one:
 
3. <b>Focus in on the first test case failure.</b>
 
   Let's focus just on the detailed output for the first test case failure,
   `test_fToC_boiling`.  What does all of the detailed output mean?
   
   In general, its a breakdown of why the assertion turned out to be false, showing every step in the calculation.  Let's break it down one line at a time:

   If we look at this, we can see that amidst all of the clutter is the crucial fact that `fToC(212.0)` returned `180.0` when what we were expecting was `100.0`, with a tolerance of `± 1.0e-04`.
            
# Step 8: Fixing the code

So, if you have failing test cases, the thing to do is fix the code so
that the test cases pass.

To do that you'll need to correct the forumla.

Keep in mind that in Python:

* The `*` symbol is used for multiplication.  In algebra, we can write
  `1.8x` to mean `1.8` multiplied by `x`, however, this does not work
  in Python.  In Python you must write `1.8 * x` if you want to
  multiply the variable `x` by 1.8.

* The `+` and `-` symbols are used for addition and subtraction

* The `/` symbol is used for division, e.g '9/5' means nine
  divided by five.  

Also, the order of operations in Python is that multiplication and
division are done before addition and subtraction. Some examples: 

* If `x` is 5, then `x + 2 * 3` gives us 11, not 21.  The
  multiplication is perfomed before the addition.

* If `x` is 16, then `x - 6 / 2` gives us 13, not 5.  The division is
  performed before the subtraction.

* If you want to force the addition or subtraction to be done first,
  you must use parentheses, e. g. `(x + 2) * 3` or `(x - 6) / 2`

When you replace `return ftemp - 32.0` with the correct formula for
converting a Fahrenheit temperature to Celsius, you should leave out
the comment that says `# TODO: Fix this line of code `.

You'll also want to replace the similar line in the cToF function.

When you have the test cases passing, try running the pytest command again&mdash;remembering that:

* it <b>must be done from the terminal shell</b>, NOT the Python shell.
* the current working directory of that terminal session must be
   the directory/folder where your `convert.py` file is located

```
python3 -m pytest convert.py
```

When you see four passing tests, your output will look like this. Also, the last line will be a pleasant shade of green instead of an angry looking red.

```
169-231-175-204:lab01 photon$ python3 -m pytest convert.py
======================== test session starts =========================
platform darwin -- Python 3.6.2, pytest-3.2.1, py-1.4.34, pluggy-0.4.0
rootdir: /Users/photon/Desktop/MAST_python/lab01, inifile:
collected 4 items                                                     

convert.py ....

====================== 4 passed in 0.01 seconds ======================
169-231-175-204:lab01 photon$ 
```
