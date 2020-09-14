import tkinter as tk

window = tk.Tk()

window.title('p209')

window.geometry('200x100')

#鼠标单击绑定事件

def func(event):
    print('单击！')

window.bind('<Button-1>',func)

#鼠标双击绑定事件

def func1(event):
    print('双击！')

window.bind('<Double-Button-1>',func1)

#实现拖拽功能
def func2(event):
    x = str(event.x_root)
    y = str(event.y_root)
    window.geometry('200x100+'+x+'+'+y)

window.bind("<B1-Motion>",func2)


#实时获取移动鼠标的坐标
def func3(event):
    x = event.x
    y = event.y

    print(x,y)

window.bind('<Motion>',func3)

#label 鼠标移入事件

def func4(event):
    label1.config(fg='red',font=('宋体','18'))

label1 = tk.Label(window,text = 'mouse')
label1.bind('<Enter>',func4)
label1.pack()




window.mainloop()
