import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../dataset/sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Create Month-Year column
df["Month"] = df["Date"].dt.strftime("%Y-%m")

# -----------------------------
# Basic Insights
# -----------------------------
print("Total Sales:", df["Total Amount"].sum())
print("Average Sales:", df["Total Amount"].mean())
print("Highest Sale:", df["Total Amount"].max())

# -----------------------------
# Monthly Sales Trend
# -----------------------------
monthly_sales = (
    df.groupby("Month")["Total Amount"]
    .sum()
)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("../outputs/monthly_sales.png")
plt.show()

# -----------------------------
# Category Sales
# -----------------------------
category_sales = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../outputs/category_sales.png")
plt.show()

# -----------------------------
# Gender Sales
# -----------------------------
gender_sales = (
    df.groupby("Gender")["Total Amount"]
    .sum()
)

plt.figure(figsize=(6,6))
gender_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales by Gender")
plt.ylabel("")

plt.tight_layout()
plt.savefig("../outputs/gender_sales.png")
plt.show()

# -----------------------------
# Top 10 Customers
# -----------------------------
top_customers = (
    df.groupby("Customer ID")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar")

plt.title("Top 10 Customers")
plt.xlabel("Customer ID")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("../outputs/top_customers.png")
plt.show()

print("Charts saved successfully")