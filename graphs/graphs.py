import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# make a list of years increase 1 year at a time from 1971 till this year.
processor_transistor = {1971: 2250, }

x = [datetime.datetime + datetime.timedelta(minutes=i) for i in range(12)]
y = [i + random.gauss(0, 1) for i, _ in enumerate(x)]

# plot
plt.plot([], [])
plt.scatter(x, y)

# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
plt.close()
