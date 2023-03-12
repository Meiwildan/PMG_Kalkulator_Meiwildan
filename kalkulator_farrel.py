import tkinter
from tkinter import *
root = Tk()
root.title('Kalkulator_Farrel')
root.geometry("570x570+110+200")
root.resizable(False, False)
root.configure(bg='#2193b0')

perhitungan = ""

def show(value):
    global perhitungan
    perhitungan+=value
    label_tampil.config(text=perhitungan)
    
def clear():
    global perhitungan
    perhitungan = ""
    label_tampil.config(text=perhitungan)
    
def kalkulasi():
    global perhitungan
    hasil = ""
    if perhitungan !="":
        try:
            hasil = eval(perhitungan)
            hasil = round(hasil,10)
            if float(hasil).is_integer():
                hasil = int(hasil)
                
        except(SyntaxError, ZeroDivisionError):
            hasil = "error"
            perhitungan = ""
    label_tampil.config(text=hasil)
    
def delete_each():
    try:
        global perhitungan
        list = []
        list.extend(perhitungan)
        list.pop(len(list) -1)
        hasil = ''.join(list)
        perhitungan = hasil
        label_tampil.config(text=perhitungan)
    except:
        label_tampil.config(text='0')

label_tampil = Label(root,width=27, height=2, text="", font=('Times New Roman',30))
label_tampil.pack()

Button(root, text="+", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: show('+')).place(x=10, y=110)
Button(root, text="-", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: show('-')).place(x=150, y=110)
Button(root, text="x", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: show('*')).place(x=290, y=110)
Button(root, text="÷", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: show('/')).place(x=430, y=110)

Button(root, text="7", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('7')).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('8')).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('9')).place(x=290, y=200)
Button(root, text="C", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: clear()).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('4')).place(x=10, y=290)
Button(root, text="5", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('5')).place(x=150, y=290)
Button(root, text="6", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('6')).place(x=290, y=290)
Button(root, text="CE", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command= delete_each).place(x=430, y=290)

Button(root, text="1", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('1')).place(x=10, y=380)
Button(root, text="2", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('2')).place(x=150, y=380)
Button(root, text="3", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('3')).place(x=290, y=380)
Button(root, text="0", width=11, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('0')).place(x=10, y=470)

Button(root, text=".", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: show('.')).place(x=290, y=470)
Button(root, text="=", width=5, height=3, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: kalkulasi()).place(x=430, y=380)



root.mainloop()