import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data1 = pd.read_csv('uber.csv')
print(data1.describe())
sns.scatterplot(x="Lon", y="Lat", data=data1)
plt.title("Uber Ride Locations")
plt.show()


