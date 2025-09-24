# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Iris.csv')

# 1. Species Distribution (Bar Chart)
plt.figure(figsize=(6,4))
sns.countplot(x='Species', data=df)
plt.title('Iris Species Distribution')
plt.show()

# 2. Sepal Length vs Sepal Width (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm', hue='Species', data=df, s=100)
plt.title('Sepal Length vs Sepal Width')
plt.show()

# 3. Petal Length vs Petal Width (Scatter Plot)
plt.figure(figsize=(6,4))
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', hue='Species', data=df, s=100)
plt.title('Petal Length vs Petal Width')
plt.show()

# 4. Pairplot for all features
sns.pairplot(df, hue='Species')
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# 6. Boxplot (Petal Length by Species)
plt.figure(figsize=(6,4))
sns.boxplot(x='Species', y='PetalLengthCm', data=df)
plt.title('Petal Length by Species')
plt.show()
