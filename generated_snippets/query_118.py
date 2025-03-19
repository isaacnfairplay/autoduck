# Generated: 2025-03-19 10:22:42.685667
# Result: [('Smartphone', datetime.date(2023, 7, 2), Decimal('8992.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
    CREATE TABLE product_sales (
        product_id INTEGER,
        product_name VARCHAR,
        sale_date DATE,
        quantity INTEGER,
        price DECIMAL(10,2)
    );

    INSERT INTO product_sales VALUES
        (1, 'Laptop', '2023-07-01', 10, 999.99),
        (2, 'Smartphone', '2023-07-02', 15, 599.50)
''');

# Perform simple SELECT with multiple conditions
result = conn.execute('''
    SELECT product_name, sale_date, quantity * price as total_revenue
    FROM product_sales
    WHERE quantity > 10 AND price > 500
    ORDER BY total_revenue DESC
''').fetchall()

for row in result:
    print(row)