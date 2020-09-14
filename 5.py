import tkinter as tk

#定义函数 从输入框enter获取数据  然后计算  赋值给标签label
def jisuan():
    a = float(enter.get())
    F = 1.8*a+32

    F = float('%0.2f'%F)
    label.config(text = F)


window = tk.Tk()

window.title('Entry 控件')

window.geometry('400x200')


label1 = tk.Label(window,text='摄氏度：')

enter = tk.Entry(window,text='0')

label2 = tk.Label(window,text='华氏度：')

label = tk.Label(window,text='代计算',fg='red')

button = tk.Button(window,text='计算',command = jisuan)


label1.pack()

enter.pack()

label2.pack()

label.pack()


button.pack()




window.mainloop()
