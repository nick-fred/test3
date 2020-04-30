from tkinter import *
win=Tk() #创建窗口对象
win.title('计算器')
win.geometry('200x200+280+280') #窗口大小
#win.maxsize("1440x800")

#lable=tkinter.Label(win,text='hello,python')
#lable.pack()

#button1=tkinter.Button(win,text='button1')
#button1.pack(side=tkinter.LEFT)
#button2=tkinter.Button(win,text='button2')
#button2.pack(side=tkinter.RIGHT)
L1=Button(win,text='1',width=5,bg='yellow')
L2=Button(win,text='2',width=5)
L3=Button(win,text='3',width=5)
L4=Button(win,text='4',width=5)
L5=Button(win,text='5',width=5,bg='green')
L6=Button(win,text='6',width=5)
L7=Button(win,text='7',width=5)
L8=Button(win,text='8',width=5)
L9=Button(win,text='9',width=5,bg='yellow')
L0=Button(win,text='0')
Lp=Button(win,text='.')
L1.grid(row=0,column=0)
L2.grid(row=0,column=1)
L3.grid(row=0,column=2)
L4.grid(row=1,column=0)
L5.grid(row=1,column=1)
L6.grid(row=1,column=2)
L7.grid(row=2,column=0)
L8.grid(row=2,column=1)
L9.grid(row=2,column=2)
L0.grid(row=3,column=0,columnspan=2,sticky=E+W)
Lp.grid(row=3,column=2,sticky=E+W)



win.mainloop();
