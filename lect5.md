**Use of for loops**

We can also use them to go through a string one letter (i.e. character) at a time:

```python
myString = "Hello!"
for ch in myString:
	print(ch)
```

**Variations on the print() function**

By default, print( ) issues a ‘newline’ character at the end
– That’s why successive print( )s are done on separate lines

You can optionally do this differently with the end= operator inside of print( ). 

```python
for n in range(0, 3):
	print(n)

for n in range(0, 3):
	print(n, end=" ")
	
for n in range(0, 3):
	print(n, end="*")
```

**Ciphers**

String manipulation lends itself well to problems of coding/decoding private or secret messages

Examples:
Make every letter the letter after it: 'abc' becomes 'bcd', and 'Hello' becomes 'Ifmmp'

Mirrored alphabet: 'abcd' becomes 'zyxw', 'bye' becomes 'ybv'

```python
def encrypt(message): 	# message is a string type
	result = '' 			# start with an empty result
	
	for c in message: 	# go thru every letter in message
		# let’s apply the “mirror” formula:
		nc = ord(c)
		nr = ord('a') + ord('z') - nc
		# then accumulate the encoded chars, one at a time
		result = result + chr(nr)
		
	# Now we’re done with the for-loop, so let’s return when we got:
	return result
```

Example run:

```
>>> encrypt("abcdefghijklmnopqrstuvwxyz")
‘zyxwvutsrqponmlkjihgfedcba’
```

Note that the same function decrypts this as well!

```
>>> encrypt('zyxwvutsrqponmlkjihgfedcba')
'abcdefghijklmnopqrstuvwxyz'
```
Because this is symmetric. You mirror it twice, you get the original.

**Asking for input from the user**

```python
number = ("Give me a number:")
```