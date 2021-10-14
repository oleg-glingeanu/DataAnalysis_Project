# importing needed libraries
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('PS4_GamesSales')

platform_index_list = data['North America'].tolist()
platforms = list(dict.fromkeys(platform_index_list))
sales_index_list = data['Global_Sales'].tolist()
print(platforms)


cut = [Europe, NorthAmerica, Japan]
myLabels = ["Wii", 'Pc', 'Ps2']
my_explode = [0.3, 0, 0]

plt.pie(cut, labels=myLabels, explode=my_explode, shadow=True)
plt.show()
