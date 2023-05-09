def is_prime(num):
	i = 2
	a = []
	while i < num:
		if num % i == 0:
			a.append(i)
		i+=1
	return len(a) == 0

def are_relatively_prime(num1,num2):
	if num2 % num1 == 0:
		return False
	else: 
		pass
	b = []
	nums = [num1,num2]
	for x in  nums:
		a = []
		i = 2
		while i < x:
			if x % i == 0:
				a.append(i)
			i+=1
		else:
			b.append(a)
	return len(list(set(b[0]) & set(b[1]))) == 0

def primes(num):
	a = []
	if num >= 0:
		i = 2
		while i <= num:
			if is_prime(i):
				a.append(i)
			i+=1
	return a

def prime_decomposition(num):
	a = []
	i = 0
	while True:
		nums = primes(num)[::-1]
		for i in nums:
			if num % i == 0:
				a.append(i)
				num = num//i
				break
		if not primes(num):
			break
	return a

def filterOfPrimeDecomposition(lOfI,min):
	a = []
	for i in lOfI:
		if len(prime_decomposition(i)) >= min:
			a.append(i)
	return a

if __name__ == '__main__':
	pass

	

