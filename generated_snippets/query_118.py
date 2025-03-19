# Generated: 2025-03-19 14:32:06.044258
# Result: [(3, 'Electronics', Decimal('750.75'), 1), (1, 'Electronics', Decimal('500.50'), 2), (4, 'Books', Decimal('100.00'), 1), (2, 'Clothing', Decimal('200.25'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data with product details
conn.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        category VARCHAR,
        amount DECIMAL(10,2)
    );
    INSERT INTO sales VALUES
        (1, 'Electronics', 500.50),
        (2, 'Clothing', 200.25),
        (3, 'Electronics', 750.75),
        (4, 'Books', 100.00)
''')

# Use window functions to rank products within categories
result = conn.execute('''
    SELECT 
        product_id, 
        category, 
        amount,
        RANK() OVER (PARTITION BY category ORDER BY amount DESC) as category_rank
    FROM sales
''').fetchall()

for row in result:
    print(f"Product {row[0]} in {row[1]}: ${row[2]} (Rank: {row[3]})")