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

	# Transpose vector shape
	v3 = v2.T()
	print(v3)
	print(v3.shape)

	# Dot product
	print(Vector([[1., 3.]]).dot(Vector([[2., 4.]])))
	print(Vector([[1., 2., 3.]]).dot(Vector([[4., -5., 6.]])))
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
	print(v1.dot(v2))
	v3 = Vector([[1.0, 3.0]])
	v4 = Vector([[2.0, 4.0]])
	print(v3.dot(v4))

	# Transpose vector shape
	v4 = v3.T()
	print(v4)
	print(v4.shape)

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
	print(v1 + Vector([[1], [5], [3], [8]]))

	# Vector-Vector substraction
	print(v3 - v3)

	v1 = Vector([[1.985], [8.5], [99]])
	v2 = Vector([[6.8], [9.9], [4.4]])

	# Vector-Scalar division
	print(v4 / 1.52)

	# Vector-Vector division
	print(v1 / v2)

	# Vector-Vector multiplication
	print(v1 * v2)

	# Vector-Scalar multiplication
	print(v4 * 2)

	# Scalar-Vector multiplication
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

	try:
		v1 + [1, 5, 3]
	except TypeError as e:
		print(e)

	try:
		v1 + [[1], [5], [3], [8]]
	except TypeError as e:
		print(e)

	try:
		v3 + v2
	except ValueError as e:
		print(e)

	try:
		v3 * v2
	except ValueError as e:
		print(e)

	try:
		v3 / 0
	except ZeroDivisionError as e:
		print(e)

	try:
		1 / v3
	except NotImplementedError as e:
		print(e)
	
	try:
		v1 = Vector([[1., 2., 3.]])
		v2 = Vector([[1., 0., 1.]])
		v1 / v2
	except ZeroDivisionError as e:
		print(e)

	try:
		Vector([[0], [1]]).dot([[0]])
	except TypeError as e:
		print(e)

	try:
		Vector([[0], [1]]).dot(Vector([[0]]))
	except ValueError as e:
		print(e)



