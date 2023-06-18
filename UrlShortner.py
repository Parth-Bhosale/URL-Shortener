from tkinter import *
import pyshorteners

def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)

root = Tk()
root.title("Url shortener")
root.geometry("400x300")
root.resizable(False, False)
root.config(background="cyan")

photo = PhotoImage(file = "D:\\Documents\\DSE\\CodeClause Internship\\Url-Shortner-main\\url.png")
root.iconphoto(False, photo)

url = StringVar()
shorturl = StringVar()

Label(root, text="URL Shortener", bg="#41B3A3",fg="#2C3E50", font="verdana 22 ").place(x=80, y=10)

Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold"
            , padx=2, pady=2).place(x=7, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=7, y=120)

Button(root, text="Convert...", bg="blue", fg="#000", font="verdana 12 "
        , command=convert, relief=GROOVE).place(x=7, y=180)

Label(root, text="Shortened URL", bg="#2C3E50", fg="#EAECEE"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)

root.mainloop()
