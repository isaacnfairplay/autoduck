# Generated: 2025-03-19 16:37:24.703695
# Result: [(2, 'Electronics', Decimal('750.50'), 1, 1), (4, 'Electronics', Decimal('600.25'), 2, 2), (1, 'Electronics', Decimal('500.00'), 3, 3), (5, 'Clothing', Decimal('300.00'), 1, 4), (3, 'Clothing', Decimal('250.75'), 2, 5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    category TEXT,
    sale_amount DECIMAL(10,2)
);
''')

conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    (1, 'Electronics', 500.00),
    (2, 'Electronics', 750.50),
    (3, 'Clothing', 250.75),
    (4, 'Electronics', 600.25),
    (5, 'Clothing', 300.00)
])

result = conn.execute('''
SELECT 
    product_id, 
    category, 
    sale_amount,
    RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as category_rank,
    DENSE_RANK() OVER (ORDER BY sale_amount DESC) as overall_dense_rank
FROM sales
''').fetchall()

print(result)