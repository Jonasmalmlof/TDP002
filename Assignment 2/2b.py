#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

def create_shopping_list():
    # skapar listan
    slist = ["Kurslitteratur", "Anteckningsblock", "Penna"]
    return slist

def shopping_list(slist):
    # visar listan
    for length in range(1, len(slist)+1):
        print(length, end="")
        print(". " + slist[length-1])                                 # , = bad + = good
    # print(slist)

def shopping_add(slist):
    # adderar till listan
    print("Vad ska läggas till i listan? ", end="")
    x = input()
    slist.append(x)
    return slist

def shopping_remove(slist):
    # tar bort från listan
    print("Vilken sak ska tas bort från listan? ", end="")
    x = input()
    if x.isdigit():
      x = int(x)
      del slist[x-1]
    else:
      print("not a number.")
      shopping_remove(slist)
    return slist

def shopping_edit(slist):
    print("Vilken sak ska ändras på? ", end="")
    x = input()
    if x.isdigit():
      x = int(x)
      print('Vad ska stå istället för "' + slist[x-1] + '"? ', end="")
      y = input()
      slist[x-1:x] = [y]
    else:
      print("not a number.")
      shopping_edit(slist)

    return slist
    
slist = create_shopping_list()
shopping_list(slist)
shopping_add(slist)
shopping_list(slist)
shopping_remove(slist)
shopping_list(slist)
shopping_edit(slist)
shopping_list(slist)
