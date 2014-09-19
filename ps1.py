# Author: Douglas Skrypa
# Date: 2014.09.16
import math

def inner_product(L1,L2,domain):
	'''
	Inner product between two vectors' elements that are in the given domain,
	where vectors are represented as alphabetically sorted (word,freq) pairs.

	Example: inner_product([["and",3],["of",2],["the",5]],
							[["and",4],["in",1],["of",1],["this",2]],
							["and","two"]) = 12.0 
	'''
	sum = 0.0
	i = 0
	j = 0
	while i<len(L1) and j<len(L2):
		# if L1[i][0] is in the domain,
		if L1[i][0] in domain:
			# then find that word in L2
			while (L2[j][0] != L1[i][0]) and j<len(L2):
				j += 1
			# and add the product of their frequencies to the sum
			sum += L1[i][1] * L2[j][1]
			i += 1
			j += 1
		else:
			i += 1
	return sum
#/inner_product

def vector_angle(L1,L2):
	'''
	The input is a list of (word,freq) pairs, sorted alphabetically.
	Return the angle between these two vectors.
	'''
	s1 = set()
	s2 = set()
	for p in L1:
		s1.add(p[0])
	for p in L2:
		s2.add(p[0])
	domain = s1.intersection(s2)
		
	numerator = inner_product(L1,L2,domain)
	denominator = math.sqrt(inner_product(L1,L1,domain)*inner_product(L2,L2,domain))
	return math.acos(numerator/denominator)
#/vector_angle

def inner_productA(L1,L2,domain):
	sum = 0.0
	i = 0
	j = 0
	while i<len(L1) and j<len(L2):
		# if L1[i][0] is in the domain,
		if L1[i][0] in domain:
			# then find that word in L2
			while (L2[j][0] != L1[i][0]) and j<len(L2):
				j += 1
			# and add the product of their frequencies to the sum
			sum += L1[i][1] * L2[j][1]
			i += 1
			j += 1
		else:
			i += 1
	return sum
#/inner_product

def inner_productB(L1,L2,domain):
	sum = 0.0
	i = 0
	j = 0
	while i<len(L1) and j<len(L2):	
		# L1[i:] and L2[j:] yet to be processed
		if L1[i][0] == L2[j][0]:
			# both vectors have this word
			if L1[i][0] in domain:
				sum += L1[i][1] * L2[j][1]
			i += 1
			j += 1
		elif L1[i][0] < L2[j][0]:
			# word L1[i][0] is in L1 but not L2
			i += 1
		else:
			# word L2[j][0] is in L2 but not L1
			j += 1
	return sum
#/inner_product
