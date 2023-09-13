import tkinter as tk
from tkinter import messagebox
import sqlite3
import os


# starting GUI
root = tk.Tk()
# giving name to application and setting its height and width
root.title("To Do list")
root.geometry("400x300")

# setting min and max size of the root window
root.minsize(450, 500)
root.maxsize(450, 500)
root.config(bg='Blue')

# creating frames
startwindow = tk.Frame(root)
startwindow.config(background="Blue")
tab1frame = tk.Frame(root)
Viewfram = tk.Frame(root)
Createfram = tk.Frame(root)
updatefram = tk.Frame(root)


db_file = 'Todolist.db'

font_fam=("Arile",14)
def createdatabase():
    # Create a table for the amdin login
    conn.execute('''CREATE TABLE IF NOT EXISTS ToDoApp
                     (id INTEGER PRIMARY KEY,
                      todolist Text)''')

def startwindowfun():
    WELCOMEbut = tk.Label(startwindow, text="WELCOME", fg="black", height=2, width=20,background="blue",font=font_fam)
    WELCOMEbut.pack(pady=3)
    Loginbut = tk.Button(startwindow, text="Menu", fg="black", height=2, width=20,
                         command=lambda : goto_tab1(tab1frame))
    Loginbut.pack(pady=110)

def goto_tab1(frame,val=0):
    frame.config(background="blue")
    if startwindow.winfo_ismapped():  # if frame 1 is visible
        startwindow.pack_forget()  # hide frame 1
        for widget in startwindow.winfo_children():
            widget.destroy()
        tab1()
        frame.config(background="blue")
        frame.pack(pady=50 )  # show frame 2
    elif tab1frame.winfo_ismapped():
        tab1frame.pack_forget()
        for widget in tab1frame.winfo_children():
            widget.destroy()
        if(val==1):
            view()
            Viewfram.pack(fill="both",expand=True)
        elif(val==2):
            create()
            Createfram.pack(pady=50,fill="both",expand=True)
        elif(val==3):
            update()
            updatefram.pack(fill="both",expand=True)
    else:
        frame.pack_forget()  # hide frame 1
        for widget in frame.winfo_children():
            widget.destroy()
        tab1()
        tab1frame.config(background="blue")
        tab1frame.pack(pady=50)  # show frame 2
    pass

def tab1():
    Menubut = tk.Label(tab1frame, text="Menu", fg="black", height=2, width=20, background="blue", font=font_fam)
    Menubut.pack(pady=3)
    Viewbut = tk.Button(tab1frame, text="View", fg="black", height=2, width=20,
                         command=lambda: goto_tab1(Viewfram,1))
    Viewbut.pack(pady=20)

    Createbut = tk.Button(tab1frame, text="Create", fg="black", height=2, width=20,
                        command=lambda: goto_tab1(Createfram,2))
    Createbut.pack(pady=20)

    Updatebut = tk.Button(tab1frame, text="Update", fg="black", height=2, width=20,
                        command=lambda: goto_tab1(updatefram,3))
    Updatebut.pack(pady=20)


