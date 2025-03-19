# Generated: 2025-03-19 18:10:06.574508
# Result: [(3, 'Electronics', Decimal('1200.00'), 1), (1, 'Electronics', Decimal('500.50'), 2), (5, 'Electronics', Decimal('350.00'), 3), (4, 'Books', Decimal('75.25'), 1), (2, 'Clothing', Decimal('250.75'), 1)]
# Valid: True
import duckdb

# Create an in-memory database and connect
conn = duckdb.connect(':memory:')

# Create a table with sales data
conn.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        category VARCHAR,
        sale_amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, 'Electronics', 500.50),
        (2, 'Clothing', 250.75),
        (3, 'Electronics', 1200.00),
        (4, 'Books', 75.25),
        (5, 'Electronics', 350.00);
''')

# Perform window function to rank sales by category
result = conn.execute('''
    SELECT
        product_id,
        category,
        sale_amount,
        RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as category_rank
    FROM sales
''').fetchall()

for row in result:
    print(row)