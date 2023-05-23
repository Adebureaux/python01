class Vector:
	def __init__(self, values):

		# Initialization by size
		if isinstance(values, int):
			self.values = [[float(i)] for i in range(values)]

		# Initialization by range
		elif isinstance(values, tuple):
			start, end = values
			if start > end:
				raise ValueError("__init__ tuple invalid range: start value must be smaller than end value.")
			self.values = [[float(i)] for i in range(start, end + 1)]

		# Initialization by list of a list of floats or list of lists of single float
		elif isinstance(values, list):
			if all(isinstance(sublist, list) and len(sublist) == 1 for sublist in values):
				self.values = [[float(val) for val in sublist] for sublist in values]
			elif all(isinstance(sublist, list) and all(isinstance(val, float) for val in sublist) for sublist in values):
				self.values = values
			else:
				raise ValueError("__init__ invalid parameter")

		# Initialization error
		if self.values:
			raise ValueError("__init__ invalid parameter")

		self.shape = (len(self.values), 1) if len(self.values) > 1 else (1, len(self.values[0]))

	def __str__(self):
		return str(f'Vector({self.values})')

	