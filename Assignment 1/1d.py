#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

p=0									                                          		# summation of primes

for n in range(2, 1000): 				                                 	# loops 1000 times.
  for d in range(2, n+1):				                                	# for each number it loops up to itself 
    a=n%d									                                      	# checks to see if there are any decimals
    if a == 0:						                                    		# if there are no decimals
      if n == d:						                                  		# to see if it's actually dividing by itself.
        print('next prime found:', n, '->', p, '+', n, '=', p+n)	# if it has, it's a prime.
        p+=n									                                    # adds the newest discovered prime to the pile
        break								
      else:							                	                        # if it's not dividing by itself, it continues searching.
        break								

print('sum of all primes up to 1000:', p)

