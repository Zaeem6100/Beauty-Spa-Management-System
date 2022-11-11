from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def Table(data, columns, headings, title="Table"):
    ws = Tk()
    ws.title(title)
    ws.geometry('500x500')
    ws['bg'] = '#AC99F2'
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
    my_game.heading("#0", text="", anchor=CENTER)
    for i in headings:
        my_game.heading(i, text=i, anchor=CENTER)

    for i in range(len(data)):
        my_game.insert(parent='', index='end', iid=i, text="", values=data[i])
        pass

    my_game.pack()
    ws.mainloop()


Table(None)
