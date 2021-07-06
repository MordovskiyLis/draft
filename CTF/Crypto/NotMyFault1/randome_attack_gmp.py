#!/usr/bin/python3 -u
#
#	vitaliy.gafurov@ya.ru
#	practice from https://play.picoctf.org/practice
#	RSA with CRT fault attack!
#
# Special thanks for good ideas:
# https://www.johndcook.com/blog/tag/sympy/
# https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-4/

# I tryed Fermat’s factoring trick
# But it takes to long with a limit of 15 minutes to solve the problem, even for 20 bits p and q

# Another one vector that I tryed for this challenge, but it does not work in this case
# Anyway, this one to fast to solve some qudratic problems
#
# I'm surprised, good math explanation here:
# https://en.wikipedia.org/wiki/Wiener%27s_attack
# and perfect math example here:
# https://en.wikipedia.org/wiki/Continued_fraction

# and, finally...

import random
import string
import hashlib
import time
# pip install pycryptodome
# picoCTF{1_c4n *** 4774ck!!!}

from Crypto.Util.number import inverse, getPrime, bytes_to_long, GCD
from sympy.ntheory.modular import solve_congruence

def gcd_rnd(n, e, m): 					# m - random number
	BITS = 20
	a = 1
	b = 1 << BITS
	strim = 0

	# Pay no attention, it's out of boredom after 2 days of reflection
	if strim == 1:
		# a = 1
		b = 262143
	if strim == 2:
		a = 262144
		b = 524287
	if strim == 3:
		a = 524288
		b = 786438
	if strim == 4:
		a = 786438
		# b = 1 << BITS

	for dp in range(a, b):
		if dp==1:
			start = time.time()
	# while True:
	# 	dp = random.randint(a, b)	# 1, 1 << BITS
		f = GCD(m-pow(m, e*dp, n), n)
		if f > 1:
			stop = time.time()
			print("done! ---> ", dp)
			p = f
			q = n // p
			print("summ: ", p + q )
			etr = (stop-start)/60
			print("Time: "+str(etr)+" minutes")
			return
		if dp==1:
			stop = time.time()
			etr = (stop-start)*(1<<BITS)/60
			print("Max time remaining: "+str(etr)+" minutes")
	print("Done. No key.")

#PoW

# p, q = gen_key()
# n = p * q
# print("Public Modulus : ", n)
# e = get_clue(p, q, 20)
# "".join([random.choice(string.digits) for _ in range(5)])
# "".join([random.choice(string.hexdigits.lower()) for _ in range(6)])

# n = int(input("Input Modulus : "))
# e = int(input("Input Clue: "))
n = 77866383786349131818678247976908655001041761532278205497111356944088742577269126581642415718144899458780160278125514796747546195716362301452154599043034368779022045170369901653290099436555750843874550200883048603423912050619558065093339890336868985014698107327638395504850251686606928986459014825557157390513
e = 70805392202463306101305670146244630529107801477539151889351416074773064299980343819329996783952924859410424304517013823005473195505891380417655090646193525917759260226295704341480535692750940198539728842788505988065605924797057784451877652085644233956632136016416593694133417564097119402655324729226618116255

# Fro TESTS:
m = 2
# m = random.randint(1, 1 << 20)
print("m: ", m)

# leaky_p(n, e ,m)
gcd_rnd(n, e, m)

# get_flag(p, q)