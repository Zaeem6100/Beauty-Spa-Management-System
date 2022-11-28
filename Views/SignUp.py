from tkinter import messagebox
from tkinter import *


class SignUp:
    @staticmethod
    def SignUpView():
        w = Tk()
        w.geometry('350x800')
        w.title(' S I G N  U P ')
        w.resizable(0, 0)

        # Making gradient frame
        j = 0
        r = 10
        for i in range(100):
            c = str(222222 + r)
            Frame(w, width=10, height=900, bg="#" + c).place(x=j, y=0)
            j = j + 10
            r = r + 1

        Frame(w, width=250, height=800, bg='white').place(x=50, y=50)
        # ----------------------------------- Username -----------------------------------
        l1 = Label(w, text='User Name', bg='white')
        l = ('Consolas', 13)
        l1.config(font=l)
        l1.place(x=80, y=70)
        # username entry for username entry
        username = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        username.config(font=l)
        username.place(x=80, y=100)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=130)

        # -------------------------------------------- Email --------------------------------------------
        l2 = Label(w, text='Email ', bg='white')
        l = ('Consolas', 13)
        l2.config(font=l)
        l2.place(x=80, y=160)
        # Email entry
        email = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        email.config(font=l)
        email.place(x=80, y=190)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=220)

        # -------------------------------------------- Full Name --------------------------------------------

        l3 = Label(w, text='Full Name', bg='white')
        l = ('Consolas', 13)
        l3.config(font=l)
        l3.place(x=80, y=250)
        # Full name entry
        fullname = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        fullname.config(font=l)
        fullname.place(x=80, y=280)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=310)

        # -------------------------------------------- Address --------------------------------------------
        l4 = Label(w, text='Address', bg='white')
        l = ('Consolas', 13)
        l4.config(font=l)
        l4.place(x=80, y=340)
        # Address entry
        address = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        address.config(font=l)
        address.place(x=80, y=370)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=400)

        # -------------------------------------------- Phone Number --------------------------------------------
        l5 = Label(w, text='Phone Number', bg='white')
        l = ('Consolas', 13)
        l5.config(font=l)
        l5.place(x=80, y=430)
        # phone number entry
        phone = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        phone.config(font=l)
        phone.place(x=80, y=460)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=490)

        # -------------------------------------------- Password --------------------------------------------
        l6 = Label(w, text='Password', bg='white')
        l = ('Consolas', 13)
        l6.config(font=l)
        l6.place(x=80, y=520)
        # Password entry
        password = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        password.config(font=l)
        password.place(x=80, y=550)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=580)

        # -------------------------------------------- Toggle Button   --------------------------------------------
        l7 = Label(w, text='Select User Type', bg='white')
        l = ('Consolas', 13)
        l7.config(font=l)
        l7.place(x=80, y=610)
        # radio group
        v = StringVar(value='customer')
        Radiobutton(w, text='Beautician', variable=v, value='beautician', bg='white').place(x=80, y=640)
        Radiobutton(w, text='Customer', variable=v, value='customer', bg='white').place(x=180, y=640)

        # Command
        # -------------------------------------------- Sign Up Button  Command --------------------------------------------
        def cmd():
            print(username.get())
            print(email.get())
            print(fullname.get())
            print(address.get())
            print(phone.get())
            print(password.get())
            print(v.get())
            from Model.User import User
            # check if all fields are filled

            if username.get() == '' or email.get() == '' or fullname.get() == '' or address.get() == '' or phone.get() == '' or password.get() == '':
                messagebox.showerror('Error', 'Please fill all the fields')

            elif User.checkUsernameExists(username.get()):
                messagebox.showerror('Error', 'Username already exists')

            else:
                # storing data to file

                user = User(Username=username.get(), email=email.get(), Fullname=fullname.get(), Address=address.get(),
                            phone_number=phone.get(), Password=password.get(), user_type=v.get())
                user.write_to_file()
                messagebox.showinfo('Success', 'Account Created Successfully')
                w.destroy()

        # Sign Up Button
        def bttn(x, y, text, ecolor, lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor  # when mouse enters the button it changes color
                myButton1['foreground'] = lcolor  # when mouse leaves the button it changes color

            def on_leavea(e):
                myButton1['background'] = lcolor  # when mouse enters the button it changes color
                myButton1['foreground'] = ecolor  # when mouse leaves the button it changes color

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

        bttn(100, 680, 'S I G N U P', 'white', '#994422')
        w.mainloop()


if __name__ == '__main__':
    SignUp()
