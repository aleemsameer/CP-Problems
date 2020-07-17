# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
	res = 0
	flag = 0
	while flag <=n:
		res+=1
		if(ishappynumber(res)):
			flag += 1
	return res
def ishappynumber(a):
	if a == 7 or a == 1:
		return True
	sum = a
	while sum > 9:
		sum = 0
		while a>0:
			sum += (a%10)**2
			a //= 10
		if sum == 1:
			return True
		a = sum
	return False 
