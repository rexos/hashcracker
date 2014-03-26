from Tkinter import *
from tkFileDialog import askopenfilename

filename = ''
def get_file():
    # trying Tkinter as GUI
    filename = askopenfilename()
    file.insert(0, filename)

window = Tk() # create the window
window.title('Hashcracker')
wrapper = Frame( window ) # create a big frame inside of it
hashframe = Frame(wrapper) # a smaller frame inside wrapper
Label( hashframe, text="Hash: " ).pack(side=LEFT)
hash = Entry(hashframe)
hash.pack() # pack actually saves an element on a frame or window
hashframe.pack(fill=X)
fileframe = Frame(wrapper)
Label( fileframe, text="Wordlist: " ).pack(side=LEFT)
file = Entry(fileframe)
file.insert(0, filename)
file.pack()
Button(fileframe, text="Choose", command=get_file).pack()
fileframe.pack(fill=X)
wrapper.pack(fill=X)
window.minsize(300,300)
window.mainloop() # show the window
