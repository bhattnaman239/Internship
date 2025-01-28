#Pandas
print("\nPANDAS\n")
import pandas as pd
import numpy as np
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

# #Indexing and Slicing
print("\nINDEXING AND SLICING\n")
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Dexter', 'age': 30},
]
df = pd.DataFrame(data)
print(df['name'].values)
print(df['name'][0])
print(df['name'][1:3].values)

# #Filtering
print("\nFILTERING\n")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dexter'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
print(df[df['Age'] > 30])

#Sorting
print("\nSORTING\n")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dexter'], 'Age': [235, 930, 135, 440]}
df = pd.DataFrame(data)
print(df.sort_values(by='Age'))


#Grouping
print("\nGROUPING\n")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dexter'], 'Age': [25, 30, 25, 40]}
df = pd.DataFrame(data)
grouped = df.groupby('Age')
print("Grouping by Age:",grouped.groups)

#Aggregation
print("\nAGGREGATION\n")
print("Mean: ",df['Age'].mean())
print("Sum: ",df['Age'].sum())
print("Count: ",df['Name'].count())
a=df.describe()
print(a)


#Reading and Writing CSV
print("\nREADING AND WRITING CSV\n")
df.to_csv("data.csv", index=False)
print(pd.read_csv("data.csv"))

#Reading and Writing Excel
print("\nREADING AND WRITING EXCEL\n")
df.to_excel("data.xlsx", index=False)
print(pd.read_excel("data.xlsx"))


#Merging
print("\nMERGING\n")
data1 = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
data2 = {'Name': ['Charlie', 'Dexter'], 'Age': [35, 40]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(pd.concat([df1, df2]))

print("\nJOINING\n")
data1 = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
data2 = {'Name': ['Alice', 'Bob'], 'City': ['New York', 'Los Angeles']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(pd.merge(df1, df2, on='Name'))

#Missing Data
print("\nMISSING DATA\n")
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dexter'], 'Age': [25, 30, None, 40]}
df = pd.DataFrame(data)
print("Filling null with 0:\n",df.fillna(0))
print("Dropping Null value:\n",df.dropna())
# print(df.isnull())
print("Counts null value:\n",df.isnull().sum())

#Time Series
print("\nTIME SERIES\n")
dates = pd.date_range('20220101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4),columns=list('ABCD'), index=dates)
print(df)
print(df['2022-01-02':'2022-01-04'])


#Plotting
print("\nPLOTTING\n")
import matplotlib.pyplot as plt
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dexter'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
df.plot(kind='bar', x='Name', y='Age')
plt.show()
df.plot(kind='scatter', x='Name', y='Age')
plt.show()

df.plot(kind='pie', y='Age', labels=df['Name'], autopct='%1.f%%', legend=True)
plt.title("Age Distribution Pie Chart")
plt.show()