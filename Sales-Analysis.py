import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SuperMarket_Analysis.csv")  # Adjust path if needed

# Top 5 Products by Total Sales
product_sales = df.groupby('Product_line')['Sales'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=product_sales.index, y=product_sales.values, palette='husl', width=0.5)
plt.title('Top 5 Products by Total Sales')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Revenue Distribution by City
revenue_by_city = df.groupby('City')['Sales'].sum()
plt.pie(revenue_by_city, labels=revenue_by_city.index, autopct='%1.1f%%')
plt.title('Revenue Distribution by City')
plt.tight_layout()
plt.show()

# Most Popular Payment Method
sns.countplot(x='Payment', data=df, order=df['Payment'].value_counts().index, width=0.5, palette='husl')
plt.title('Most Popular Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Average Rating by Gender
avg_rating = df.groupby('Gender')['Rating'].mean()
sns.barplot(x=avg_rating.index, y=avg_rating.values, palette='husl')
plt.title('Average Rating by Gender')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show()

# Monthly Revenue Trend
df['Month'] = pd.to_datetime(df['Date'], dayfirst=False, errors='coerce').dt.month
monthly_revenue = df.groupby('Month')['Sales'].sum()
sns.lineplot(x=monthly_revenue.index, y=monthly_revenue.values, marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(monthly_revenue.index)
plt.grid(True)
plt.tight_layout()
plt.show()

# Average Unit Price by Product Line
avg_unit_price = df.groupby('Product_line')['Unit_price'].mean().sort_values(ascending=False)
sns.barplot(x=avg_unit_price.index, y=avg_unit_price.values, width=0.5, palette='husl')
plt.title('Average Unit Price by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Avg Unit Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
