# Generated: 2025-03-19 11:45:16.183950
# Result: [('Laptop', 'Electronics', 50, Decimal('1200.00'), Decimal('60000.00')), ('Smartphone', 'Electronics', 100, Decimal('800.50'), Decimal('140050.00')), ('Headphones', 'Electronics', 200, Decimal('150.25'), Decimal('170100.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with inventory data
conn.execute('''
CREATE TABLE inventory (
    product_id INTEGER,
    product_name VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    unit_price DECIMAL(10,2)
);

INSERT INTO inventory VALUES
(1, 'Laptop', 'Electronics', 50, 1200.00),
(2, 'Smartphone', 'Electronics', 100, 800.50),
(3, 'Headphones', 'Electronics', 200, 150.25);
''')

# Analyze inventory with cumulative calculation
result = conn.execute('''
SELECT
    product_name,
    category,
    quantity,
    unit_price,
    SUM(quantity * unit_price) OVER (PARTITION BY category ORDER BY quantity) as cumulative_value
FROM inventory
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): Qty {row[2]}, Price ${row[3]}, Cumulative Value ${row[4]:.2f}")