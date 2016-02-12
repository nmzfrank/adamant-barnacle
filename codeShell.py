import Encode
import Tkinter as Tk
import tkMessageBox


def encode(rstr,txtbox):
	rg = Encode.randomGenerator(0.724,1000)
	plaintext = rstr;
	try:
		e = Encode.encode(plaintext,rg)
		ciphertext = e.transform()
		txtbox.delete(0,Tk.END)
		txtbox.insert(0,ciphertext)
	except Encode.rangeException:
		tkMessageBox.showinfo(message="empty entry!")


def customSetting(win,g_setting):
	print 1
	top = Tk.Toplevel(win)
	top.title("settings...")


def main():
	g_setting = []
	win = Tk.Tk()
	win.title('codeShell')
	win.geometry('800x200')

	menubar = Tk.Menu(win)
	settingmenu = Tk.Menu(menubar,tearoff=0)
	settingmenu.add_command(label="custom settings...",command= lambda: customSetting(win,g_setting))

	menubar.add_cascade(label="setting",menu=settingmenu,)

	str1 = Tk.Entry(win,width= 50)
	str2 = Tk.Entry(win)
	btn = Tk.Button(win,text="||\n\\/",command= lambda: encode(str1.get(),str2))
	
	str1.pack()
	btn.pack()
	str2.pack()
	
	win.config(menu=menubar)
	Tk.mainloop()


main()