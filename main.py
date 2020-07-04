from tkinter import *
from bookDownloader import bookDownloader
from bookDescription import bookDescription





#important stuff
window = Tk()
window.title("InstaBook")
window.configure(background = "black")
window.iconbitmap(default = "bookIcon.ico")
window.geometry("500x500")


#logo
image = PhotoImage(file = "instabook logo.png")
logo = Label(image = image, background = "black")
logo.pack()


#book search
bookTitle = Label(window, text = "Book: ", foreground = "white", background = "black", pady = 10)
bookTitle.pack()
bookEntry = Entry(window)
bookEntry.pack()


#author search
author = Label(text = "Author: ", foreground = "white", background = "black", pady = 10)
author.pack()
authorEntry = Entry()
authorEntry.pack()


#word function
def words(string):
    holder = string.split(" ")
    final = ""
    count = 0
    for i in holder:
        final = final + i + " "
        count = count + 1
        if count % 10 == 0:
            final = final + "\n"

    return final

#searching function
def searching():
    find = bookEntry.get() + " " + authorEntry.get()
    bookDownloader(find)

    try:
        description = bookDescription(find)
        summary = Label(window, text = words(description), foreground = "white", background = "black", width = 50, pady = 5)
        summary.pack()
    except:
        summary = Label(window, text = "synopsis not found", foreground="white", background="black", width = 50, pady = 5)
        summary.pack()


#buttons
search = Button(window, text = "search", command = searching)
search.pack(pady = 20)





window.mainloop()