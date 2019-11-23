import math 

class Circle():
	"""
	Write a class Circle :
    Parameters:
    -----------
    coordinates of its center x , y (0,0): int
    radius R = 1: int. 
    position()
    Return :
    --------
    area() 
    Return :
    --------
    
    circumference()
    Return :
    --------
    
    is_in_circle() 
    Return :
    --------
    bool
	"""
	def __init__(self, x = 0, y = 0, radius = 1):
		self.x = x
		self.y = y
		self.radius = radius

	def position(x, y):
		return x, y


	def area(self, radius):
		return math.pi * self.radius * self.radius


	def circumference(self, radius):
		return 2*math.pi* self.radius

	def is_in_circle(self, x , y):
		if x + y <= R:
			return true
		else :
		    return false
