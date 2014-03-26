from Tkinter import *
from tkFileDialog import askopenfilename


class Window():

    def __init__(self):
        self.filename = ''
        self.root = Tk() # create the window
        self.root.title('Hashcracker')
        wrapper = Frame( self.root ) # create a big frame inside of it
        hashframe = Frame(wrapper) # a smaller frame inside wrapper
        Label( hashframe, text="Hash:      " ).pack(side=LEFT)
        self.hash = Entry(hashframe)
        self.hash.pack(side=LEFT) # pack actually saves an element on a frame or window
        hashframe.pack(fill=X)
        fileframe = Frame(wrapper)
        Label( fileframe, text="Wordlist: " ).pack(side=LEFT)
        self.file = Entry(fileframe) # will contain the path to the wordlist
        self.file.pack(side=LEFT)
        Button(fileframe, text="..", command=self.__get_file).pack(side=LEFT)
        fileframe.pack(fill=X)
        startframe = Frame(wrapper)
        Button(startframe, text="Look Up").pack()
        startframe.pack(fill=X)
        wrapper.pack(fill=X)
        self.root.minsize(300,300) # set the window minimum size

    def show(self):
        self.root.mainloop()

    def __get_file(self):
        self.filename = askopenfilename()
        self.file.delete( 0, END )
        self.file.insert(0, self.filename)

def main():
    w = Window()
    w.show()

if __name__ == '__main__':
    main()
