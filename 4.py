import tkinter as tk

#定义函数
def btnHelloClicked():
    labelHello.config(text='Hello World!',fg='red')



window = tk.Tk()

window.title('Button 控件')
window.geometry('400x400')

labelHello = tk.Label(window,text='Prece the button...',height='5')

#Button 大多数属性都于Label一致，但是Button有一个  command  属性用于绑定函数或方法，当用户点击该按钮时，就会调用该函数。
button = tk.Button(window,text='Hello',command = btnHelloClicked)

labelHello.pack()
button.pack()


window.mainloop()
