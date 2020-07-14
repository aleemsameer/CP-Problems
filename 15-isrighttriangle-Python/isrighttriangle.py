# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	x = distance(x1,y1,x2,y2)
	y = distance(x2,y2,x3,x3)
	z = distance(x1,y1,x3,y3)

	sides = [X,Y,Z]
	sides.sort()
	return math.isclose(sides[2], sides[0] + sides[1])
def distance(x1,y1,x2,y2):
	return(math.pow(x2 - x1),2) + math.pow((y2 - y1),2)