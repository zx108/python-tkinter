import tkinter as tk

def callback():
    print('单击了“显示”菜单！')




window = tk.Tk()

window.title('Menu 控件')

window.geometry('400x400')

menubar = tk.Menu(window)

menubar.add_command(label='显示',command = callback)

menubar.add_command(label='推出',command = window.quit)

window.config(menu = menubar)

window.mainloop()
