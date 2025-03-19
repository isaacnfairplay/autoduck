# Generated: 2025-03-19 12:45:06.414174
# Result: [('John', Decimal('50.00'), '2023-06-01', Decimal('50.00')), ('Jane', Decimal('75.50'), '2023-06-02', Decimal('125.50')), ('Bob', Decimal('125.25'), '2023-06-03', Decimal('250.75')), ('Alice', Decimal('200.00'), '2023-06-04', Decimal('450.75'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample customer orders
conn.execute('''
CREATE TABLE orders AS
SELECT * FROM (VALUES
    (1, 'John', 50.00, '2023-06-01'),
    (2, 'Jane', 75.50, '2023-06-02'),
    (3, 'Bob', 125.25, '2023-06-03'),
    (4, 'Alice', 200.00, '2023-06-04')
) AS t(order_id, customer, total, order_date);
''')

# Calculate running total with window function
result = conn.execute('''
SELECT 
    customer, 
    total, 
    order_date,
    SUM(total) OVER (ORDER BY order_date) as cumulative_sales
FROM orders
''').fetchall()

for row in result:
    print(row)