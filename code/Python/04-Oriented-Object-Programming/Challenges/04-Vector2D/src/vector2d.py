"""
2d-vectors are described by a pair of real numbers ${(a,b)}$. There are mathematical rules for operations on vectors:
${(a,b)+(c,d) = (a+c, b+d)}$
${(a,b)−(c,d) = (a−c, b−d)}$
${{(a,b)}.{(c,d)} = ac + bd}$
${||(a,b)||= \sqrt{{(a,b)}.{(a,b)}}}$
Moreover, two vectors ${(a,b)}$ and ${(c,d)}$ are equal if ${a=c}$ and ${b=d}$.
Build a class Vector2D where the above mathematical operations are implemented by special methods. 
The class must contain two data attributes x and y, one for each component of the vector. 
It must include special methods for addition, subtraction, the scalar product (multiplication), 
the absolute value (length), comparison of two vectors (== and !=), as well as a method for printing 
out a vector and the number of dimensions (in that case, it is always 2).
"""

class Vector2D():
	def __init__(self, x, y):

		if x == 0 and y == 0:
			self.values = (0,0)
		else:
			self.values = (x,y)


	def __add__(self, other):
		added = tuple(a + b for a, b in zip(self.values, other.values))
		return Vector2D(*added)
		

	def __sub__(self, other):
		sub = tuple(a - b for a, b in zip(self.values, other.values))
		return Vector2D(*sub)

	def __mul__(self, other):
		mul = tuple(a * b for a, b in zip(self.values, other.values))
		return Vector2D(*mul)

	def __abs__(self):
		pass

	def __ne__(self, other):
		pass

v1 = Vector2D(1, 2)
v2 = Vector2D(10, 13)
v3 = Vector2D.__sub__(v1, v2)
v4 = Vector2D.__mul__(v1, v2)
print(v4.values)
