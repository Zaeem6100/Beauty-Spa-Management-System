from tkinter import *
from tkinter import messagebox

# variable for  entry 1
e1 = None
# variable for  entry 2
e2 = None


def Login():
    w = Tk()
    w.geometry('350x500')
    w.title(' L O G I N ')
    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=600, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    #  frame for white screen
    Frame(w, width=250, height=500, bg='white').place(x=50, y=50)

    #  label for username
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

    # button Action for Sign Up
    def Sign():
        import SignUp as s
        s.SignUp()

    # button Action for Login
    def cmd():
        # import function
        from Model import User
        u = User.User()
        # read data from file
        user = u.readAllUsers()
        # check if username and password is correct
        for i in user:
            if i.Username == e1.get() and i.Password == e2.get():
                messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        " + i.user_type.upper())
                # check if user is admin or not
                if i.user_type == 'Admin':
                    w.destroy()
                    from Views import manager as m
                    m.manager()
                    exit(0)
                elif i.user_type == 'customer':
                    w.destroy()
                    from Views import customer
                    customer.customer()
                    exit(0)

        messagebox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")

    #  sign up Button_with hover effect
    def bttn2(x, y, text, ecolor, lcolor):
        def on_entera2(e):
            myButton2['background'] = ecolor  # ffcc66
            myButton2['foreground'] = lcolor  # 000d33

        def on_leavea2(e):
            myButton2['background'] = lcolor
            myButton2['foreground'] = ecolor

        myButton2 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=Sign)

        myButton2.bind("<Enter>", on_entera2)
        myButton2.bind("<Leave>", on_leavea2)
        myButton2.place(x=x, y=y)

    # Login Button_with hover effect
    def bttn(x, y, text, ecolor, lcolor):
        def on_entera(e):
            myButton1['background'] = ecolor  # ffcc66
            myButton1['foreground'] = lcolor  # 000d33

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(w, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
        myButton1.place(x=x, y=y)

    bttn(100, 375, 'L O G I N', 'white', '#994422')
    bttn2(100, 425, 'S I G N U P', 'white', '#994422')
    w.mainloop()


if __name__ == '__main__':
    Login()
