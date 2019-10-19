# -*- coding: utf-8 -*-
"""Gomez_Skill6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qdSfwtlzT-VRIDkpBXu7k9bSf0rrcWQh
"""

import pandas as pd

url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"
header_csv= ["CountryName", "CountryCode","Year","GDP"]

pima = pd.read_csv(url, header=None,names=header_csv, skiprows=1)
# header=None, names=header_csv,skiprows=1

print(pima.shape)
pima.head()

us = pima[pima.CountryName == 'United States']
ch = pima[pima.CountryName == 'China']
eu = pima[pima.CountryName == 'European Union']

from matplotlib import pyplot as plt

plt.plot( us.Year, us.GDP/ 10**9,'o')
plt.plot( ch.Year, ch.GDP/ 10**9,'-')
plt.plot( eu.Year, eu.GDP/ 10**9,'--')

#plt.plot(pima.column_a, sample_data.column_c)
plt.title("Gregorio's GDP Plot")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend(["United States", "China", "E.U."])
plt.show()



