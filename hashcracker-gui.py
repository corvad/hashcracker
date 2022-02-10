import time
import hashlib
from tkinter import *
gui = Tk()

def run_cracker(hashtocrack,al,wordlist):
    
    def md5():
        
        f = open(wordlist, "r", errors="ignore")
        for x in f:
            x = str(x).strip()
            y = x.encode()
            z = hashlib.md5(y).hexdigest()
            if(z.__eq__(str(hashtocrack))):
                return "Password is :: " + x

    def sha1():
        f = open(wordlist, "r", errors="ignore")
        for x in f:
            x = str(x).strip()
            y = x.encode()
            z = hashlib.sha1(y).hexdigest()
            if(z.__eq__(str(hashtocrack))):
                return "Password is :: " + x
    hashtocrack = hashtocrack.lower()
    if(al.__eq__("sha1")):
        return sha1()
        
    else:
        return md5()
    


def gui_runner():
    gui.title('hashcrack')
    #gui.geometry('600x400+50+50')

    ww = 600
    wh = 600

    sw = gui.winfo_screenwidth()
    sh = gui.winfo_screenheight()

    cx = int(sw/2 - ww / 2)
    cy = int(sh/2 - wh / 2)

    gui.geometry(f'{ww}x{wh}+{cx}+{cy}')

    l1 = Label(gui, text = "Enter Hash Below")
    l1.place(x=300,y=20,anchor="center")

    e1 = Entry(gui)
    e1.place(x=300,y=60,anchor="center",width=300)

    def hash():
        result = run_cracker(e1.get(),ha.get(),e2.get())
        l4 = Label(gui,text=str(result))
        l4.place(x=300,y=300,anchor="center")
        
    b = Button(gui, text="Crack the Hash!", command=hash)
    b.place(x=300,y=550,anchor="center")

    l2 = Label(gui, text = "Select the Hashing Algorithm Below")
    l2.place(x=300,y=120,anchor="center")

    possible = list(hashlib.algorithms_available)

    print(possible)

    ha = StringVar()
    ha.set("sha1")

    select = OptionMenu(gui,ha,*possible)
    select.pack()
    select.place(x=300,y=160,anchor="center")

    l3 = Label(gui, text = "Provide the Path to the Desired Wordlist Below")
    l3.place(x=300,y=200,anchor="center")

    e2 = Entry(gui)
    e2.place(x=300,y=240,anchor="center",width=300)



    b = Button(gui, text="Crack the Hash!", command=hash)
    b.place(x=300,y=550,anchor="center")



    gui.mainloop()


if __name__ == "__main__":
    gui_runner()
