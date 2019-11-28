from math import gcd

def find_inverse(number: int, modulus: int) -> int:
	""" Task example:
		Compute inverse of 7 (number) in mult. group Z*11(modulus)
	"""
	for i in range(1, modulus):
		if (i*number)%modulus == 1:
			return i

def list_elements(modulus: int) -> []:
	""" Task example:
		List all elements in the mult. group Z*15(modulus)
	"""
	result = []
	for i in range(modulus):
		if gcd(i, modulus) == 1:
			result.append(i)
	return result

def find_generators(modulus: int) -> []:
	""" Task example:
		Find all generators of mult. group Z*17(modulus)
	"""
	group = list_elements(modulus)
	generators = []
	for g in group:
		g_group = []
		for k in range(1,len(group)+1):
			g_group.append((g**k)%modulus)
		g_group.sort()
		if g_group == group:
			generators.append(g)
	return generators

def find_logarithm(number: int, base: int, modulus: int) -> []:
	""" Task example:
		Compute log5(8) in mult. group Z*13
		(returns 0 if not found)
	"""
	result = []
	for i in range(1,modulus):
		if (base**i)%modulus == number:
			result.append(i)
	return result


if __name__ == "__main__":
	
	print(find_inverse(7, 11))

	print(list_elements(15))

	print(find_generators(17))

	print(find_logarithm(8, 5, 13))