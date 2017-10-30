import tkinter
import sys

class HelloWorld(tkinter,frame):
        def __init__(self, root):
            self.pack()
            h1 = tkinter.Button(self, text = "Hello World:", command = self.hello)
            h2 = tkinter.Button(self, text = "Bye", command = self.bye)

            h1.pack(side='left')
            h2.pack(side='left')

        def hello(self):
                print('hello')

        def bye(self):
                sys.exit(0)

        def main():
            root = tkinter.tk()
            App = HelloWorld(root)
            App.mainloop()

        if __name__ == '__main__':
            main()
