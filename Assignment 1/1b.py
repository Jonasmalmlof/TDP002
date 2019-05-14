#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

n=1										        # defines n.
for i in range(1, 513):			  # for-loop with i from 0 to 512.
# print(n, '*', i, '=', i*n)	  # prints how far the code has gotten. (for bug-testing)
 n=i*n							        	# multiplies n by a.

m = len(str(n))
print("result:", m, n)				# prints the result after the loop is done.

