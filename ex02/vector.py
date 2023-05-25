class Vector:
	def __init__(self, values):

		# Initialization by size
		if isinstance(values, int):
			if values <= 0:
				raise ValueError("__init__ invalid size: value must be positive.")
			self.values = [[float(i)] for i in range(values)]

		# Initialization by range
		elif isinstance(values, tuple):
			start, end = values
			if start > end:
				raise ValueError("__init__ invalid range: start value must be smaller or equal than end value.")
			self.values = [[float(i)] for i in range(start, end + 1)]

		# Initialization by list of a list of floats or list of lists of single float
		elif isinstance(values, list):
			if all(isinstance(sublist, list) and all(isinstance(val, (int, float)) for val in sublist) and len(sublist) == 1 for sublist in values):
				self.values = [[float(val) for val in sublist] for sublist in values]
			elif all(isinstance(sublist, list) and all(isinstance(val, (int, float)) for val in sublist) and len(sublist) != 1 for sublist in values):
				self.values = [[float(val) for val in sublist] for sublist in values]
			else:
				raise ValueError("__init__ invalid parameter.")

		# Initialization error
		else:
			raise TypeError("__init__ invalid parameter.")

		# Initialization of shape
		self.shape = (len(self.values), 1) if len(self.values) > 1 else (1, len(self.values[0]))

	# Addition operator
	def __add__(self, other):
		if isinstance(other, (int, float)):
			result = [[x + other for x in val] for val in self.values]
			return Vector(result)
		if self.shape != other.shape:
			raise ValueError("__add__ vector shapes do not match.")
		result = [[x + y for x, y in zip(v1, v2)] for v1, v2 in zip(self.values, other.values)]
		return Vector(result)

	def __radd__(self, other):
		return self.__add__(other)

	# Substraction operator
	def __sub__(self, other):
		if isinstance(other, (int, float)):
			result = [[x - other for x in val] for val in self.values]
			return Vector(result)
		if self.shape != other.shape:
			raise ValueError("__sub__ vector shapes do not match.")
		result = [[x - y for x, y in zip(v1, v2)] for v1, v2 in zip(self.values, other.values)]
		return Vector(result)

	def __rsub__(self, other):
		return self.__sub__(other)

	# Division operator
	def __truediv__(self, other):
		if not isinstance(other, (int, float)):
			raise TypeError("__truediv__ only works with scalars that in either an integer or a float.")
		result = [[x / other for x in val] for val in self.values]
		return Vector(result)

	def __rtruediv__(self, other):
		raise NotImplementedError("__rtruediv__ division of a scalar by a Vector is not defined here.")

	# Multiplication operator
	def __mul__(self, other):
		if not isinstance(other, (int, float)):
			raise TypeError("__mul__ only works with scalars that in either an integer or a float.")
		result = [[x * other for x in val] for val in self.values]
		return Vector(result)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __str__(self):
		return str(self.values)

	def __repr__(self):
		return self.__str__()