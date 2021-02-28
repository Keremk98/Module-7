Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/26/2021
>>> #Problem 3. Writing a function to multiply numbers 5,2,7,-1 in a list.
>>> def multiplyList(keremsList): #defining my function
	result = 1
	for x in keremsList:
		result = result * x
	return result

>>> list = [5, 2, 7, -1] #my numbers listed
>>> print(multiplyList(list)) #printing  the results of the multiplication
-70
>>> 