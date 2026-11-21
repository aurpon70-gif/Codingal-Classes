import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Sample data for 6 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
income = np.array([3000, 3200, 3100, 3300, 3500, 3600])
expenses = np.array([2500, 2700, 2400, 3000, 2800, 2600])
savings = income - expenses

# Category breakdown data for grouped bar chart
categories = ['Food', 'Rent', 'Utilities', 'Entertainment']
cat_data_month1 = [600, 1200, 300, 400]
cat_data_month2 = [650, 1200, 350, 500]

# 1. Create a 2x2 multi-panel figure using plt.subplots()
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Personal Finance Visualiser Dashboard', fontsize=16, fontweight='bold')

# --- Top-Left: Line charts for income and expense trends ---
axs[0, 0].plot(months, income, marker='o', color='green', linewidth=2, label='Income')
axs[0, 0].plot(months, expenses, marker='s', color='red', linewidth=2, label='Expenses')
axs[0, 0].set_title('Income & Expense Trends')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Amount ($)')
axs[0, 0].legend()
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# --- Top-Right: Bar chart with conditional green/red colouring for savings ---
bar_colors = ['green' if s >= 0 else 'red' for s in savings]
axs[0, 1].bar(months, savings, color=bar_colors)
axs[0, 1].set_title('Monthly Net Savings')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Savings ($)')
axs[0, 1].axhline(0, color='black', linewidth=0.8, linestyle='--')
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# --- Bottom-Left: Grouped bar chart for expense categories ---
x = np.arange(len(categories))
width = 0.35
axs[1, 0].bar(x - width/2, cat_data_month1, width, label='Month 1', color='skyblue')
axs[1, 0].bar(x + width/2, cat_data_month2, width, label='Month 2', color='orange')
axs[1, 0].set_title('Expense Category Comparison')
axs[1, 0].set_xlabel('Category')
axs[1, 0].set_ylabel('Amount ($)')
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(categories)
axs[1, 0].legend()
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# --- Bottom-Right: Area chart using fill_between() for cumulative savings ---
cumulative_savings = np.cumsum(savings)
axs[1, 1].plot(months, cumulative_savings, color='purple', linewidth=2, marker='o')
axs[1, 1].fill_between(months, cumulative_savings, color='purple', alpha=0.3)
axs[1, 1].set_title('Cumulative Savings (Area Chart)')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Cumulative Amount ($)')
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# Adjust layout for neat spacing
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# 7. Save the figure using savefig()
plt.savefig('personal_finance_dashboard.png', dpi=300)
print("Figure saved successfully as 'personal_finance_dashboard.png'")

# Display the plot
plt.show()