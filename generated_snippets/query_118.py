# Generated: 2025-03-19 14:00:04.740190
# Result: [(2, 'Clothing', 100, 1, 2), (3, 'Books', 75, 2, 1), (1, 'Electronics', 50, 3, 3)]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create and populate inventory table
conn.execute('''
    CREATE TABLE inventory (
        product_id INTEGER,
        category TEXT,
        stock_quantity INTEGER,
        price DECIMAL(10,2)
    );

    INSERT INTO inventory VALUES
        (1, 'Electronics', 50, 129.99),
        (2, 'Clothing', 100, 49.50),
        (3, 'Books', 75, 19.99);
''')

# Analytical query with window functions and filtering
result = conn.execute('''
    SELECT 
        product_id, 
        category, 
        stock_quantity,
        RANK() OVER (ORDER BY stock_quantity DESC) as stock_rank,
        NTILE(3) OVER (ORDER BY price) as price_tier
    FROM inventory
    WHERE stock_quantity > 25
    ORDER BY stock_rank
''').fetchall()

for row in result:
    print(row)