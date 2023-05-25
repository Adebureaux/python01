from vector import Vector

if __name__ == "__main__":
	def test_should_fail(vec):
		try:
			Vector(vec)
			return False
		except (ValueError, TypeError, NotImplementedError) as e:
			print(e)
		return True

	# Column vector of shape (n, 1)
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	print(v1.shape)
	print(v1.values)

	# Row vector of shape (1, n)
	v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
	print(v2.shape)
	print(v2.values)

	# Column vector init with integer
	print(Vector([[1], [2]]))

	# Row vector init with integer
	print(Vector([[1, 2]]))

	# Vector initialized with a size
	v3 = Vector(2)
	print(v3)
	print(v3.shape)

	# Vector initialized with a range
	v4 = Vector((16, 17))
	print(v4)
	print(v4.shape)

	# Vector initialized with a negative range
	v5 = Vector((-5, 1))
	print(v5)

	# Vector-Vector addition
	print(v3 + v3)

	# Vector-Scalar addition
	print(v3 + 8)

	# Scalar-Vector addition
	print(5 + v3)

	# Vector-Vector substraction
	print(v3 - v3)

	# Vector-Scalar substraction
	print(v3 - 3)

	# Scalar-Vector substraction
	print(5 - v3)

	# Vector-Scalar division
	print(v4 / 1.52)

	# Vector-Scalar multiplication
	print(v4 * 2)

	# Vector-Scalar multiplication
	print(3 * v2)

	if not test_should_fail('abc'):
		print('Failed')

	if not test_should_fail([1]):
		print('Failed')

	if not test_should_fail([['a'], ['b']]):
		print('Failed')

	if not test_should_fail([[1.], [1., 2., 3.], [1.]]):
		print('Failed')

	if not test_should_fail(0):
		print('Failed')

	if not test_should_fail((16, 10)):
		print('Failed')
