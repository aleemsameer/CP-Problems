# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	num = str(n).split(".")
	x = int(num[0])
	y = int(num[1])
	if x % 2 == 1:
		return x
	elif y%10 == 0:
		return x - 1
	else:
		return x+1


