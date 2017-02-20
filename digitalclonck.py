#!/usr/bin/python

try:
	import Tkinter
except:
	import tkinter as Tkinter
import time as tm

root = Tkinter.Tk(className=" Digital Clock")
time = Tkinter.Label(root,relief="raised" ,font=("times 40 bold"), bg="black", fg="green", text="Sun Jan 01 00:00:00 2017")
time.pack(ipadx=20,ipady=20)

def timeupdate():
	time['text']=tm.ctime()
	return

while True:
	timeupdate()
	root.update()
	root.update_idletasks()

