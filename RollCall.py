from tkinter import *
import tkinter.font as tkFont
import time
import random


class App():
	def __init__(self, root, names):
		self.root = root
		self.root.geometry('600x400')
		font1 = tkFont.Font(size = 60, weight=tkFont.BOLD)
		font = tkFont.Font(size = 32)
		Label(app, text="",font=font).pack()
		Label(app, text="",font=font).pack()
		self.lname = Label(app, text="下一个就是你了，好好听课",font=font1)
		self.lname.pack()
		self.blank = Label(app, text="",font=font)
		self.blank.pack()
		self.rollBtn = Button(app, text="点名",font=font,command=self.Roll)
		self.rollBtn.pack()
		self.rightBtn = Button(app, text="答对啦",font=font,command=self.AnsRight)
		self.wrongBtn = Button(app, text="继续努力",font=font,command=self.AnsWrong)
		self.rollTime = 0
		self.names = names

	def ChangeName(self):
		self.rollTime = self.rollTime + 50
		if self.rollTime > 1000:
			self.RollEnd()
			return
		self.lname["text"] = self.names[random.randint(0,len(self.names)-1)]
		self.root.after(50, self.ChangeName)

	def RollEnd(self):
		self.rollTime = 0
		self.lname["text"] = self.names[random.randint(0,len(self.names)-1)]
		self.rollBtn.pack_forget()
		self.rightBtn.pack(side=LEFT, padx=50)
		self.wrongBtn.pack(side=RIGHT, padx=50)

	def Roll(self):
		self.ChangeName()
		
	def AnsRight(self):
		self.lname["text"] = "下一个就是你了，好好听课"
		self.rightBtn.pack_forget()
		self.wrongBtn.pack_forget()
		self.rollBtn.pack()
	def AnsWrong(self):
		self.names.append(self.lname["text"])
		self.lname["text"] = "下一个就是你了，好好听课"
		self.rightBtn.pack_forget()
		self.wrongBtn.pack_forget()
		self.rollBtn.pack()
		

if __name__ == '__main__':
	app = Tk()
	names = []
	with open("names.txt", 'r') as f:
		for line in f.readlines():
			names.append(line.strip())

	App(app, names)
	app.mainloop()
	with open("names.txt", 'w') as f:
		writeStr = ""
		for line in names:
			writeStr = writeStr + line + '\n'
		f.write(writeStr)
	

