from datetime import datetime
import psutil
import notifypy


class Monitor:
    def __init__(self):
        self.date = datetime.date(datetime.now())
        self.battery = psutil.sensors_battery()
        self.charging = self.battery.power_plugged
        self.percent = self.battery.percent
        self.__str__ = f"The battery is {self.percent}% charged."

    def check_battery(self, lower_limit=40, upper_limit=80):
        if self.percent < lower_limit and not self.charging:
            self.notify(
                message=f"The battery is lower than {lower_limit}%!\nFind a charger ASAP!"
            )
        elif self.percent > upper_limit and self.charging:
            self.notify(
                message=f"The battery is higher than {upper_limit}%!\nPlease removed the charger!"
            )

    def notify(self, message, title="Battery Notification"):
        notifypy.Notify().send(title=title, message=message)

    def record(self):
        with open(f"records/{self.date}.csv", "a") as f:
            f.write(
                f"{datetime.time(datetime.now())}, {self.charging}, {self.percent}%\n"
            )
