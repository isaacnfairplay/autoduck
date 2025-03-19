# Generated: 2025-03-19 18:58:20.277658
# Result: [('Clothing', 2, 100, Decimal('79.50'), Decimal('7950.00')), ('Electronics', 1, 50, Decimal('499.99'), Decimal('47499.25')), ('Electronics', 3, 25, Decimal('899.99'), Decimal('47499.25')), ('Home', 4, 75, Decimal('149.99'), Decimal('11249.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product inventory table
conn.sql('''
CREATE TABLE inventory (
    product_id INTEGER,
    category VARCHAR,
    stock_quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO inventory VALUES
    (1, 'Electronics', 50, 499.99),
    (2, 'Clothing', 100, 79.50),
    (3, 'Electronics', 25, 899.99),
    (4, 'Home', 75, 149.99);
'''
)

# Calculate total stock value by category with window function
result = conn.sql('''
SELECT 
    category, 
    product_id, 
    stock_quantity, 
    price,
    SUM(stock_quantity * price) OVER (PARTITION BY category) as category_total_value
FROM inventory
ORDER BY category, product_id
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Product ID: {row[1]}, Stock: {row[2]}, Price: ${row[3]}, Category Total Value: ${row[4]:.2f}")