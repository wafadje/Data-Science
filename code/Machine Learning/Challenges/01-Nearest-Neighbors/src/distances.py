import math

"""distances.py
Module containing distances utility functions"""



def get_distance(p, q):

	"""
	Function that caluclate the euclidean distance between 2 points p and q
	Parameteres:
	-----------
	p and q : tuples 
	Return:
	-------
	float.
	"""
	px, py = p
	qx, qy = q
	return math.sqrt(((qx-px)**2) + ((qy-py)**2))





def get_distances(p, X): 
	"""
	Function that caluclate the euclidean distance between 2 points p and q
	Parameteres:
	-----------
	X :  is a list of points 
	p : (tuple)
	Return:
	------
	list of distances between p and each point of X (float)
	"""
	dist = []
	for point in X:
		dist.append(get_distance(p, point))
	return dist



def get_k_closest(D, K): 
	"""
	Parameters:
	-----------
	l, K : integer
	return:
	-------
	K : int
	"""
	D = sorted(D)
	indice = []
	for i in range(K):
		indice.append(D[i])
	return indice
