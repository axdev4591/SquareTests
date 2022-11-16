class Square:
	def __init__(self, side):
		""" creates a square having the given side
		"""
		self.side = side

	def area(self):
		""" returns area of the square
		"""
		return self.side**2

	def perimeter(self):
		""" returns perimeter of the square
		"""
		return 4 * self.side

	def __repr__(self):
		""" declares how a Square object should be printed
		"""
		s = 'Square with side = ' + str(self.side) + '\n' + \
		'Area = ' + str(self.area()) + '\n' + \
		'Perimeter = ' + str(self.perimeter())
		return s




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
