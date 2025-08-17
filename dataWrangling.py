import sqlite3
import pandas as pd

# Load database
df = pd.read_csv('train.csv')


conn = sqlite3.connect('demo.db')

# Load datafile to a SQLite Database
# if_exists means that if there is currently a table in the database with the same name, then we replace that table with the new table that we created here
df.to_sql("sales_data", conn, if_exists = 'replace')

cursor = conn.cursor()

prompt1 = '''

SELECT REGION, COUNT(*) AS total_orders
FROM sales_data
GROUP BY REGION
ORDER BY total_orders DESC;

'''

prompt2 = '''

SELECT CATEGORY, SUM(SALES) AS total_sales
FROM sales_data
GROUP BY CATEGORY
ORDER BY total_sales DESC;

'''

prompt3 = '''

SELECT ORDER DATE, SUM(SALES) AS total_sales_on_day
FROM sales_data
WHERE REGION = 'EAST' 
GROUP BY ORDER DATE

'''

cursor.execute(prompt1)
rows1 = cursor.fetchall()

newData = pd.DataFrame(rows1, columns = ['Regions', 'Total Orders'])
newData.to_csv('new_orders_by_region.csv', index = False)

cursor.execute(prompt2)
rows2 = cursor.fetchall()

newData2 = pd.DataFrame(rows2, columns = ['Category', 'Total Sales'])
newData2.to_csv('total_sales_by_category.csv', index = False)

cursor.execute(prompt3)
rows3 = cursor.fetchall()

newData3 = pd.DataFrame(rows3, columns = ['Category', 'Sales by Date'])
newData3.to_csv('total_sales_on_each_date.csv', index = False)

#Close connection   
conn.close()

