from tkinter import *

root = Tk()
root.title("Mile to Km Converter")

def calculate():
    miles = float(mile_entry.get())
    km = miles * 1.609
    print(km)
    num_label.config(text=f"{round(km,2)}")



mile_entry = Entry(root,width=25)
mile_entry.grid(row=0,column=1,pady=15,padx=15)
mile_entry.focus()

mile_label = Label(root,text="Miles")
mile_label.grid(row=0,column=2)

equal_label = Label(root,text="Is Equal To")
equal_label.grid(row=1,column=0)

num_label = Label(root,text="0")
num_label.grid(row=1,column=1)

km_label = Label(root,text="Km")
km_label.grid(row=1,column=2)

calculate_btn = Button(root,text="Calculate",command=calculate)
calculate_btn.grid(row=2,column=1)



root.mainloop()