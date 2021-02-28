Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/26/2021
>>> #Problem 4. Writing a function that takes a list of numbers and returns a new list with unique elements of the first list.
>>> def unique_list(numbers): #defining our function
	unique = []
	for item in numbers :
		if item not in unique:
			unique.append(item) #using the append function
	return unique

>>> print(unique_list([1, 3, 3, 3, 6, 2, 3, 5])) #printing the results
[1, 3, 6, 2, 5]
>>> 