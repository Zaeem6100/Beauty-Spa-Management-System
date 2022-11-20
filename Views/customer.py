from tkinter import *
import Model.User as u
import Model.Services as s
from Views.Table import Table
from Views.SignUp import SignUp
from Views.AddService import AddNewService


def customer():
    w = Tk()
    w.geometry('400x300')
    w.title(' C U S T O M E R')
    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=60, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1
    btn4 = Button(w, text='View Beautician', width=20, height=2, bg='#141414', fg='white', command=view_beauticians)
    btn4.place(x=100, y=100)
    btn5 = Button(w, text='View  Service', width=20, height=2, bg='#141414', fg='white', command=view_service)
    btn5.place(x=100, y=200)
    w.mainloop()


def view_beauticians():
    user = u.User()
    data = user.readAllUsers()
    dat = []
    columns = ('Full Name', 'Address', 'Phone Number', 'Email')
    headings = ('Full Name', 'Address', 'Phone Number', 'Email')
    for i in range(len(data)):
        if data[i].user_type == 'beautician':
            dat.append(data[i].convertToListForUser())

    Table(dat, columns, headings, title="Users")


def view_service():
    service = s.Services()
    data = service.read_from_file()
    dat = []
    columns = ('Service Name', 'Service Price')
    headings = ('Service Name', 'Service Price')
    for i in range(len(data)):
        dat.append(data[i].convertToList())

    Table(dat, columns, headings, title="Services")


if __name__ == '__main__':
    customer()
