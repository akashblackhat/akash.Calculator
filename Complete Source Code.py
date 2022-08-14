from tkinter import *
""" developer Akash Ram"""
""" android & pc game developer """
""" AKASHRAM8090AS@GMAIL.COM"""

def fCalc(src, side):
    appObj = Frame(src, borderwidth=4, bd=2, bg="#cccccc")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj


def button(src, side, text, command=None):
    appObj = Button(src, text=text, command=command)
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj


class app(Frame):
    def __init__(self, root=Tk(), width=364, height=425):
        Frame.__init__(self)
        self.option_add("*Font", 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Developer Akash Ram (-_-)akashram8090as@gmail.com")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display, state=DISABLED, justify='right', bd=20, bg="silver").pack(side=TOP, expand=YES,
                                                                                              fill=BOTH)
        clrChar = "Clear"
        button(self, TOP, clrChar, lambda appObj=display, i=clrChar: appObj.set(''))

        for btnNum in ("789/", "456*", "123-", "0.+"):

            FunctionNum = fCalc(self, TOP)
            for fEquals in btnNum:
                button(FunctionNum, LEFT, fEquals,
                       lambda appObj=display, i=fEquals: appObj.set(appObj.get() + i))
                EqualsButton = fCalc(self, TOP)

        for fEquals in "=":
            if fEquals == "=":
                btnEquals = button(EqualsButton, LEFT, fEquals)
                btnEquals.bind('<ButtonRelease-1>',
                               lambda e, s=self, appObj=display: s.result(appObj), "+")
            else:
                btnEquals = button(EqualsButton, LEFT, fEquals,
                                   lambda appObj=display, s=" %s " % fEquals: appObj.set(appObj.get() + s))

    def result(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("UNDEFINED")


if __name__ == '__main__':
    app().mainloop()