Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/26/2021
>>> #Problem 2. Writing a Python function to check whether a number is in a given range.
>>> def test_range(x):
	if x in range(1,10):
		print( "Number %s is in the range"%str(x))
	else :
		print("The number is outside the given range.")

		
>>> test_range(5)
Number 5 is in the range
>>> test_range(11)
The number is outside the given range.
>>> #with the if statement, I told the program to determine whether or not the tested number is in the range. If not in the range, the else statement prints "the number is outside the given range."