import json
from datetime import datetime

import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
from matplotlib import dates

with open('results.log') as f:
    df = pd.DataFrame(json.loads(line) for line in f)

print df.head()

print df['download'].mean()

df['timestamp'] = [datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ') for dt in df['timestamp']]

axes = df.plot(x='timestamp', y='download', rot=15)
# axes.xaxis.set_major_locator(dates.WeekdayLocator())
# 2017-06-16T20:15:11.416971Z
# print datetime.strptime(df.timestamp[0], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')

# quit()
# axes.set_xticklabels([datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d') for dt in df.timestamp])
plt.show()