# Generated: 2025-03-19 11:43:23.371361
# Result: [('Electronics', 1500, 39.473684210526315), ('Electronics', 2300, 60.526315789473685), ('Clothing', 1000, 36.36363636363637), ('Clothing', 1750, 63.63636363636363)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Calculate percentage of total sales within each category
result = conn.execute('''
SELECT 
    category, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as category_percentage
FROM sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}, Percentage: {row[2]:.2f}%")