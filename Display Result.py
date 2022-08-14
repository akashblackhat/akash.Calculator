def result(self, display):
    try:
        display.set(eval(display.get()))
    except:
        display.set("UNDEFINED")