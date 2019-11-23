"""
A program that generates Pascal's triangle both iteratively and recursively
"""

# TODO: ìterative_pascal_triangle()`
def iterative_pascal_triangle(n, k):
	matrix = [[0 for x in range(k+1)] for x in range(n+1)]
	
	for i in range(n+1): 
		for j in range(min(i, k)+1): 
			if j == 0 or j == i:
				matrix[i][j] = 1
			else :
				matrix[i][j]  = matrix[i -1 ][j - 1] + matrix[i - 1][j] 

	return matrix[n][k]

print(iterative_pascal_triangle(5, 2))


# TODO: `recursive_pascal_triangle()`
def recursive_pascal_triangle(n, k):
	matrix = [[0 for x in range(k+1)] for x in range(n+1)]
	
	if k == 0 or k == n:
		return 1
	else :
		return  recursive_pascal_triangle(n-1, k - 1) + recursive_pascal_triangle(n-1, k )

print(recursive_pascal_triangle(5, 2))
