from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
# Removes the blurry text #


def submit():
    input = entry.get()
    print(input)
def temp_text(e):
    entry.delete(0,"end")

window = Tk()
window.geometry("700x250")
window.config(background="black")
submit = Button(window, text="gönder",command=submit)
submit.pack(side = BOTTOM)
entry = Entry()
entry.config(font=('Times New Roman', 10))
#entry.config(fg='white')
#entry.config(bg='black')
entry.insert(0,'Lütfen beğendiğiniz film türünü giriniz')
entry.config(width=100)
entry.pack()
entry.bind("<FocusIn>", temp_text)
window.mainloop()
