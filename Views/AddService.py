from tkinter import messagebox
from tkinter import *


class Service:
    @staticmethod
    def AddNewService():
        w = Tk()
        w.geometry('350x400')
        w.title(' A D D  S E R V I C E ')
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
        # ----------------------------------- name -----------------------------------
        l1 = Label(w, text='Name', bg='white')
        l = ('Consolas', 13)
        l1.config(font=l)
        l1.place(x=80, y=70)
        # name entry for name entry
        name = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        name.config(font=l)
        name.place(x=80, y=100)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=130)

        # -------------------------------------------- price --------------------------------------------
        l2 = Label(w, text='Price', bg='white')
        l = ('Consolas', 13)
        l2.config(font=l)
        l2.place(x=80, y=160)
        # full name entry for full name entry
        price = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        price.config(font=l)
        price.place(x=80, y=190)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=220)

        # Command
        def cmd():
            print('Name: ', name.get())
            print('Price: ', price.get())
            import Model.Services as s
            s1 = s.Services(name.get(), price.get())
            s1.write_to_file()
            messagebox.showinfo('Success', 'Service Added Successfully')

        # Add Service  Button
        def bttn(x, y, text, ecolor, lcolor):
            def on_entera(e):
                myButton1['background'] = ecolor  # when mouse enters the button it changes color
                myButton1['foreground'] = lcolor  # when mouse leaves the button it changes color

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

        bttn(100, 250, 'A D D S E R V I C E', 'white', '#994422')
        w.mainloop()


if __name__ == '__main__':
    Service.AddNewService()
