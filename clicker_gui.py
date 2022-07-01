from tkinter import Button,Entry,Label,Tk
from time import sleep
from keyboard import add_hotkey, write

runningStatus = True

def exitLoopEvent():
    global runningStatus
    runningStatus=False
    pass

def runProgram():
    entryKey1.get()
    entryKey2.get()
    entryKey3.get()
    sleep(5)
    b=True
    add_hotkey("esc", exitLoopEvent)
    while runningStatus:
        write(entryKey1.get()+entryKey2.get(),0.1)
        sleep(int(entryKey3.get())/1000)
        
root = Tk()

labelKey1=Label(root, text="Klawisz 1", padx=10,pady=10)
labelKey2=Label(root, text="Klawisz 2", padx=10,pady=10)
labelDelay=Label(root, text="delay [ms]", padx=10,pady=10)

entryKey1=Entry(root, width=2, border=2)
entryKey2=Entry(root, width=2, border=2)
entryKey3=Entry(root, width=5, border=2)

startButton=Button(root,text="Start", command=runProgram, bg="white")

labelKey1.grid(row=0,column=0)
labelKey2.grid(row=1,column=0)
labelDelay.grid(row=2, column=0)

entryKey1.grid(row=0,column=1)
entryKey2.grid(row=1,column=1)
entryKey3.grid(row=2,column=1)

startButton.grid(row=3, pady=10,)

entryKey1.insert(0, "~")
entryKey2.insert(0, "z")
entryKey3.insert(0, "1000")

root.mainloop()
