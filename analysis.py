import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_csv("../data/fashion_sales.csv", low_memory=False)

# CLEAN COLUMNS
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# CONVERT DATA TYPES
df['selling_price'] = pd.to_numeric(df['selling_price'], errors='coerce')
df['mrp'] = pd.to_numeric(df['mrp'], errors='coerce')
df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')

# REMOVE DUPLICATES
df.drop_duplicates(inplace=True)

# REMOVE NULL VALUES
df.dropna(subset=['selling_price'], inplace=True)

# BASIC ANALYSIS
print("AVERAGE SELLING PRICE")
print(df['selling_price'].mean())

print("\nMAXIMUM SELLING PRICE")
print(df['selling_price'].max())

print("\nMINIMUM SELLING PRICE")
print(df['selling_price'].min())

# TOP BRANDS
top_brands = df['brand'].value_counts().head(10)

print("\nTOP 10 BRANDS")
print(top_brands)

# TOP BRANDS CHART
plt.figure(figsize=(10,5))

top_brands.plot(kind='bar')

plt.title("Top 10 Brands")
plt.xlabel("Brands")
plt.ylabel("Count")

plt.savefig("../images/top_brands_chart.png")

print("\nTOP BRANDS CHART SAVED SUCCESSFULLY")

# PRICE DISTRIBUTION CHART
plt.figure(figsize=(10,5))

df['selling_price'].plot(kind='hist', bins=30)

plt.title("Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")

plt.savefig("../images/price_distribution_chart.png")

print("PRICE DISTRIBUTION CHART SAVED SUCCESSFULLY")