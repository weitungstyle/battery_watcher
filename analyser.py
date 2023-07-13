from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt


class Analyser:
    def __init__(self, date_start, date_end) -> None:
        self.date_start = date_start.date()
        self.date_end = date_end.date()

    def load_data(self):
        file_list = []
        if self.date_start > self.date_end:
            raise ValueError("Date start must be before date end")
        elif self.date_start == self.date_end:
            file_list.append(f"records/{self.date_start}.csv")
        else:
            for i in range((self.date_end - self.date_start).days):
                file_list.append(f"records/{self.date_start+timedelta(days=i)}.csv")
        try:
            data = pandas.concat(
                map(pandas.read_csv, file_list), axis=0, ignore_index=True
            )
        except FileNotFoundError:
            print("No data found")
        return data

    def draw_chart(self):
        pass


a = Analyser(datetime(2023, 7, 12), datetime(2023, 7, 12))
s = a.load_data()
print(s)