def view():
    todolist=tk.Label(Viewfram,text="TO DO LIST",font=font_fam,height=2,width=20,bg="Blue")
    todolist.pack(pady=10)

    order_items = conn.execute('SELECT id,todolist FROM ToDoApp ')

    # initializing the Canvas variable
    canvas = tk.Canvas(Viewfram)
    canvas.pack(side="left", fill="both", expand=True)
    # initializing the Scrollbar variable
    scrollbar = tk.Scrollbar(Viewfram, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.config(background="blue")
    # initializing the inner frame variable
    inner_frame = tk.Frame(canvas)
    inner_frame.config(background='blue')
    inner_frame.pack(fill="both", expand=True, padx=15)

    # creating the Canvas window
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # displaying data from the database on the screen
    for item in order_items:
        label = tk.Label(inner_frame, text=f'{item[0]}. {item[1]}', font=font_fam,bg="Blue")
        label.pack(pady=2, anchor="nw")

    Returnbut = tk.Button(inner_frame, text="Return", fg="black", height=2, width=20,
                        command=lambda: goto_tab1(Viewfram, 1))
    Returnbut.pack(pady=20)


def create():
    Create = tk.Label(Createfram, text="Create List", font=font_fam, height=2, width=20,bg="Blue")
    Create.pack(pady=10)

    label=tk.Label(Createfram,text="Enter Task:",font=font_fam, height=2, width=20,bg="Blue")
    label.pack()

    todo=tk.Entry(Createfram)
    todo.pack(pady=5)

    but = tk.Button(Createfram, text="Save", fg="black", height=1, width=20,
                   command=lambda: save(todo))
    but.pack(pady=10)


    Returnbut = tk.Button(Createfram, text="Return", fg="black", height=1, width=20,
                        command=lambda: goto_tab1(Createfram, 1))
    Returnbut.pack(pady=10)

def save(todo):
    val = todo.get()
    val=str(val)
    conn.execute(
        "INSERT INTO ToDoApp (todolist) "
        "VALUES (?)",
        (val,)
    )
    messagebox.showinfo("Created", "New Task Added to todo list")

def update():
    Update = tk.Label(updatefram, text="Update task list", font=font_fam, height=2, width=20,bg="Blue")
    Update.pack(pady=10)

    # creating a Canvas variable for the update frame
    canvas = tk.Canvas(updatefram)
    canvas.pack(side="left", fill="both", expand=True)

    # creating the Scroll barr variable for the update frame
    scrollbar = tk.Scrollbar(updatefram, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # configuring the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # initializing a inner frame so that we can scroll
    inner_frame = tk.Frame(canvas)
    inner_frame.grid(row=0, column=0, sticky="nsew")
    inner_frame.config(background="blue")
    canvas.config(background="blue")
    # initializing window for the canvas
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")


    # getting items from the database
    inventory_items = conn.execute('SELECT id,todolist FROM ToDoApp ')

    # displaying contents from the database on the screen
    for item in inventory_items:
        label = tk.Label(inner_frame, text=f'{item[0]}. {item[1]} ',font=font_fam,background="blue")
        label.pack(pady=2, anchor="nw")

    # creating label and entry field
    label = tk.Label(inner_frame, text="Enter id of Task you want to update: ",font=font_fam,background="blue")
    label.pack(anchor="nw", pady=5, padx=2)
    ident = tk.Entry(inner_frame)
    ident.pack(anchor="nw", padx=5,pady=5)

    # creating label and entry field
    label = tk.Label(inner_frame, text="Enter new Task:",font=font_fam,background="blue")
    label.pack(anchor="nw", padx=2)
    newqun = tk.Entry(inner_frame)
    newqun.pack(anchor="nw", padx=5,pady=5)

    # creating Button
    submit = tk.Button(inner_frame, text="Submit", fg="black", height=1, width=20,
                       command=lambda: submit12(ident, newqun))
    submit.pack(pady=10, padx=5, anchor="nw")

    Returnbut = tk.Button(inner_frame, text="Return", fg="black", height=1, width=20,
                          command=lambda: goto_tab1(updatefram, 1))
    Returnbut.pack(pady=5,padx=5, anchor="nw")


def submit12(id_en, new_quan):
    id = id_en.get()
    quan = new_quan.get()
    # updating the database
    conn.execute("UPDATE ToDoApp SET todolist = ? WHERE id = ?", (quan, id))
    goto_tab1(updatefram, 1)



if __name__ == "__main__":
    startwindowfun()
    if not os.path.isfile(db_file):
        conn = sqlite3.connect(db_file)
        createdatabase()
    else:
        conn = sqlite3.connect(db_file)

    startwindow.pack(pady=50)
    root.mainloop()
    conn.commit()
    conn.close()