import tkinter as tk

x=False

def nextp5():
    global entryone
    global entrytwo
    global entrythree
    global enter4
    global app6
    global x
    x=True
    entryfour = enter4.get()
    tale = "Yesterday you went to "+str(entryone)+". When there you did "\
           +str(entrytwo)+". You went there with "+str(entrythree)+\
           ". Afterwards you went to "+str(entryfour)+"."
    app6 = Window()
    explainah = tk.Label(app6, text="Here is the story you made!")
    explainah.grid(column=0, row=0)
    story = tk.Text(app6, height=15, width=40)
    story.grid(column=0, row=1)
    story.insert(tk.END, tale)
    continueb6 = tk.Button(app6, text="Play again", command=nextp)
    continueb6.grid(column=0, row=2)
    leave = tk.Button(app6, text="Or leave", command=app6.quit)
    leave.grid(column=0, row=3)
    app5.destroy()
    app6.mainloop()
    
def nextp4():
    global app5
    global app4
    global enter3
    global entrythree
    global enter4
    entrythree = enter3.get()
    app5 = Window()
    sen4 = tk.Label(app5, text="Afterwards you went to ")
    sen4.grid(row=1, column=0)
    inst = tk.Label(app5, text="Enter a word and press continue")
    inst.grid(row=0, column=0)
    enter4 = tk.Entry(app5, width=10)
    enter4.grid(row=2, column=0)
    continueb5 = tk.Button(app5, text="Continue", command=nextp5)
    continueb5.grid(row=3, column=0)
    app4.destroy()
    app5.mainloop()

def nextp3():
    global app4
    global app3
    global enter2
    global entrytwo
    global enter3
    entrytwo = enter2.get()
    app4 = Window()
    sen3 = tk.Label(app4, text="You went there with ")
    sen3.grid(row=1, column=0)
    inst = tk.Label(app4, text="Enter a word and press continue")
    inst.grid(row=0, column=0)
    enter3 = tk.Entry(app4, width=10)
    enter3.grid(row=2, column=0)
    continueb4= tk.Button(app4, text="Continue", command=nextp4)
    continueb4.grid(row=3, column=0)
    app3.destroy()
    app4.mainloop()

def nextp2():
    global app2
    global app3
    global entryone
    global enter1
    global enter2
    app3 = Window()
    sen2 = tk.Label(app3, text="When there you did ")
    sen2.grid(row=1, column=0)
    inst = tk.Label(app3, text="Enter a word and press continue")
    inst.grid(row=0, column=0)
    enter2 = tk.Entry(app3, width=10)
    enter2.grid(row=2, column=0)
    continueb3 = tk.Button(app3, text="Continue", command=nextp3)
    continueb3.grid(row=3, column=0)
    entryone = enter1.get()
    app2.destroy()
    app3.mainloop()

def nextp():
    global app2
    global app6
    global entryone
    global enter1
    global x
    app2 = Window()
    sen1 = tk.Label(app2, text="Yesterday you went to ")
    sen1.grid(row=1, column=0)
    inst = tk.Label(app2, text="Enter a word and press continue")
    inst.grid(row=0, column=0)
    enter1 = tk.Entry(app2, width=10)
    enter1.grid(row=2, column=0)
    continueb2 = tk.Button(app2, text="Continue", command=nextp2)
    continueb2.grid(row=3, column=0)
    app.destroy()
    if x == True:
        app6.destroy()
    else:
        pass
    app2.mainloop()
    
class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.quitb = tk.Button(self, text="Exit", command=self.quit)
        self.quitb.grid(column=2, row=0)
        

app = Window()
intro = tk.Label(app, text="You will get a sentence, enter a word")
intro.grid(column=0, row=0)
continueb = tk.Button(app, text="Continue", command=nextp)
continueb.grid(column=0, row=1)
app.master.title("Madlibs!")
app.master.geometry('300x300')
app.mainloop()
