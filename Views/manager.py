from tkinter import *
import Model.User as u
import Model.Services as s
from Views.Table import Table
from Views.SignUp import *
from Views.AddService import *
from Views.login import *


class Managers:

    @staticmethod
    def manager():
        w = Tk()
        w.geometry('650x400')
        w.title(' M A N A G E R')
        w.resizable(0, 0)

        # Making gradient frame
        j = 0
        r = 10
        for i in range(100):
            c = str(222222 + r)
            Frame(w, width=10, height=900, bg="#" + c).place(x=j, y=0)
            j = j + 10
            r = r + 1

        m = Managers()
        Frame(w, width=550, height=800, bg='white').place(x=50, y=50)
        btn1 = Button(w, text='View Customers', width=20, height=2, bg='#141414', fg='white', command=m.view_customer)
        btn1.place(x=100, y=100)

        btn2 = Button(w, text='Add Service', width=20, height=2, bg='#141414', fg='white', command=m.add_service)
        btn2.place(x=100, y=200)

        btn3 = Button(w, text='Add User', width=20, height=2, bg='#141414', fg='white', command=m.add_customer)
        btn3.place(x=100, y=300)

        btn4 = Button(w, text='View Beautician', width=20, height=2, bg='#141414', fg='white',
                      command=m.view_beauticians)
        btn4.place(x=400, y=100)

        btn5 = Button(w, text='View  Service', width=20, height=2, bg='#141414', fg='white', command=m.view_service)
        btn5.place(x=400, y=200)

        w.mainloop()

    @staticmethod
    def view_customer():
        user = u.User()
        data = user.readAllUsers()
        dat = []
        columns = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
        headings = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
        for i in range(len(data)):
            if data[i].user_type == 'customer':
                dat.append(data[i].convertToList())

        Table(dat, columns, headings, title="Users")

    @staticmethod
    def view_beauticians():
        user = u.User()
        data = user.readAllUsers()
        dat = []
        columns = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
        headings = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
        for i in range(len(data)):
            if data[i].user_type == 'beautician':
                dat.append(data[i].convertToList())

        Table(dat, columns, headings, title="Users")

    @staticmethod
    def view_service():
        service = s.Services()
        data = service.read_from_file()
        dat = []
        columns = ('Service Name', 'Service Price')
        headings = ('Service Name', 'Service Price')
        for i in range(len(data)):
            dat.append(data[i].convertToList())

        Table(dat, columns, headings, title="Services")

    @staticmethod
    def add_service():
        Service.AddNewService()

    @staticmethod
    def add_customer():
        SignUp.SignUpView()

    @staticmethod
    def add_employee():
        SignUp.SignUpView()


if __name__ == '__main__':
    Managers.manager()
