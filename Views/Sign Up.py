from tkinter import messagebox
from tkinter import *


def SignUp():
    w = Tk()
    w.geometry('350x500')
    w.title(' S I G N  U P ')
    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    Frame(w, width=250, height=400, bg='white').place(x=50, y=50)
    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)
    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)
    # e2 entry for password entry
    e2 = Entry(w, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=310)
    l2 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=280)

    ###lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)

    # Command
    def cmd():
        if e1.get() == '' or e2.get() == '':
            messagebox.showinfo("SIGN UP  FAILED", "        PLEASE TRY AGAIN        ")
        else:
            messagebox.showwarning("SIGN UP SUCCESSFULLY", "         W E L C O M E        ")
            w.destroy()
            q = Tk()
            q.mainloop()

    # Sign Up Button
    b = Button(w, text='Sign Up', command=cmd, bg='#141414', fg='white', border=0)
    l = ('Consolas', 13)
    b.config(font=l)
    b.place(x=80, y=380)
    w.mainloop()


if __name__ == '__main__':
    SignUp()
