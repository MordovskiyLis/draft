#!/usr/bin/python3 -u
#
#	vitaliy.gafurov@ya.ru
#	practice from https://play.picoctf.org/practice
#	RSA with CRT fault attack!
#

# First step of the challenge

import string
import hashlib

#PoW
i = 0
vals1 = input("First 5 digits: ") # "".join([random.choice(string.digits) for _ in range(5)])
vals2 = input("Hash 6 hex digits: ")  # "".join([random.choice(string.hexdigits.lower()) for _ in range(6)])
# user_input = input("Enter a string that starts with \"{}\" (no quotes) which creates an md5 hash".format(vals1))


while True:
	user_input = vals1 + str(i)
	user_hash = hashlib.md5(user_input.encode()).hexdigest()

	if user_hash[-6:] == vals2:
		print("Digits : ", user_input)
		print("MD5 HASH : ", user_hash)
		exit()
	i = i + 1
