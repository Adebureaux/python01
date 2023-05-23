from vector import Vector

# Column vector of shape (n, 1)
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
print(v1.values)

# Row vector of shape (1, n)
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
print(v2.values)

# Vector initialized with a size
v3 = Vector(3)
print(v3)

# Vector initialized with a range
v4 = Vector((16, 18))
print(v4)

# Vector initialized with a range
v5 = Vector([[9.], [0.]])
print(v5)

try:
	Vector('abc')
except (ValueError, TypeError) as e:
	print(e)

try:
	Vector([1])
except (ValueError, TypeError) as e:
	print(e)

try:
	Vector([[1, 2]])
except (ValueError, TypeError) as e:
	print('1', e)

try:
	Vector([[1], [2]])
except (ValueError, TypeError) as e:
	print(e)