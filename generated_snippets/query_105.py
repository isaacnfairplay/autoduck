# Generated: 2025-03-17 19:56:52.134249
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
)''')

# Insert sample sales data
conn.execute('''
INSERT INTO sales VALUES
    (1, '2023-01-15', 10, 50.00),
    (1, '2023-02-20', 15, 52.50),
    (2, '2023-01-10', 5, 75.00),
    (2, '2023-02-25', 8, 77.25)
''')

# Complex analytical query with window functions
query = '''
SELECT 
    product_id,
    sale_date,
    quantity,
    price,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity,
    AVG(price) OVER (PARTITION BY product_id) as avg_product_price
FROM sales
ORDER BY product_id, sale_date
'''

results = conn.execute(query).fetchall()
for row in results:
    print(row)

conn.close()