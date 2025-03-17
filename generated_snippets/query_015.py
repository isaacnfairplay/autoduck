# Generated: 2025-03-16 22:10:17.485686
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('500.00'), Decimal('500.00'), 12.5), (1, datetime.date(2023, 2, 20), 15, Decimal('750.00'), Decimal('1250.00'), 12.5), (2, datetime.date(2023, 1, 10), 5, Decimal('250.00'), Decimal('250.00'), 6.5), (2, datetime.date(2023, 2, 25), 8, Decimal('400.00'), Decimal('650.00'), 6.5)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample sales table with product and revenue data
con.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        revenue DECIMAL(10,2)
    );
''')

# Insert sample sales data
con.execute('''
    INSERT INTO sales VALUES
    (1, '2023-01-15', 10, 500.00),
    (1, '2023-02-20', 15, 750.00),
    (2, '2023-01-10', 5, 250.00),
    (2, '2023-02-25', 8, 400.00)
''')

# Perform a complex analytical query with window functions
result = con.execute('''
    SELECT 
        product_id, 
        sale_date, 
        quantity,
        revenue,
        SUM(revenue) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue,
        AVG(quantity) OVER (PARTITION BY product_id) as avg_product_quantity
    FROM sales
    ORDER BY product_id, sale_date
''').fetchall()

for row in result:
    print(row)