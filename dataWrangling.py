import sqlite3
import pandas as pd

# Load CSV into a DataFrame
df = pd.read_csv('train.csv')

# Connect to SQLite database
conn = sqlite3.connect('demo.db')

# Load data into SQLite (replace if table exists)
df.to_sql("sales_data", conn, if_exists='replace', index=False)


# Total orders by region
query1 = """

SELECT REGION, COUNT(*) AS total_orders
FROM sales_data
GROUP BY REGION
ORDER BY total_orders DESC;

"""

# Total sales by category
query2 = """

SELECT REGION, CATEGORY, SUM(SALES) AS total_sales
FROM sales_data
GROUP BY REGION, CATEGORY
ORDER BY REGION, total_sales DESC;

"""

# Total sales per day for EAST region
query3 = """

SELECT [ORDER DATE] AS order_date, SUM(SALES) AS total_sales_on_day
FROM sales_data
WHERE REGION = 'EAST'
GROUP BY [ORDER DATE]
ORDER BY [ORDER DATE];

"""

# Top 10 products by sales
query4 = """

SELECT [Product Name] AS product_name, SUM(SALES) AS total_sales
FROM sales_data
GROUP BY [Product Name]
ORDER BY total_sales DESC
LIMIT 10;

"""

# Total sales by category and subcategory in descending order
query5 = """

SELECT CATEGORY, SUBCATEGORY, SUM(SALES) AS total_sales
FROM sales_data
GROUP BY CATEGORY, SUBCATEGORY
ORDER BY CATEGORY, total_sales DESC;

"""

# -------- Execute queries and save CSVs --------
pd.read_sql_query(query1, conn).to_csv('new_orders_by_region.csv', index=False)
pd.read_sql_query(query2, conn).to_csv('total_sales_by_category.csv', index=False)
pd.read_sql_query(query3, conn).to_csv('total_sales_on_each_date.csv', index=False)
pd.read_sql_query(query4, conn).to_csv('popular_products.csv', index=False)
pd.read_sql_query(query5, conn).to_csv('total_sales_by_category_and_subcategory.csv', index=False)

# Close connection
conn.close()