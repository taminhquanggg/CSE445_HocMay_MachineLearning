
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def convert_text_to_number(X):
	for i in range(len(X)):
		for j in range(len(X[i])):
			if(X[i][j] == "yes"):
				X[i][j] = 3
			elif(X[i][j] == "no"):
				X[i][j] = 1
			elif(X[i][j] == "furnished"):
				X[i][j] = 4
			elif(X[i][j] == "semi-furnished"):
				X[i][j] = 5
			elif(X[i][j] == "unfurnished"):
				X[i][j] = 6
	return X
list_textbox = []
def Form(name_row,tieude,data_predic,datacombo,predict):
	form = Tk()
	form.title("Đánh giá giá nhà bằng thuật toán " +str(tieude))
	winwidth = form.winfo_screenwidth()
	winheight = form.winfo_screenheight()
	form.geometry('640x460+%d+%d' %(winwidth/2-320 ,winheight/2-230))
	for i in range(0,12):
		form.columnconfigure(i, weight=1)
	lable_title = Label(form, text="NHẬP THÔNG TIN LIÊN QUAN ĐỂ DỰ ĐOÁN " , bg='#fff', fg='red', font = "Arial 15 bold")
	lable_title.grid(row = 0,columnspan = 12 , padx = 4, pady = 5,sticky = N)
	dem = 1
	for i in name_row:
		if (dem%2 != 0):
			labe = Label(form, text = i)
			labe.grid(column = 0,columnspan = 2, row=dem,  padx = (30,10), pady=10 ,sticky = "NWSE")
			textbox = ttk.Combobox(form, width=30)
			textbox.grid(column=2,columnspan = 4, row=dem, padx=(0,10), pady=10,sticky = "NWSE")
			textbox['values'] = datacombo[dem-1]
			list_textbox.append((i, textbox))
		else:
			labe = Label(form, text = i)
			labe.grid(column=6, columnspan = 2,row=dem-1, padx = (10,10), pady=10,sticky = "NWSE")
			textbox = ttk.Combobox(form,width=30)
			textbox.grid(column=8,columnspan = 4, row=dem-1, padx=(0,30), pady=10,sticky = "NWSE")
			textbox['values'] = datacombo[dem-1]
			list_textbox.append((i, textbox))
		dem = dem + 1
	def hienthi():
		data = []
		for entry in list_textbox:
			raw_data_point = entry[1].get()
			if (raw_data_point != ""):
				data.append(raw_data_point)
			else:
				messagebox.showerror("Thông Báo ","Mời bạn nhập đủ thông tin")
				data = []
				break
		if(data != []):
			try:
				data_list = []
				data_list.append(data)
				data_convert  = convert_text_to_number(data_list)
				messagebox.showinfo("Thông Báo ","Với thuật toán "+str(tieude)+" hệ thống dự đoán : " + str(predict(data_convert)))	
			except:
				messagebox.showerror("Thông Báo ","Thông tin bạn đã nhập sai với định dạng dự đoán")	
	Button(form, text = "Dự đoán " , command =hienthi ).grid(column=2,columnspan = 5, row=dem+1, padx=(0,10), pady=10,sticky = "NWSE")
	# Button(form, text = "Dự đoán ").grid(column=7,columnspan = 5,row=dem+1, padx=(10,30), pady=10,sticky = "NWSE")
	richtext = Text(form)
	richtext.grid( row = dem + 2, sticky = "NWSE", column=0,columnspan = 12, padx = 10, pady = 10)
	richtext.insert(tk.END,data_predic)
	richtext["state"] = "disabled"
	form.mainloop()
def get_Data_combobox(X):
	giatri = []
	for j in range(len(X[0])):
		cot = []
		for i in range(len(X)):
			cot.append(X[i][j])
		giatri.append(list(set(cot)))
	return giatri
