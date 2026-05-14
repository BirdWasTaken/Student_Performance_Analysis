import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Loading Students Performance Dataset
df = pd.read_csv("StudentsPerformance.csv")
print(df.head())

#Checking dataset size
print(df.shape)

#Showing column names
print(df.columns)

#Checking datatypes and null values
print(df.info())
print(df.isnull().sum())

#Showing Statistical summary
print(df.describe())

#Average in Math Score
print(df["math score"].mean())

#Average male and female math score
print(df.groupby("gender")["math score"].mean())

#Average math scores for different test preparation course
print(df.groupby("test preparation course")["math score"].mean())

#Average reading scores for different lunch types
print(df.groupby("lunch")["reading score"].mean())

#Histogram for Math Score
plt.hist(df["math score"])
plt.show()

#Boxplot for math scores of male and female
sns.boxplot(x="gender", y="math score", data=df)
plt.show()

#Corelation between Math score, Reading score and Writing score
sns.heatmap(df.select_dtypes(include="number").corr(),annot= True)
plt.show()

#Scatter plot between Math score and Reading score
plt.scatter(df["math score"], df["reading score"])
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()

#Bar Graph for Average math score by gender
df.groupby("gender")["math score"].mean().plot(kind="bar")
plt.show()