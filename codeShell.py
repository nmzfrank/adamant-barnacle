import Encode
import Tkinter as Tk


def encode(rstr,txtbox):
	rg = Encode.randomGenerator(0.724,1000)
	plaintext = rstr;
	e = Encode.encode(plaintext,rg)
	ciphertext = e.transform()
	txtbox.insert(0,ciphertext)




def main():
	win = Tk.Tk()
	win.title('codeShell')
	win.geometry('800x200')
	str1 = Tk.Entry(win)
	str2 = Tk.Entry(win)
	btn1 = Tk.Button(win,text="||\n\\/",command= lambda: encode(str1.get(),str2))
	
	str1.pack()
	btn.pack()
	str2.pack()
	Tk.mainloop()


main()