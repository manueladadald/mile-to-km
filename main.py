"""Simple Mile to KM converter, using the tools available on TkInter"""

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

equal = Label(text="is equal to", font=("Arial", 12, "normal"))
equal.grid(column=0, row=1)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

converted = Label(text="0", font=("Arial", 12, "normal"))
converted.grid(column=1, row=1)


def convert():
    to_convert = int(entry.get())
    to_convert *= 1.60943
    converted_km = round(to_convert, 2)
    converted.config(text=converted_km)


calculate = Button(text="Calculate", command=convert)
# button.place(x=0, y=60)
calculate.grid(column=1, row=2)

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)

window.mainloop()
