import dirs
from tkinter import *
from tkinter import ttk, filedialog

root = Tk()
root.title("Docx to Doc and PDF converter")
root.geometry('560x120')

def starten():
    text_message.set("Ich fange an...")
    if not input_path.get() == "":
        message = dirs.create_out_dir(input_path.get())
        text_message.set(message)
    else:
        text_message.set("Wählen Sie einen Ordner")
    # message = dirs.create_out_dir(input_path)

def path_browse():
    dir_name = filedialog.askdirectory(initialdir="./", title="Ordner wählen")
    input_path.set(dir_name)

mainframe = ttk.Frame(root, padding="20 20 20 20") # create the mainframe
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # maintain on the screen (on the root)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input_path = StringVar()
text_message = StringVar()

ttk.Label(mainframe, text="Input Ordner", width=12).grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, textvariable=text_message, width=12).grid(column=2, row=3, sticky=W)

path_entry = ttk.Entry(mainframe, width=50, textvariable=input_path)  # create an entry
path_entry.grid(column=2, row=1, sticky=(W, E)) # maintain it on the mainframe

ttk.Button(mainframe, text="Ordner wählen", width=15, command=path_browse).grid(
    column=3, row=1, sticky=(W, E)
)

ttk.Button(mainframe, text='Start', command=starten).grid(column=1, row=3, sticky=(W, E))


for child in mainframe.winfo_children():  # Padding for every element of the mainfraim.
    child.grid_configure(padx=5, pady=10)  # Could be written when initialized

path_entry.focus() # Cursor starts at the path_entry Entry

root.bind("<Return>", starten) # Enter -> starten()

root.mainloop()