import tkinter as tk



def colorCheck():
    labelHello.config(fg=color.get())



def typeCheck():
    c = a.get()+b.get()
    labelHello.config(text=str(c),font=('宋体',24))


window = tk.Tk()
window.title('Radiobutton  and   Checkbutton   (单选框和复选框)')
window.geometry('300x400')


#创建标签
labelHello = tk.Label(window,text='check the format of text',height='3',font=('Arial',12))
labelHello.pack()


#获取单选框输入
color = tk.StringVar()
color.set(0)


#创建三个单选框并显示
tk.Radiobutton(window,text='red',variable=color,value='red',command=colorCheck).pack()

tk.Radiobutton(window,text='green',variable=color,value='green',command=colorCheck).pack()

tk.Radiobutton(window,text='blue',variable=color,value='blue',command=colorCheck).pack()

#获取两个复选框输入
a = tk.IntVar()
b = tk.IntVar()


#创建两个复选框并输入

tk.Checkbutton(window,text='1',variable=a,onvalue=1,offvalue=0,command=typeCheck).pack()

tk.Checkbutton(window,text='2',variable=b,onvalue=2,offvalue=0,command=typeCheck).pack()






window.mainloop()#主事件循环


