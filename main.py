# Main Python file
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# PS4 Dataset
df = pd.read_csv('vgamesales.csv')

# Getting information on the dataset using df.info

# Getting the data set has null values
# Getting the total null values of the dataset 
null_percentage = len(df[df['Year_of_Release'].isnull() | df['Publisher'].isnull()])/ len(df)*100
print(null_percentage)


# The total null values are 1.8% of the whole data set
# Dropping the null data using df.dropna
df.dropna(inplace = True)

# plat = df[df["Platform"] == "X360"]
# plat['Global_Sales'].sum()
wii = None
ps2 = None
ps3 = None
ps4 = None
Ds = None
xbx = None

top_platforms = []
global_all_sales = []
df_platforms = df['Platform'].unique().tolist()
for i in (df_platforms):
    if i == "Wii":
        plat = df[df["Platform"] == i]
        wii = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
    elif i == "DS":
        plat = df[df["Platform"] == i]
        Ds = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
    elif i == "PS2":
        plat = df[df["Platform"] == i]
        ps2 = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
    elif i == "PS3":
        plat = df[df["Platform"] == i]
        ps3 = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
    elif i == "PS4":
        plat = df[df["Platform"] == i]
        ps4 = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
    elif i == "X360":
        plat = df[df["Platform"] == i]
        xbx = plat['JP_Sales'].sum()
        top_platforms.append(i)
        global_all_sales.append(plat['JP_Sales'].sum())
        
explode = [0.1,0.1,0.1,0.1,0.1,0.1]
colors = ['lightseagreen', 'mediumpurple', 'aquamarine', 'lawngreen', 'lightsalmon', 'turquoise', 'cornflowerblue']
def platform_pie(title, sales):
  plt.title(title)
  plt.pie(sales,
         labels = top_platforms,
         wedgeprops=dict(width=0.2),
         shadow = True,
         colors = colors,
         explode = explode,
         startangle = 90,
         autopct='%1.1f%%');
platform_pie("Japan Sales", global_all_sales)

glob_total = df["EU_Sales"].sum()
print(glob_total)








