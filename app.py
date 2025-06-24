import pandas as pd

# Load Titanic dataset (update path if needed)
df = pd.read_csv("titanic-Dataset.csv")  # or the path where you've downloaded the dataset

# Basic info
print(df.info())

# Descriptive stats
print(df.describe(include='all'))

# Null value check
print(df.isnull().sum())

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of numeric features
df.hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plt.show()

# Boxplot for fare
plt.figure(figsize=(8, 4))
sns.boxplot(x='Fare', data=df)
plt.title('Boxplot of Fare')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# Pairplot (only for selected features to avoid clutter)
sns.pairplot(df[['Age', 'Fare', 'Pclass', 'Survived']], hue='Survived')
plt.show()

# Count plot of survival by gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title("Survival Count by Gender")
plt.show()

# Age distribution by survival
sns.kdeplot(data=df[df['Survived'] == 1]['Age'], label='Survived', fill=True)
sns.kdeplot(data=df[df['Survived'] == 0]['Age'], label='Not Survived', fill=True)
plt.title("Age Distribution by Survival Status")
plt.legend()
plt.show()

import plotly.express as px

# Interactive boxplot
fig = px.box(df, x='Pclass', y='Fare', color='Survived', points='all')
fig.show()
