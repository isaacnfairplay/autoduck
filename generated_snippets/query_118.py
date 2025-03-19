# Generated: 2025-03-19 17:54:46.954422
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DFA771F0>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic sales data
conn.execute('''CREATE TABLE regional_sales (
    region VARCHAR,
    product VARCHAR,
    sales_amount DECIMAL(10,2)
)''')

# Insert sample sales data
conn.executemany('INSERT INTO regional_sales VALUES (?, ?, ?)', [
    ('North', 'Laptop', 50000.00),
    ('North', 'Tablet', 25000.50),
    ('South', 'Laptop', 45000.25),
    ('South', 'Smartphone', 60000.75)
])

# Calculate rolling average sales per region using window function
result = conn.execute('''SELECT 
    region, 
    product, 
    sales_amount,
    AVG(sales_amount) OVER (PARTITION BY region ORDER BY sales_amount) as region_rolling_avg
FROM regional_sales
ORDER BY region, sales_amount''')

for row in result.fetchall():
    print(row)