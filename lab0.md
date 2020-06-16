# Lab 0: Warmup--experiencing floating point inaccuracy

You are expected to follow each step and understand why they turn out this way

If you are not already at the Python prompt, bring up a terminal window, and just type `python3`.  This should give you the Python Shell Prompt (`>>>`) where you can type in some expressions and see the resulting values. You could also just open the Python IDLE, which does the same thing.

Type in the `import math`, followed by `math.sqrt(2)`.  It should look like this:

```
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> 
```

The value we get back is the square root of 2, which is an irrational number; its decimal representation goes on forever.  Unfortunately, real world computing devices typically store numbers with a finite number of decimal places. So, the representation we see for the square root of two `1.4142135623730951` is in fact an approximation.


We can see this if we multiply `math.sqrt(2)` by itself.  Try it:

```
>>> math.sqrt(2) * math.sqrt(2)
2.0000000000000004
>>> 
```

See that pesky `4` digit in the ten quadrillionths place?   My goodness, we are really, really close to 2.0, but if we ask whether the values are equal, Python says no:

```
>>> math.sqrt(2) * math.sqrt(2) == 2.0
False
```

In fact, Python is very clear about the difference between `2.0` and `math.sqrt(2) * math.sqrt(2)`, and can even tell us 
how big that difference is.  The `4` digit is only the tip of the very, very, very small iceberg:

```
>>> math.sqrt(2) * math.sqrt(2)- 2.0
4.440892098500626e-16
>>> 
```
Here the `e-16` means 10<sup>-16</sup>, which is a teeny tiny number. This fact is going to be annoying to us many times.   One consequence is that <strong>when we test software involving floating point numbers, we must allow for some inaccuracy</strong>.   This "allowable inaccuracy" is sometimes called the <em>tolerance</em>, and it might be a small value such as `0.001` (1x10<sup>-3</sup>, or `0.000001` (1x10<sup>-6</sup>).

In Python, we can write `0.001` as `1e-03`, and `0.000001` as `1e-06`.  (The lowercase `e` is the way that Python represents scientific notation.)

You can see that Python, by default, formats numbers in this notation once the fifth decimal place is reached:

```
>>> 0.01
0.01
>>> 0.0001
0.0001
>>> 0.00001
1e-05
>>> 0.000001
1e-06
>>>
```


That's it for this week's lab. We will work much harder next time. But for now, let's just start gently.
