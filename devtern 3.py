import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
data=pd.read_csv('yearly.csv')
plt.figure(figsize=(8,7))
plt.plot(data['year'], data['births'], label=['Moratality Before Handwash'])
plt.plot(data['year'], data['deaths'], label=['Moratality After Handwash'])
plt.title(' Impact Of Handwashing On Mortality Rate')
plt.xlabel('year')
plt.ylabel('Mortality Rate')
plt.legend()
plt.show()
