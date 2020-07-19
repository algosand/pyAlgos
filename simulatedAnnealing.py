"""
Implementation of the simulated annealing algorithm
Best for when many local minima exist and want to find global minima.
Gradient descent gets stuck in local minima

Using simulated annealing to find the best location for a public service center with respect to some array of 
locations.  In this case our cost function is the distance function which is also convex so that means
we have only one local and global minimum and they are equivalent. 
"""
import math
def euclideanDist(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def sumED(p, points):
	return sum(euclideanDist(p, q) for q in points)

def arithmeticMean(points):
	n = len(points)
	xm, ym = (sum(x for x, _ in points) / n, sum(y for _, y in points) / n)
	return xm , ym

def simulatedAnnealing(arr):
	dirs = [(-1,0), (1,0), (0,-1), (0,1)]
	INF = float('inf')
	n = len(arr)
	cx, cy = arithmeticMean(arr)
	step, limit = 10, 1e-6
	minDist = sumED([cx, cy], arr)
	while step > limit:
		improved = False
		for xd, yd in dirs:
			nx, ny = cx + step*xd, cy + step*yd
			ndist = sumED([nx, ny], arr)
			if ndist < minDist:
				improved = True
				cx, cy = nx, ny
				minDist = ndist
		if not improved:
			step /= 2
	return minDist



if __name__ == '__main__':
	# ans = 32.94036
	arr = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
	print(simulatedAnnealing(arr))
	# ans = 2.73205
	arr = [[1,1],[0,0],[2,0]]
	print(simulatedAnnealing(arr))
	# ans = 2.82843
	arr = [[1,1],[3,3]]
	print(simulatedAnnealing(arr))
	# ans = 4.00000
	arr = [[0,1],[1,0],[1,2],[2,1]]
	print(simulatedAnnealing(arr))

"""
Research into how to prove that the distance function is convex.  
- If distance function is convex -> 1 global and local minimum
- sum of convex functions is convex
- to prove a single variable function is convex from first principles
- f(lambda*x + (1-lambda)*y) <= lambda*f(x) + (1-lambda)*f(y)
- This would seem to indicate that a convex or concave function is nonlinear by definition
- It contradicts the definition of linearity
"""