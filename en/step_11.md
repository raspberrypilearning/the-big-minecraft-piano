## Investigating `for` loops

For the next section, you're going to need to use a `for` loop to place multiple keys. You can experiment with `for` loops if you're unsure how they work; to do this click on `File` > `New File` and write some test code in a new blank file.

- You can write a simple `for` loop in your new file. This loop will make sure each value is printed with commas separating the numbers.

	```python
	for i in range(19):
		print(i, end = ',')

	>>> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
	```

- You can see that the first value is `0` and the last is `20`.

	If you wanted to get every third number, then you need to add a step value to the `range()` function. Here, the function provides values from `0` to `20` with a step value of `3`.

	```python
	for i in range(0, 19, 3):
		print(i, end = ',')

	>>> 0,3,6,9,12,15,18,
	```

