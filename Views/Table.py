from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def Table(data, columns, headings, title="Table"):
    ws = Tk()
    ws.title(title)
    ws.geometry('1398x200')
    ws['bg'] = '#AC99F2'
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(ws, width=1120, height=1600, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1


    game_frame = Frame(ws)
    game_frame.pack()
    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)
    game_scroll = Scrollbar(game_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)
    my_game.pack()
    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)
    my_game['columns'] = columns
    my_game.heading("#0", text="Sr#", anchor=W)
    for i in headings:
        my_game.heading(i, text=i, anchor=W)

    for i in range(len(data)):
        # add serial number in first column
        my_game.insert(parent='', index='end', iid=i, text=i + 1, values=data[i])
        pass

    my_game.pack()
    ws.mainloop()


if __name__ == '__main__':
    import Model.User as u
    user = u.User()
    data = user.readAllUsers()
    print(data)
    columns = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
    headings = ('User Name', 'Password', 'Full Name', 'Address', 'Phone Number', 'Email')
    Table(data, columns, headings , title="Users")
