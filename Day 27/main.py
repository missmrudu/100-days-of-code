from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx = 100, pady = 100)

my_label = Label(text="I am a label",font= ("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text = "Click me", command = button_clicked)
button.grid(column=1, row=1)

new_button = Button(text = "Click me", command = button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width = 10)
input.get()
input.grid(column=3, row=3)












window.mainloop()