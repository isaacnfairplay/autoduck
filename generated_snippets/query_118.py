# Generated: 2025-03-19 09:55:21.303144
# Result: [(3, 'Electronics', Decimal('1200.00'), 1), (1, 'Electronics', Decimal('500.50'), 2), (4, 'Books', Decimal('75.25'), 1), (2, 'Clothing', Decimal('250.75'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('''
CREATE TABLE sales AS 
SELECT * FROM (
    VALUES 
    (1, 'Electronics', 500.50),
    (2, 'Clothing', 250.75),
    (3, 'Electronics', 1200.00),
    (4, 'Books', 75.25)
) t(sale_id, category, amount)
''')

# Perform window function to rank sales within categories
result = conn.execute('''
SELECT 
    sale_id, 
    category, 
    amount,
    RANK() OVER (PARTITION BY category ORDER BY amount DESC) as category_rank
FROM sales
''').fetchall()

for row in result:
    print(row)