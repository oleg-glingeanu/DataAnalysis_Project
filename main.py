# importing needed libraries
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('XboxOne_GameSales.csv', encoding='latin1')

print(data.head())


platform_index_list = data[data["Game"] == "Grand Theft Auto V"]
europe = platform_index_list['Europe'].tolist()
america = platform_index_list['North America'].tolist()
rest_of_world = platform_index_list['Rest of World'].tolist()

cut = [europe[0], america[0], rest_of_world[0]]

print(cut)
myLabels = ["Europe", 'North America', 'Rest of World']
my_explode = [0, 0, 0.3]
plt.pie(cut, labels=myLabels, explode=my_explode, shadow=True)
plt.title("Grand Theft auto V sales")
plt.show()

