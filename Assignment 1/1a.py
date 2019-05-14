#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

n=0									          # defines n.
for i in range(1, 513):				# for-loop with i from 0 to 512.
# print(n, "+", i, "=", n+i)	  # prints how far the code has gotten. (for bug-testing)
 n+=i							            # adds a to n.

print("result:", n)					  # prints the result after the loop is done.
