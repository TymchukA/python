from tkinter import *

root =Tk()
root.title('7')
root.geometry('350x150')

def calculate(event):
     v = var.get()
     num1 = EntryFirst.get()
     num2 = EntrySecond.get()
     num3 = EntryThird.get()
     if v == 0:
          Result['text'] = min([float(num1),float(num2),float(num3)])/max([float(num1),float(num2),float(num3)])
     elif v == 1:
          Result['text'] = max([float(num1),float(num2),float(num3)])/min([float(num1),float(num2),float(num3)])
	

FirstNumber = Label(root, text ="Число один:", fg = "black")
EntryFirst = Entry(root)
SecondNumber = Label(root, text ="Число два:", fg = "black")
EntrySecond = Entry(root)
ThirdNumber = Label(root, text ="Число три:", fg = "black")
EntryThird = Entry(root)
Result = Label(root, text ="Тут буде результат", fg = "black")


FirstNumber.grid (row=0, sticky = E)
SecondNumber.grid (row=1, sticky = E)
ThirdNumber.grid (row=2, sticky = E)

EntryFirst.grid (row=0, column=1)
EntrySecond.grid (row=1, column=1)
EntryThird.grid (row=2, column=1)

var=IntVar()
var.set(0)
radio1 = Radiobutton (root, text = "найменше/найбільше",variable = var, value = 0)
radio1.grid (row=4,column = 0, sticky = E)

radio2 = Radiobutton (root, text = "найбільше/найшменше",variable = var, value = 1)
radio2.grid (row = 4, column = 1, sticky =E)


button1 = Button (root, text ="Вирахувати")
button1.bind('<Button-1>',calculate) 
button1.grid (columnspan = 2)
Result.grid(columnspan = 2)
root.mainloop()
