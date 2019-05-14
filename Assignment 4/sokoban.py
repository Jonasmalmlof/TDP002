#! /usr/bin/env Python3
# -*- coding: utf-8 -*-

import sys

def print_there(x, y, text):				
  ## http://stackoverflow.com/questions/7392779/
  ## allows printing on anywhere you want in the terminal window.
  sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y+5, x+20, text))
  sys.stdout.flush()


def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns the character of the key that was pressed (zero on
    KeyboardInterrupt which can happen when a signal gets handled)

	http://stackoverflow.com/questions/983354/how-do-i-make-python-to-wait-for-a-pressed-key

    """
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    try:
        ret = sys.stdin.read(1) # returns a single character
    except KeyboardInterrupt: 
        ret = 0
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return ret




def board(action, level):
  ## create board and return dictionary.
	soko_levels = open("sokoban_levels.txt")
	if action == "start":
		level = {"player": [], "walls": [], "crates":[], "done":[], "wrong":[], "stash": [], "number":1, "start":0, "stop":0}
	if action == "next":
		level["number"] += 1
		level["start"] = level["stop"]		## if we want to move to the next map. reset current map and set the start to the last map's end.
		level["player"] = []
		level["walls"] = []
		level["crates"] = []
		level["done"] = []
		level["stash"] = []
		level["wrong"] = []
	if action == "restart":
		level["stop"] = level["start"]		## if we want to start over on the same map, reset what's in memory and re-read the text-file from last position.
		level["player"] = []
		level["walls"] = []
		level["crates"] = []
		level["done"] = []
		level["stash"] = []
		level["wrong"] = []
	ty = -1									
	last_column=0							
	for line in soko_levels:
		ty += 1											## increment ty to keep track of y-coordinate.
		if level["start"] > ty:							## if start is higher than ty, it means we're not ready to start reading yet. skip to next line.
			continue
		tx  = 0
		for column in line:
			tx += 1												## increment tx to keep track of x-coordinate.
			if column == "#":										
				level["walls"].append([tx,ty-level["stop"]])		
			if column == "@":
				level["player"].append([tx,ty-level["stop"]])
			if column == ".":
				level["stash"].append([tx,ty-level["stop"]])		## find symbols and add x&y-coordinates to level dictionary.
			if column == "o":
				level["crates"].append([tx,ty-level["stop"]])
			if column == "+":
				level["player"].append([tx,ty-level["stop"]])
				level["wrong"].append([tx,ty-level["stop"]])
			if column == "*":
				level["done"].append([tx,ty-level["stop"]])
			if column == "\n" and last_column == "\n":				## two \n in a row = empty line = new map.
				level["stop"] = ty+1								## set end of current level.
				break
			last_column = column
		if level["stop"]== ty+1:
			break
	if level["start"] == level["stop"]:								## if both start and end are the same, it means there are no more maps to conquer.
		level["stop"] = "end of line"
		return level
	return level 

def move(x,y, level):
	one_step = [level["player"][0][0]+x, level["player"][0][1]+y]				## just for clarity and simplicity.. nothing more.
	two_step = [level["player"][0][0]+x*2, level["player"][0][1]+y*2]
	if one_step in level["walls"] or ((one_step in level["crates"] or one_step in level["done"]) and (two_step in level["walls"] or two_step in level["crates"] or two_step in level["done"])):
		return level							## yeah, that's a hell of an if-statement. "if A or ((B or C) and (D or E or F))": takes care of seven scenarios.
	if one_step in level["crates"]:
		if two_step in level["stash"]:
			level["done"].append(two_step)
			level["stash"].remove(two_step)
			level["crates"].remove(one_step)
		else:
			level["crates"].append(two_step)
			level["crates"].remove(one_step)
	if one_step in level["done"]:
		if two_step in level["stash"]:
			level["done"].append(two_step)
			level["done"].remove(one_step)
			level["stash"].remove(two_step)
			level["stash"].append(one_step)
		else:
			level["done"].remove(one_step)
			level["crates"].append(two_step)
	if one_step in level["stash"]:
		level["wrong"].append(one_step)
	if level["player"][0] in level["stash"]:
		level["wrong"].remove(level["player"][0])		
	level["player"] = [one_step]
	return level

def display_board(level):
			## accept current dictionary and print it. return nothing, since nothing is altered.
	for f in level["stash"]:
		print_there(f[0]*2, f[1], ".")
	for f in level["crates"]:
		print_there(f[0]*2, f[1], "o")
	for f in level["done"]:
		print_there(f[0]*2, f[1], "*")
	for f in level["player"]:
		if f in level["wrong"]:
			print_there(f[0]*2, f[1], "+")
			continue
		print_there(f[0]*2, f[1], "@")
	for f in level["walls"]:
		print_there(f[0]*2, f[1], "#")
	print_there(-17,-1,"level:")
	print_there(-10,-1,level["number"])
	print_there(-17,1,"w, a, s, d")
	print_there(-17,3,"(r)estart")
	print_there(-17,4,"(q)uit")
	print_there(-17,5,"(n)ext")
#	 print_there(-17,8,level["start"])
#	 print_there(-17,9,level["stop"])
	return

def init(inp):
			## start board(), and then accept player input.
	while inp != "q":											## keeps asking for input until you hit "Q".
		if inp == "o":											## start from scratch.
			level = board("start", 0)
			display_board(level)
		if inp == "n":											## go to next level.
			if level["stop"] == "end of line":					## unless there is no next level:
				inp = "r"										## then restart current one instead.
				continue
			level = board("next", level)
		if inp == "r":											## restart current map.
			level = board("restart", level)
		if inp == "a":											## a = left, w = up, s = down, d = right.
			move(-1,0, level)
		if inp == "d":
			move(+1,0, level)
		if inp == "w":
			move(0,-1, level)
		if inp == "s":
			move(0,+1, level)
		print(chr(27) + "[2J")				## http://stackoverflow.com/questions/2084508/ clear screen.
		display_board(level)								## print the board/map.
		if level["crates"] == []:								## if there are no crates left on the map: you win!
			if level["stop"] == "end of line":					## if you're on the last map: you win MORE!
				print_there(5,-3,"Congratulations!")
				print_there(0,-2,"you finished all the maps!")
				inp = input("Press Enter to quit:")
				break
			print_there(4,-3,"A Winner Is You!")
			inp = input("Press Enter to continue:")
			level = board("next", level)
			continue
		inp = read_single_keypress()							## doesn't wait for <enter>. function at the very top. not mine, obviously.
#		inp = input()											## if previously mentioned function isn't allowed.
			## input: w, a,s, d for movement.
			## r: restart, q: quit, n: next, o: start all over.
	return

init("o")														## does the thing.
