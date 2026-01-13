#!/usr/bin/python3
print(', '.join("{}{}".format(num, num2)
				for num in range(10) for num2 in range(num + 1, 10)))
