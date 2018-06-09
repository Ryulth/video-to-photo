import tkinter as tk
from tkinter import filedialog

pathin = ""




if __name__ == "__main__":
    arg = ["",""]
    root = tk.Tk()
    root.title("sex")
    menubar = tk.Menu(root)

    filemenu = tk.Menu(menubar, tearoff=0)


    def path():
        tk.Tk().withdraw()  # Close the root window
        pathin = filedialog.askopenfilename()
        print(pathin)
        arg[0] = pathin

    def donothing():
        filewin = tk.Toplevel(root)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()

    filemenu.add_command(label="Open", command=path)

    filemenu.add_command(label="Save", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tk.Menu(menubar, tearoff=0)
   # root.geometry("200x150")
    lbl = tk.Label(root, text="input Frame")
    lbl.grid(row=0, column=0)
    txt = tk.Entry(root)
    txt.grid(row=0, column=1)
    lbl_fin=tk.Label(root,text="")
    lbl_fin.grid(row=1, column=1)


    def clicked():
        value=txt.get()
        res = txt.get() + " Frames"
        print(value)
        print(res)
        lbl_fin.configure(text=res)
        #lbl_fin2.configure(text="Frame")
        arg[1] = value
        print(arg)


    processbt = tk.Button(root, text="Make_Panorama", width=15, command=clicked)
    processbt.grid(row=0, column=2)
    #lbl_fin.cget()
    frame = txt.get()
    print(type(frame))
    print(frame)

    """"
    pathbt = tk.Button(root, text="Path",width = 15, command=path)
    pathbt.grid(row=1,column=0)
    processbt=tk.Button(root, text="Make_Panorama",width = 15, command=path)
    processbt.grid(row=1,column=1)
    """
    root.config(menu=menubar)
    root.mainloop()
    #main()