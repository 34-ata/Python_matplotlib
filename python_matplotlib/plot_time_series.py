import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use("fivethirtyeight")

data = pd.read_csv("data4.csv")

data["Date"] = pd.to_datetime(data["Date"])
data.sort_values("Date", inplace=True)

price_date = data["Date"]
price_close = data["Close"]

plt.plot_date(price_date, price_close, linestyle="solid", linewidth=1.15)

plt.gcf().autofmt_xdate()

plt.title("Bitcoin Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.tight_layout()
plt.show()