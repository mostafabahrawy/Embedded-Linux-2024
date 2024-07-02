import tkinter

def Button():
    print(f'You touched Ba7r')

m = tkinter.Tk()
m.title('Ba7r')
button1 = tkinter.Button(m, text='Button1', width=20, command=Button).grid(row=0, column=1)
button2 = tkinter.Button(m, text='Button2', width=20, command=Button).grid(row=1, column=0)
button3 = tkinter.Button(m, text='Button3', width=20, command=Button).grid(row=1, column=2)
button4 = tkinter.Button(m, text='Button4', width=20, command=Button).grid(row=2, column=1)

m.mainloop()