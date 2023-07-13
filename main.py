from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox
from tkinter import IntVar
from battery_monitor import Monitor
from analyser import Analyser
from datetime import datetime
import time

lower_limit = 40
upper_limit = 80


def setting_limit():
    global upper_limit
    global lower_limit
    u = int(battery_high_entry.get())
    l = int(battery_low_entry.get())
    if u > 100 or u < 0 or l > 100 or l < 0:
        messagebox.showerror(title="Battery Watcher", message="Invalid Input!")
    elif u < l:
        messagebox.showerror(title="Battery Watcher", message="Invalid Input!")
    else:
        upper_limit = u
        lower_limit = l
    messagebox.showinfo(title="Battery Watcher", message="Setting Done!")


def check_battery_status():
    battery_monitor = Monitor()
    battery_monitor.check_battery(lower_limit, upper_limit)
    battery_monitor.record()


def update_battery_status():
    check_battery_status()
    window.after(60000, update_battery_status)


def show_chart():
    date_start = datetime(
        int(from_year.get()), int(from_month.get()), int(from_day.get())
    )
    date_end = datetime(int(to_year.get()), int(to_month.get()), int(to_day.get()))
    analyser = Analyser(date_start, date_end)
    analyser.draw_chart(analyser.load_data())


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
record_from_label.grid(column=0, row=5, sticky=E)

record_to_label = Label(text="Record Date To:")
record_to_label.grid(column=0, row=6, sticky=E)

bg_run_label = Label(text="After Closing Window:")
bg_run_label.grid(column=0, row=3, sticky=E)

# Entries
battery_high_entry = Entry(width=5, justify='right')
battery_high_entry.grid(column=1, row=0)
battery_high_entry.insert(0, upper_limit)

battery_low_entry = Entry(width=5, justify='right')
battery_low_entry.grid(column=1, row=1)
battery_low_entry.insert(0, lower_limit)


# Spinbox - Year
from_year = StringVar()
from_year.set(time.strftime("%Y"))
record_from_year_entry = Spinbox(
    from_=2020, to=2050, textvariable=from_year, width=4, justify='right'
)
record_from_year_entry.grid(column=1, row=5)

to_year = StringVar()
to_year.set(time.strftime("%Y"))
record_to_year_entry = Spinbox(
    from_=2020, to=2050, textvariable=to_year, width=4, justify='right'
)
record_to_year_entry.grid(column=1, row=6)


# Spinbox - Month
from_month = StringVar()
from_month.set(time.strftime("%m"))
record_from_month_entry = Spinbox(
    from_=1, to=12, textvariable=from_month, width=2, justify='right'
)
record_from_month_entry.grid(column=2, row=5)

to_month = StringVar()
to_month.set(time.strftime("%m"))
record_to_month_entry = Spinbox(
    from_=1, to=12, textvariable=to_month, width=2, justify='right'
)
record_to_month_entry.grid(column=2, row=6)


# Spinbox - Day
from_day = StringVar()
from_day.set(time.strftime("%d"))
record_from_day_entry = Spinbox(
    from_=1, to=31, textvariable=from_day, width=2, justify='right'
)
record_from_day_entry.grid(column=3, row=5)

to_day = StringVar()
to_day.set(time.strftime("%d"))
record_to_day_entry = Spinbox(
    from_=1, to=31, textvariable=to_day, width=2, justify='right'
)
record_to_day_entry.grid(column=3, row=6)


# Seperators
sep = Separator(orient=HORIZONTAL)
sep.grid(column=0, row=2, columnspan=5, sticky=EW, pady=10)

sep2 = Separator(orient=HORIZONTAL)
sep2.grid(column=0, row=4, columnspan=5, sticky=EW, pady=10)

# Buttons
set_button = Button(text="Set", command=setting_limit)
set_button.grid(column=4, row=1)

calculate_button = Button(text="Inquire", command=show_chart)
calculate_button.grid(column=4, row=7)

# Radiobuttons
bg_run = IntVar()
radiobutton1 = Radiobutton(text="Keep Notice", value=0, variable=bg_run)
radiobutton2 = Radiobutton(text="Turn Off", value=1, variable=bg_run)
radiobutton1.grid(column=1, row=3, columnspan=2, sticky=W)
radiobutton2.grid(column=3, row=3, columnspan=2, sticky=W)

window.after(0, update_battery_status)

window.mainloop()

while not bg_run.get():
    time.sleep(60)
    check_battery_status()
