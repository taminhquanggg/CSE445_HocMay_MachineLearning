from sklearn import datasets, linear_model
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("D:/oto.csv", delimiter=',')
X = np.array(df[['SOCHO','DUNGTICHBINH','CONGSUAT']].values)
Y = np.array(df['GIAXE']).T
regr1 = linear_model.LinearRegression()
regr1.fit(X,Y)
w_0=regr1.intercept_
w_1=regr1.coef_


form = Tk()
form.title("ÄÃ¡nh giÃ¡ giÃ¡ xe")
winwidth = form.winfo_screenwidth()
winheight = form.winfo_screenheight()
form.geometry('540x260+%d+%d' %(winwidth/2-270 ,winheight/2-130))
lb1 = Label(form, text="Nháº­p thÃ´ng sá»‘ liÃªn quan Ä‘á»ƒ dá»± Ä‘oÃ¡n: " , font = "Times 12 bold").grid(row = 0, column = 0 , padx = 4, pady = 5)
lb_chongoi = Label(form, text="Nháº­p thÃ´ng tin chá»— ngá»“i: ").grid(row = 1, column = 0)
tb_chongoi = Entry(form)
tb_chongoi.grid(row = 1 , column =1, pady = 4)
lb_dungtich = Label(form, text="Nháº­p dung tÃ­ch bÃ¬nh xÄƒng : ").grid(row = 2, column = 0)
tb_dungtich = Entry(form)
tb_dungtich.grid(row = 2 , column =1, pady = 4)
lb_dongco = Label(form, text="Nháº­p thÃ´ng Ä‘á»™ng cÆ¡: ").grid(row = 3, column = 0)
tb_dongco = Entry(form)
tb_dongco.grid(row = 3 , column =1, pady = 4)


def duDoan():
    data1 = float(tb_chongoi.get())
    data2 = float(tb_dungtich.get())
    data3 = float(tb_dongco.get())
    if(data1 != "" and data2 != "" and data3 != ""):
        a = np.array([data1,data2,data3]).T
        kqDuDoan = np.dot(w_1, a) + w_0
        messagebox.showinfo( "Káº¿t quáº£ dá»± Ä‘oÃ¡n","Há»‡ thá»‘ng dá»± Ä‘oÃ¡n lÃ  "+ str(kqDuDoan)+ " triá»‡u VND")  
    else:
         messagebox.showerror("Lá»—i", "Vui lÃ²ng nháº­p Ä‘áº§y Ä‘á»§ thÃ´ng tin")
bt_dudoan = Button(form,  text='Dá»± Ä‘oÃ¡n', command=duDoan)
bt_dudoan.grid(row=4, column=0, padx = 10,  pady=10)



def exit():
    if(messagebox.askyesno("ThÃ´ng bÃ¡o", "Báº¡n cÃ³ muá»‘n thoÃ¡t khÃ´ng")):
         form.destroy()
Button(form, text='ThoÃ¡t' , command = exit).grid(row=4,column=2,padx = 10,  pady=10)




form.mainloop()