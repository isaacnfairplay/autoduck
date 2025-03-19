# Generated: 2025-03-19 10:27:05.437423
# Result: [('Smartphone', 'Electronics', datetime.date(2023, 7, 2), 15, Decimal('18992.40'), 1), ('Laptop', 'Electronics', datetime.date(2023, 7, 1), 10, Decimal('9999.90'), 2), ('Desk Chair', 'Furniture', datetime.date(2023, 7, 3), 5, Decimal('1249.95'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a complex product sales analysis table
conn.execute('''
    CREATE TABLE product_sales (
        product_id INTEGER,
        product_name VARCHAR,
        category VARCHAR,
        sale_date DATE,
        quantity INTEGER,
        unit_price DECIMAL(10,2)
    );

    INSERT INTO product_sales VALUES
        (1, 'Laptop', 'Electronics', '2023-07-01', 10, 999.99),
        (2, 'Smartphone', 'Electronics', '2023-07-02', 15, 599.50),
        (3, 'Desk Chair', 'Furniture', '2023-07-03', 5, 249.99)
''');

# Advanced sales analysis with window functions
result = conn.execute('''
    SELECT 
        product_name,
        category,
        sale_date,
        quantity,
        SUM(quantity * unit_price) OVER (PARTITION BY category ORDER BY sale_date) as cumulative_revenue,
        RANK() OVER (PARTITION BY category ORDER BY quantity DESC) as sales_rank
    FROM product_sales
''').fetchall()

for row in result:
    print(row)