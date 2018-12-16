from Tkinter import Tk, Label, Button, StringVar, Entry

app=Tk(className='Kalkulator')

L1=Label(app, text='Angka 1')
L1.grid(row=0, column=0)
str1=StringVar()
E1=Entry(app, textvariable=str1)
E1.grid(row=0, column=2, columnspan=3)

L2=Label(app, text='Angka 2')
L2.grid(row=1, column=0)
str2=StringVar()
E2=Entry(app, textvariable=str2)
E2.grid(row=1, column=2, columnspan=3)

def tambah():
           a=float(str1.get())
           b=float(str2.get())
           c=a+b
           hasil.config(text=c)
def kurang():
           a=float(str1.get())
           b=float(str2.get())
           c=a-b
           hasil.config(text=c)
def kali():
           a=float(str1.get())
           b=float(str2.get())
           c=a*b
           hasil.config(text=c)
def bagi():
           a=float(str1.get())
           b=float(str2.get())
           c=a/b
           hasil.config(text=c)

B1=Button(app, text='+', command=tambah)
B1.grid(row=2, column=0, pady=10)
B2=Button(app, text='-', command=kurang)
B2.grid(row=2, column=1)
B3=Button(app, text='x', command=kali)
B3.grid(row=2, column=2)
B4=Button(app, text=':', command=bagi)
B4.grid(row=2, column=3)

answer=Label(app, text='Hasil')
answer.grid(row=3, column=0, columnspan=2)
hasil=Label(app, text='0')
hasil.grid(row=3, column=2, columnspan=2)

app.mainloop()
