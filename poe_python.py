import pandas as pd
import matplotlib.pyplot as plt
import glob

currencyFiles = glob.glob("*.currency.csv")
itemFiles = glob.glob("*.items.csv")
#esult = pd.concat([pd.read_csv(f, sep=";") for f in currencyFiles], ignore_index = True)
#print(result.head(10))
result2 = pd.concat([pd.read_csv(f, sep=";", dtype={"Links": str}) for f in itemFiles], ignore_index = True)
#print(result2[(result2["Name"] == "Cospri's Malice") & (result2["Value"] > 200)])





#harvest_currency = pd.read_csv("C:/Users/user/Desktop/Harvest.2020-06-19.2020-09-14.currency.csv", sep=";", index_col=0, parse_dates=True)
#delirium_currency = pd.read_csv("C:/Users/user/Desktop/Delirium.2020-03-13.2020-06-15.currency.csv", sep=";", index_col=0, parse_dates=True)
#two_currencies = pd.concat([harvest_currency, delirium_currency], axis=0)
#ex = two_currencies[two_currencies["Get"] == "Exalted Orb"]
#c = two_currencies[two_currencies["Get"] == "Chaos Orb"]
#print(ex.describe())
#print(c.agg({'min', 'max', 'median', 'skew', 'mean'}))

#Exalted_orb = harvest_currency[harvest_currency["Get"] =="Exalted Orb"]
#Currency = harvest_currency["Get"]
#print(Currency)
#Exalted_orb.head(10).plot.scatter(x="Date", y="Value")
#axs = Currency.plot.area(figsize=(12, 4), subplots=True)
#plt.show()
#print(harvest_currency["Get" = "Exalted Orb"].plot.scatter(x="Date", y="Value")
#plt.show()