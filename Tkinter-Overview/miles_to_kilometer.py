from tkinter import *

def miles_to_km():
    """ Convert Miles do Kilometers """
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f'{km}')


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width = 7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_input.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
miles_input.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
miles_input.grid(column=1, row=1)

kilometer_label = Label(text="Km")
miles_input.grid(column=2, row=1)

calculater_button = Button(text="Calculate", command = miles_to_km)
miles_input.grid(column=1, row=2)
