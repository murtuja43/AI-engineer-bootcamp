# pandas
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [23, 25, 22, 24],
    "score": [85, 90, 78, 92],
    "country": ["USA", "UK", "USA", "Canada"]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.tail())

print(df["name"])
print(df[["name", "score"]])

print(df.iloc[0])
print(df.iloc[0:2])

print(df.loc[df["age"] > 23])

print(df.dtypes)

df["passed"] = df["score"] > 80
print(df)

grouped = df.groupby("country").mean(numeric_only=True)
print(grouped)

sorted_df = df.sort_values(by="score", ascending=False)
print(sorted_df)

# numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

zeros = np.zeros((3,3))
print(zeros)

ones = np.ones((2,4))
print(ones)

range_arr = np.arange(0, 10, 2)
print(range_arr)

linspace_arr = np.linspace(0, 1, 5)
print(linspace_arr)

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix)
print(matrix.shape)
print(matrix[0])
print(matrix[:,1])

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)

print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

# broadcasting
a = np.array([1,2,3])
b = 10

print(a + b)

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

vector = np.array([10,20,30])

print(matrix + vector)

# vectorization
numbers = np.arange(1, 11)
squared = numbers ** 2
print(squared)

# matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.bar(["A","B","C"], [5,7,3])
plt.title("Bar Chart")
plt.show()

data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()

# seaborn
import seaborn as sns

tips = sns.load_dataset("tips")

sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

sns.heatmap(tips.corr(numeric_only=True), annot=True)
plt.show()