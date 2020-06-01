## 2. Introduction To The Data ##

import pandas as pd
unrate=pd.read_csv("unrate.csv")
unrate["DATE"]=pd.to_datetime(unrate["DATE"])
unrate.head(12)


## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

unrate_1948=unrate[:12]
plt.plot(unrate_1948["DATE"],unrate_1948["VALUE"])
plt.show()

## 8. Fixing Axis Ticks ##

import pandas as pd
import matplotlib.pyplot as plt

unrate_1948=unrate[:12]
plt.plot(unrate_1948["DATE"],unrate_1948["VALUE"])
plt.xticks(rotation=90)
plt.show()

## 9. Adding Axis Labels And A Title ##

%matplotlib inline
unrate_1948=unrate[:12]
plt.plot(unrate_1948["DATE"],unrate_1948["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()