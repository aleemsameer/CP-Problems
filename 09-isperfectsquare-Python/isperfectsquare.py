# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	if type(n) == str:
		if not n.isdigit():
			return False
		n = int(n)
	if n< 0:
		return False
	elif n % 1 == 0:
		return False
	m = math.sqrt(n)
	if n == math.pow(m,2):
		return True
