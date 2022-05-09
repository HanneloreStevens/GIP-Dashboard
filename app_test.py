import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('C:/Users/hannelores409/OneDrive - Campus Sint-Ursula Lier/schooljaar 2021-2022/informatica/trimester 2/module and packiging/matplotlib/data/DW.csv',sep = ',')
ax=plt.gca()
df.plot(x='DW2020',y='cijfer2020',ax=ax, color='red')
df.plot(x='DW2021',y='cijfer2021',ax=ax, color='orange')


#legende
plt.legend()

# toon grafiek.
plt.show()


#DW2021,cijfer2021,DW2020,cijfer2020
