#!/usr/bin/python3
""" a function that divides all elements of a matrix """


from typing import Type


def matrix_divided(matrix, div):
	""" Our prototype per task"""

	# the matrix must be list of ints or float, if not raise Error
	if isinstance(matrix, list):
		for row in matrix:
			if not isinstance(row, list):
				raise TypeError("matrix must be a matrix(list of lists) of integers/floats")

			for numb in row:
				if not isinstance(numb, (int, float)):
					raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	else:
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	# the matrix must have the same size of rows or TypeError
	for row in matrix:
		if len(row) == len(matrix[0]):
			continue
		else:
			raise TypeError("Each row of the matrix must have the same size")

	# we can have a div that equals zero, yet must be int or float
	if isinstance(div, (int, float)):
		if div == 0:
			raise ZeroDivisionError("division by zero")
	else:
		raise TypeError("div must be a number")

	# elements of the matrix should be divided by div, rounded to 2 decimal places
	nuevoMatrix = []
	for row in matrix:
		row = [numb /div for numb in row]
		nuevoRow = [round(numb, 2) for num in row]
		nuevoMatrix.append(nuevoRow)
	
	return nuevoMatrix
