#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

i=1												     # defining the variables used
n=0												
while i < 13: 						  		# while-loop because we don't know how long we'll go
  n+=1											    # add one to counter.
  for i in range(14):			  		# for-loop because we DO know when to stop (13)
    a=(n)%(i+1)									# calculate 
    if a > 0:										# if we get decimals, break off.
      break										



for i in range(14):					  	# once we have a good number, this bit displays it.
  if i > 0:										  # (also displays each division separately)
    print(n, '/', i, '=', n//i)	# btw: 360360 is also divisible by both 14 and 15.

