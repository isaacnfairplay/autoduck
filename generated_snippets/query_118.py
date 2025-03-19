# Generated: 2025-03-19 13:59:12.688409
# Result: [(1, datetime.date(2023, 1, 15), 5, 5, Decimal('250.50')), (1, datetime.date(2023, 2, 20), 3, 8, Decimal('401.25')), (2, datetime.date(2023, 1, 10), 2, 2, Decimal('100.25')), (2, datetime.date(2023, 3, 5), 7, 9, Decimal('450.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table with sales data
conn.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        revenue DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, '2023-01-15', 5, 250.50),
        (1, '2023-02-20', 3, 150.75),
        (2, '2023-01-10', 2, 100.25),
        (2, '2023-03-05', 7, 350.00);
''')

# Demonstrate window function: cumulative sales per product
result = conn.execute('''
    SELECT 
        product_id, 
        sale_date, 
        quantity,
        SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity,
        SUM(revenue) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue
    FROM sales
    ORDER BY product_id, sale_date
''').fetchall()

for row in result:
    print(row)