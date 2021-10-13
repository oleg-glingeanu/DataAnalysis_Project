# importing needed libraries
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('games_data.csv')

platform_index_list = data['Platform'].tolist()
platforms = list(dict.fromkeys(platform_index_list))
sales_index_list = data['Global_Sales'].tolist()
print(platforms)

wii_total = 0
pc_total = 0
ps2_total = 0
iteration = 0

for key in platform_index_list:
    if key == "Wii":
        wii_total += sales_index_list[iteration]
    elif key == "PC":
        pc_total += sales_index_list[iteration]
    elif key == "PS2":
        ps2_total += sales_index_list[iteration]
    iteration += 1


print(wii_total)
print(pc_total)
print(ps2_total)

cut = [wii_total, pc_total, ps2_total]
myLabels = ["Wii", 'Pc', 'Ps2']
my_explode = [0.3, 0, 0]

plt.pie(cut, labels=myLabels, explode=my_explode, shadow=True)
plt.show()
