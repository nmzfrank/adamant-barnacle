# -*- coding: utf-8 -*-
import Ran
import Tkinter as Tk
import tkMessageBox
import tkFileDialog

def reserved():
	tkMessageBox.showinfo(message='reserved...')

def decode(rstr,txtbox,g_setting,workingState):
	rg = Ran.randomGenerator(g_setting['randomSeed'],g_setting['randomStart'])
	ciphertext = rstr[:-1]
	try:
		d = Ran.decode(ciphertext,rg)
		plaintext = d.transform()
		txtbox.delete(1.0,Tk.END)
		txtbox.insert(1.0,plaintext)
		workingState[0].set('d')
	except Ran.rangeException:
		tkMessageBox.showinfo(message=u"输入不能为空！")

def encode(rstr,txtbox,g_setting,workingState):
	rg = Ran.randomGenerator(g_setting['randomSeed'],g_setting['randomStart'])
	plaintext = rstr[:-1]
	try:
		e = Ran.encode(plaintext,rg)
		ciphertext = e.transform()
		txtbox.delete(1.0,Tk.END)
		txtbox.insert(1.0,ciphertext)
		workingState[0].set('e')
	except Ran.rangeException:
		tkMessageBox.showinfo(message=u"输入不能为空！")

def configSet(g_setting,txt1,txt2,top):
	s1 = txt1.get()
	s2 = txt2.get()
	if(len(s1) > 0 and len(s2) > 0):
		g_setting['randomSeed'] = float(s1)
		g_setting['randomStart'] = int(s2)
		top.destroy()


def loadFile(win, str1, str2, workingState):
	 filename = tkFileDialog.askopenfilename(initialdir = 'D:')
	 if(filename):
	 	fp = open(filename)
	 	if(workingState[0].get() == 'e'):
	 		str1.insert(1.0, fp.read()) 
	 	else:
	 		str2.insert(1.0, fp.read())


def saveFile(win, str1, str2, workingState):
	fp = tkFileDialog.asksaveasfile(initialdir = 'D:')
	if(fp):
		if(workingState[0].get() == 'e'):
			fp.write(str2.get(1.0, Tk.END)[:-1])
		else:
			fp.write(str1.get(1.0, Tk.END)[:-1])
		fp.close()


def customSetting(win,g_setting):
	top = Tk.Toplevel(win)
	top.title("settings...")
	top.iconbitmap("favicon.ico")
	prompt1 = Tk.Label(top,text="randomSeed: ")
	txt1 = Tk.Entry(top)
	txt1.insert(0,str(g_setting['randomSeed']))
	prompt2 = Tk.Label(top,text="randomStart: ")
	txt2 = Tk.Entry(top)
	txt2.insert(0,str(g_setting['randomStart']))
	btn = Tk.Button(top,text="OK",command=lambda: configSet(g_setting,txt1,txt2,top))

	prompt1.grid(row=0,column=0)
	txt1.grid(row=0,column=1)
	prompt2.grid(row=1,column=0)
	txt2.grid(row=1,column=1)
	btn.grid(row=2,column=0,columnspan=2)





def main():
	g_setting = {'randomSeed':0.8,'randomStart':1000}
	workingState = []
	win = Tk.Tk()
	win.title('codeShell')
	win.geometry('600x320')
	win.iconbitmap('favicon.ico')

	inputframe = Tk.Frame(win)
	outputframe = Tk.Frame(win)
	stateframe = Tk.Frame(win)
	
	scroll1 = Tk.Scrollbar(inputframe, orient=Tk.VERTICAL)
	str1 = Tk.Text(inputframe, height=5 , yscrollcommand = scroll1.set)
	scroll1.config(command=str1.yview)

	scroll2 = Tk.Scrollbar(outputframe, orient=Tk.VERTICAL)
	str2 = Tk.Text(outputframe, height=5, yscrollcommand=scroll2.set)
	scroll2.config(command=str2.yview)

	btn1 = Tk.Button(win,text="||\n\\/",command= lambda: encode(str1.get(1.0, Tk.END),str2,g_setting,workingState))
	btn2 = Tk.Button(win,text="/\\\n||",command= lambda: decode(str2.get(1.0, Tk.END),str1,g_setting,workingState))

	state = Tk.StringVar()
	state.set('e')
	label0 = Tk.Label(stateframe,text="current state:")
	label1 = Tk.Label(stateframe, textvariable=state)
	workingState.append(state)
	
	inputframe.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
	scroll1.pack(side=Tk.RIGHT,fill=Tk.Y)
	str1.pack(side=Tk.LEFT)
	btn1.grid(row=1,column=0,pady=10)
	btn2.grid(row=1,column=1,pady=10)
	outputframe.grid(row=2,column=0,columnspan=2,pady=10)
	scroll2.pack(side=Tk.RIGHT,fill=Tk.Y)
	str2.pack(side=Tk.LEFT)
	stateframe.grid(row=3,column=0,columnspan=2,sticky=Tk.S)
	label0.grid(row=0,column=0)
	label1.grid(row=0,column=1)



	menubar = Tk.Menu(win)

	filemenu = Tk.Menu(menubar,tearoff=0)
	filemenu.add_command(label="load from files...", command=lambda: loadFile(win, str1, str2, workingState))
	filemenu.add_command(label="save to files...", command=lambda: saveFile(win, str1, str2, workingState))
	menubar.add_cascade(label="file",menu=filemenu)

	settingmenu = Tk.Menu(menubar,tearoff=0)
	settingmenu.add_command(label="custom settings...",command= lambda: customSetting(win,g_setting))
	menubar.add_cascade(label="setting",menu=settingmenu)

	generatormenu = Tk.Menu(menubar,tearoff=0)
	generatormenu.add_command(label="square", command=lambda: reserved())
	generatormenu.add_command(label="moore code", command=lambda: reserved())
	menubar.add_cascade(label="generator",menu=generatormenu)

	win.config(menu=menubar)
	Tk.mainloop()




if __name__ == '__main__':
	main()

