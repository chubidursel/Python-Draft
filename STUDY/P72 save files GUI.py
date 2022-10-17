from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\User\\Desktop",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    #if we stared process of saveing file, but exit out of the window before
    #So there is no exeption that we encounter (сталкиваемся)
    if file is None:
        return

    filetext = str(text.get(1.0, END)) # 1.0 > starting index | END > ending index || text.get > gt text from text are
    #filetext = input("Enter some text: ") #if u want to use console window below to write the text
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="save",command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
