import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Rainfall.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())


# Histograms


df.hist(figsize=(12,8))
plt.tight_layout()
plt.savefig("histograms.png")
print("Histogram created")
plt.close()
 
# Rainfall Count


df["rainfall"].value_counts().plot(kind="bar")

plt.title("Rainfall Distribution")

plt.xlabel("Rainfall")

plt.ylabel("Count")

plt.savefig("rainfall_distribution.png")
print("Rainfall distribution created")
plt.close()


# Correlation Matrix


numeric = df.copy()

numeric["rainfall"] = numeric["rainfall"].map({"yes":1,"no":0})

corr = numeric.corr()

plt.figure(figsize=(8,6))

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)),corr.columns,rotation=90)

plt.yticks(range(len(corr.columns)),corr.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("correlation_matrix.png")
print("Correlation matrix created")
plt.close()