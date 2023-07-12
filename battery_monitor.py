from datetime import datetime
import psutil
import notifypy


class Monitor:
    def __init__(self):
        self.now = datetime.now()
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
        notification = notifypy.Notify()
        notification.title = title
        notification.message = message

        notification.send()

    def record(self):
        with open(f"records/{self.now.date()}.csv", "a") as f:
            f.write(f"{self.now.strftime('%H:%M')}, {self.charging}, {self.percent}%\n")
