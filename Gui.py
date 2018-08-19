#trying to make gui
from tkinter import *
import PyPDF2
import os,random

window=Tk()
window.geometry("500x800")
window.configure(background='khaki3')
window.title("PDF To TEXT BY Saurabh Jadhav")
l1=Label(text='An Awesome PDF2TEXT\nBy Saurabh Jadhav',font=('Times',18),fg='white',bg='purple')
l1.pack(fill=X)
l2=Label(window,text='Enter File Location :',font=('Century gothic',17),background='khaki2')
l2.pack()
e1=Entry(window,font=('Lucida calligraphy',10))
e1.pack()
b1=Button(window,text="Go",font=('Times',16),background='khaki4',fg='white',command=lambda: code(e1.get()))
b1.pack()
t1=Text(height=4,font=('Comic sans ms',18),bg='sienna4',fg='white')
t1.pack(fill=X)
l3=Label(window,text='''"Every great developer you know
got there by solving problems 
they were unqualified to solve until 
they actually did it."
  - Patrick McKenzie''',font=('Comic sans ms',21))
l3.pack()
#code
def code(path):

	try:
		res=open(path,'rb')
		pdf=PyPDF2.PdfFileReader(res)
		num=pdf.numPages
		text=''
		title=path[4:-4]+'.txt'
		for i in range(num):
			
			text=text+pdf.getPage(i).extractText()

		
		try:
			os.mkdir("MYFolder")
			os.chdir("MYFolder")
		except FileExistsError:
			os.chdir("MYFolder")
			
		
		f=open("MYfile.txt","w+")
		f.write("Converted BY PDF to TEXT converter BY \n Saurabh Jadhav\n")
		f.write(text)
		f.close()
		t1.delete(1.0,END)
		t1.insert(END,"Your PDF is Converted in Txt\n Successfuly !!")

	except FileNotFoundError:
		t1.delete(1.0,END)
		t1.insert(END,"FileNotFoundError check file Location")
	
	

window.mainloop()