Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/26/2021
>>> #Problem 1, writing a function area of circle which returns the area of a circle of radius r.
>>> import math #importing math module
>>> 
>>> def area_of_circle(r): #defining our function

	area_of_circle = r * r * math.pi
	return area_of_circle

>>> r = 5
>>> result = area_of_circle
>>> print ("The area of the circle is", result) #printing the final result after giving the value 5 to our radius
The area of the circle is <function area_of_circle at 0x0000022D28B7DDC0>
>>> 