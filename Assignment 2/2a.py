#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

def frame(meddelande):
    print()

    print("*"*(len(meddelande)+4))
    print("*", meddelande, "*")
    print("*"*(len(meddelande)+4))

    print("\n")
    return


def triangle(x):
    star = 1
    for line in range(x):
        space = x-line-1
        print(" "*space, end="")
        space -= 1
        print("*"*star, end="")
        star += 2
        print()

    print("\n")
    return


def flag(x):
    for twice in range(2):
        for height in range(4*x):
            print("*"*(11*x), end="")
            print(" "*x, end="")
            print("*"*(11*x))
        print()
    print("\n")
    return

frame("Välkommen till Python")

triangle(6)

flag(2)

