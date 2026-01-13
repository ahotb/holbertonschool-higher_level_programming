#!/usr/bin/python3
def uppercase(str):
	for ch in str:
		if 97 <= ord(ch) <= 122:  
			print(chr(ord(ch) - 32), end = "")
		else:
			print(ch, end = "")
     
	print()
