from tkinter import *
from tkinter.ttk import Separator
from battery_monitor import Monitor
from analyser import Analyser
import time


def check_battery_status():
    upper_limit = int(battery_high_entry.get())
    lower_limit = int(battery_low_entry.get())
    battery_monitor = Monitor()
    battery_monitor.check_battery(lower_limit, upper_limit)
    battery_monitor.record()


def update_battery_status():
    check_battery_status()
    window.after(60000, update_battery_status)


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
battery_high_entry = Entry(width=5, justify='right')
battery_high_entry.grid(column=1, row=0)
battery_high_entry.insert(0, "80")

battery_low_entry = Entry(width=5, justify='right')
battery_low_entry.grid(column=1, row=1)
battery_low_entry.insert(0, "40")


# Spinbox - Year
from_year = StringVar()
from_year.set(time.strftime("%Y"))
record_from_year_entry = Spinbox(
    from_=2020, to=2050, textvariable=from_year, width=4, justify='right'
)
record_from_year_entry.grid(column=1, row=3)

to_year = StringVar()
to_year.set(time.strftime("%Y"))
record_to_year_entry = Spinbox(
    from_=2020, to=2050, textvariable=to_year, width=4, justify='right'
)
record_to_year_entry.grid(column=1, row=4)


# Spinbox - Month
from_month = StringVar()
from_month.set(time.strftime("%m"))
record_from_month_entry = Spinbox(
    from_=1, to=12, textvariable=from_month, width=2, justify='right'
)
record_from_month_entry.grid(column=2, row=3)

to_month = StringVar()
to_month.set(time.strftime("%m"))
record_to_month_entry = Spinbox(
    from_=1, to=12, textvariable=to_month, width=2, justify='right'
)
record_to_month_entry.grid(column=2, row=4)


# Spinbox - Day
from_day = StringVar()
from_day.set(time.strftime("%d"))
record_from_day_entry = Spinbox(
    from_=1, to=31, textvariable=from_day, width=2, justify='right'
)
record_from_day_entry.grid(column=3, row=3)

to_day = StringVar()
to_day.set(time.strftime("%d"))
record_to_day_entry = Spinbox(
    from_=1, to=31, textvariable=to_day, width=2, justify='right'
)
record_to_day_entry.grid(column=3, row=4)


# Seperators
sep = Separator(orient=HORIZONTAL)
sep.grid(column=0, row=2, columnspan=5, sticky=EW, pady=10)

# Buttons
calculate_button = Button(text="Inquire")
calculate_button.grid(column=4, row=5)

window.after(0, update_battery_status)

window.mainloop()
