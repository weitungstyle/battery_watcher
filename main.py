from tkinter import *
from tkinter.ttk import Separator


window = Tk()
window.title("Battery Watcher")
window.config(padx=20, pady=20)

# Labels
battery_high_label = Label(text="Battery Upper Limit:")
battery_high_label.grid(column=0, row=0)

percentage_high_label = Label(text="%")
percentage_high_label.grid(column=2, row=0, sticky=W)

battery_low_label = Label(text="Battery Lower Limit:")
battery_low_label.grid(column=0, row=1)

percentage_low_label = Label(text="%")
percentage_low_label.grid(column=2, row=1, sticky=W)

record_from_label = Label(text="Record Date From:")
record_from_label.grid(column=0, row=3, sticky=E)

record_to_label = Label(text="Record Date To:")
record_to_label.grid(column=0, row=4, sticky=E)

# Entries
battery_high_entry = Entry(width=5)
battery_high_entry.grid(column=1, row=0)

battery_low_entry = Entry(width=5)
battery_low_entry.grid(column=1, row=1)

# Spinbox
record_from_year_entry = Entry(width=5)
record_from_year_entry.grid(column=1, row=3)

record_from_month_entry = Entry(width=3)
record_from_month_entry.grid(column=2, row=3)

record_from_day_entry = Entry(width=3)
record_from_day_entry.grid(column=3, row=3)

record_to_year_entry = Entry(width=5)
record_to_year_entry.grid(column=1, row=4)

record_to_month_entry = Entry(width=3)
record_to_month_entry.grid(column=2, row=4)

record_to_day_entry = Entry(width=3)
record_to_day_entry.grid(column=3, row=4)

# Seperators
sep = Separator(orient=HORIZONTAL)
sep.grid(column=0, row=2, columnspan=5, sticky=EW, pady=10)

# Buttons
calculate_button = Button(text="Inquire")
calculate_button.grid(column=4, row=5)

window.mainloop()
