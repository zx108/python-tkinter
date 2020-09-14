import tkinter as tk

window = tk.Tk()

demo = tk.Tk()


window.title('Label 控件')
window.geometry('600x600')


demo.geometry('300x200')

#Label控件是用于在界面上输出描述信息的标签，可以显示文本和图像。
#注意控件要放在哪一个窗体上
label = tk.Label(demo,text='Label studyyyyyyyyyy',bg='black',fg='white',font=('宋体'),width='20',height='3')

label.pack()


demo.mainloop()
window.mainloop()
