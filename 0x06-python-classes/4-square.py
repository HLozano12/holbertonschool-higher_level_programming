#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
	"""Create Square Class"""

	def __init__(self, size=0):
		"""initialization of square instance"""
		self.__size = size

	@property
	def size(self):
		"""The Getter of size"""
		return self.__size

	@size.setter
	def size(self, size):
		"""setter for size"""
		if not instance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	def area(self):
		"""return area"""
		return (self.__size **2)
			