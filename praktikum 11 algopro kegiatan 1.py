from Tkinter import Tk, Label, Entry, Button

my_app=Tk(className='kegiatan 1')

L1=Label(my_app, text="Data Diri", font=('Arial, 24'))
L1.grid(row=0,column=0)

L2=Label(my_app, text="Nama")
L2.grid(row=1,column=0, sticky='w')
L3=Label(my_app, text="Safira Putri Kinanti")
L3.grid(row=1, column=1)

L4=Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky='w')
L5=Label(my_app, text="L200180145")
L5.grid(row=2,column=1, sticky='w')

L6=Label(my_app, text="Buku Favorit")
L6.grid(row=3, column=0, sticky='w')
L7=Label(my_app, text="The Book Of Almost")
L7.grid(row=3, column=1, sticky='w')

L8=Label(my_app, text="Idola dikalangan sahabat")
L8.grid(row=4, column=0, sticky='w')
L9=Label(my_app, text="Umar Bin Khattab")
L9.grid(row=4, column=1, sticky='w')

L10=Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky='w')
L11=Label(my_app, text="Teruslah berusaha untuk mendapatkan apa yang kita inginkan")
L11.grid(row=5, column=0, sticky='w')

B=Button(my_app, text='Tutup', command=my_app.destroy)
B.grid(row=6,column=1)
my_app.mainloop()
