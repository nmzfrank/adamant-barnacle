# -*- coding: utf-8 -*-
import Encode
import Tkinter as Tk
import tkMessageBox
import tkFileDialog

def encode(rstr,txtbox,g_setting):
	rg = Encode.randomGenerator(g_setting['randomSeed'],g_setting['randomStart'])
	plaintext = rstr[:-1];
	try:
		e = Encode.encode(plaintext,rg)
		ciphertext = e.transform()
		txtbox.delete(1.0,Tk.END)
		txtbox.insert(1.0,ciphertext)
	except Encode.rangeException:
		tkMessageBox.showinfo(message=u"输入不能为空！")

def configSet(g_setting,txt1,txt2,top):
	s1 = txt1.get()
	s2 = txt2.get()
	if(len(s1) > 0 and len(s2) > 0):
		g_setting['randomSeed'] = float(s1)
		g_setting['randomStart'] = int(s2)
		top.destroy()


def loadFile(win,str1):
	 filename = tkFileDialog.askopenfilename(initialdir = 'D:')
	 if(filename):
	 	fp = open(filename)
	 	str1.insert(1.0, fp.read()) 


def saveFile(win, str2):
	fp = tkFileDialog.asksaveasfile(initialdir = 'D:')
	if(fp):
		fp.write(str2.get(1.0, Tk.END)[:-1])
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
	win = Tk.Tk()
	win.title('codeShell')
	win.geometry('600x400')
	win.iconbitmap('favicon.ico')

	inputframe = Tk.Frame(win)
	outputframe = Tk.Frame(win)
	
	scroll1 = Tk.Scrollbar(inputframe, orient=Tk.VERTICAL)
	str1 = Tk.Text(inputframe, height=5 , yscrollcommand = scroll1.set)
	scroll1.config(command=str1.yview)

	scroll2 = Tk.Scrollbar(outputframe, orient=Tk.VERTICAL)
	str2 = Tk.Text(outputframe, height=5, yscrollcommand=scroll2.set)
	scroll2.config(command=str2.yview)

	btn = Tk.Button(win,text="||\n\\/",command= lambda: encode(str1.get(1.0, Tk.END),str2,g_setting))
	
	inputframe.pack()
	scroll1.pack(side=Tk.RIGHT,fill=Tk.Y)
	str1.pack(side=Tk.LEFT)
	btn.pack()
	outputframe.pack()
	scroll2.pack(side=Tk.RIGHT,fill=Tk.Y)
	str2.pack(side=Tk.LEFT)


	menubar = Tk.Menu(win)

	filemenu = Tk.Menu(menubar,tearoff=0)
	filemenu.add_command(label="load from files...", command=lambda: loadFile(win, str1))
	filemenu.add_command(label="save to files...", command=lambda: saveFile(win, str2))
	menubar.add_cascade(label="file",menu=filemenu)

	settingmenu = Tk.Menu(menubar,tearoff=0)
	settingmenu.add_command(label="custom settings...",command= lambda: customSetting(win,g_setting))
	menubar.add_cascade(label="setting",menu=settingmenu)


	win.config(menu=menubar)
	Tk.mainloop()

