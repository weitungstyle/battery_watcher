from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Analyser:
    def __init__(self, date_start, date_end) -> None:
        self.date_start = date_start.date()
        self.date_end = date_end.date()

    def load_data(self):
        file_list = []
        if self.date_start > self.date_end:
            raise ValueError("Date start must be before date end")
        elif self.date_start == self.date_end:
            try:
                file = pandas.read_csv(
                    f"records/{self.date_start}.csv",
                    on_bad_lines='skip',
                )
                return file
            except FileNotFoundError:
                print("No data found")

        else:
            for i in range((self.date_end - self.date_start).days):
                try:
                    file = pandas.read_csv(
                        f"records/{self.date_start+timedelta(days=i)}.csv",
                        on_bad_lines='skip',
                    )
                    file_list.append(file)
                except FileNotFoundError:
                    print("No data found")
            data = pandas.concat(file_list, axis=0, ignore_index=True)
            return data

    def draw_chart(self, data):
        data['Time'] = pandas.to_datetime(data['Time'])
        data.set_index('Time', inplace=True)
        chart = data.plot(
            xlabel="Time",
            ylabel="%",
            legend=True,
            kind="line",
        )
        plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=240))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gcf().autofmt_xdate()
        plt.show()
