import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(9, 4))

plt.plot(df["Date"], df["ALL"], label="ALL", color="y")
plt.plot(df["Date"], df["Hokkaido"], label="Hokkaido", color="b")
plt.plot(df["Date"], df["Gifu"], label="Gifu", color="r")
plt.plot(df["Date"], df["Okinawa"], label="Okinawa")

plt.title("全国-コロナ感染者数")
plt.xlabel("日付")
plt.ylabel("感染者数")

plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.show()
