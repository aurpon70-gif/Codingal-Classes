import pandas as pd
import numpy as np

# 1. Create a Pandas DataFrame with 60 sales transactions from a list of dictionaries
np.random.seed(42)  # For reproducible random data

stores = ['Store_A', 'Store_B', 'Store_C', 'Store_D']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']

data = {
    'Transaction_ID': range(101, 161),
    'Store': np.random.choice(stores, 60),
    'Category': np.random.choice(categories, 60),
    'Price': np.round(np.random.uniform(10.0, 500.0, 60), 2),
    'Quantity': np.random.randint(1, 10, 60),
    'Discount_Rate': np.random.choice([0.0, 0.05, 0.1, 0.15, 0.2], 60)
}

df = pd.DataFrame(data)

# 2. Add calculated columns using vectorized operations (Revenue, Net_Revenue)
df['Revenue'] = df['Price'] * df['Quantity']
df['Net_Revenue'] = df['Revenue'] * (1 - df['Discount_Rate'])

print("--- First 5 Rows of DataFrame ---")
print(df.head(), "\n")

# 3. Filter rows with boolean conditions (e.g., transactions where Revenue > 500)
high_value_sales = df[df['Revenue'] > 500]
print(f"Number of transactions with Revenue > 500: {len(high_value_sales)}")

# 4. Sort a DataFrame using sort_values() (e.g., sort by Net_Revenue descending)
df_sorted = df.sort_values(by='Net_Revenue', ascending=False)
print("\n--- Top 3 Transactions by Net Revenue ---")
print(df_sorted.head(3), "\n")

# 5. Aggregate data with groupby() and agg() (Total revenue and average quantity per store)
store_performance = df.groupby('Store').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Net_Revenue=('Net_Revenue', 'sum'),
    Avg_Quantity=('Quantity', 'mean')
)
print("--- Store Performance Summary ---")
print(store_performance, "\n")

# 6. Use value_counts() and apply() to derive new insights
print("--- Category Counts ---")
print(df['Category'].value_counts(), "\n")

# Custom function to categorize transaction size based on Net_Revenue
def classify_sale(net_rev):
    if net_rev > 1000:
        return 'Large'
    elif net_rev > 400:
        return 'Medium'
    else:
        return 'Small'

df['Sale_Size'] = df['Net_Revenue'].apply(classify_sale)
print("--- Sample with Custom 'Sale_Size' Column ---")
print(df[['Transaction_ID', 'Net_Revenue', 'Sale_Size']].head(), "\n")

# 7. Use idxmax() to identify the best-performing store by Total Net Revenue
best_store = store_performance['Total_Net_Revenue'].idxmax()
print(f"The best-performing store by Total Net Revenue is: {best_store}")