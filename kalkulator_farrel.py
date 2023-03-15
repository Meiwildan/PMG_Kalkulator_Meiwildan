import tkinter
from tkinter import *
root = Tk()
root.title('Kalkulator_Farrel')     
root.geometry("570x570+110+200")
root.resizable(False, False)
root.configure(bg='#2193b0')

perhitungan = []

#menambahkan angka
def show(value):
    label_tampil.config(text=value)

#menghapus semua angka
def clear():
    global perhitungan
    perhitungan = []
    label_tampil.config(text=perhitungan)
    
#proses perhitungan
def kalkulasi():
    global perhitungan
    if perhitungan and perhitungan[-1] == "Error":
        return
    kalkulasi = "".join(perhitungan)
    try:
        hasil = eval(kalkulasi)
        hasil = round(hasil, 10)
         
        if float(hasil).is_integer():
            hasil = int(hasil)
        show(str(hasil))
        perhitungan = [str(hasil)]
        
    except ZeroDivisionError:
        show("Tidak bisa dibagi dengan 0")
        perhitungan = []
    except SyntaxError:
        show("Error")
        perhitungan = []

#membuat operator perhitungan tidak lebih dari satu    
def handle_perhitungan(dobel):
    global perhitungan
    if perhitungan and perhitungan[-1] == "Error":
        return
    if perhitungan and perhitungan[-1] in ["+", "-", "*", "/", "."]:
        perhitungan[-1] = dobel
    else:
        perhitungan.append(dobel)
    show("".join(perhitungan))

#handling angka
def handle_number(number):
    global perhitungan
    if perhitungan and perhitungan[-1] == "Error":
        return
    if len(perhitungan) == 1 and perhitungan[0] == "0":
        perhitungan = []
    perhitungan.append(str(number))
    show("".join(perhitungan))

#menghapus angka satu persatu
def delete_each():
    global perhitungan
    if perhitungan:
        perhitungan.pop()
        if perhitungan:
            show("".join(perhitungan))
        else:
            show("0")

label_tampil = Label(root,width=27, height=2, text="", font=('Times New Roman',30))
label_tampil.pack()

Button(root, text="+", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_perhitungan('+')).place(x=10, y=110)
Button(root, text="-", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_perhitungan('-')).place(x=150, y=110)
Button(root, text="x", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_perhitungan('*')).place(x=290, y=110)
Button(root, text="÷", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_perhitungan('/')).place(x=430, y=110)

Button(root, text="7", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('7')).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('8')).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('9')).place(x=290, y=200)
Button(root, text="C", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: clear()).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('4')).place(x=10, y=290)
Button(root, text="5", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('5')).place(x=150, y=290)
Button(root, text="6", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('6')).place(x=290, y=290)
Button(root, text="CE", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command= delete_each).place(x=430, y=290)

Button(root, text="1", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('1')).place(x=10, y=380)
Button(root, text="2", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('2')).place(x=150, y=380)
Button(root, text="3", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#65C7F7", command=lambda: handle_number('3')).place(x=290, y=380)
Button(root, text="0", width=11, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_number('0')).place(x=10, y=470)

Button(root, text=".", width=5, height=1, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: handle_perhitungan('.')).place(x=290, y=470)
Button(root, text="=", width=5, height=3, font=("Times New Roman", 30, "bold"), fg="#fff", bg="#185a9d", command=lambda: kalkulasi()).place(x=430, y=380)



root.mainloop()