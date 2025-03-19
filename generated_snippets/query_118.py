# Generated: 2025-03-19 08:35:02.431507
# Result: [(1, datetime.date(2023, 1, 15), Decimal('500.00'), Decimal('500.00')), (1, datetime.date(2023, 2, 20), Decimal('750.00'), Decimal('1250.00')), (2, datetime.date(2023, 1, 10), Decimal('250.00'), Decimal('250.00')), (2, datetime.date(2023, 2, 25), Decimal('400.00'), Decimal('650.00'))]
# Valid: True
import duckdb

# Create an in-memory database with sales data
conn = duckdb.connect(':memory:')
conn.execute("""
    CREATE TABLE sales (
        product_id INT, 
        sale_date DATE, 
        quantity INT, 
        revenue DECIMAL(10,2)
    );
    INSERT INTO sales VALUES
        (1, '2023-01-15', 10, 500.00),
        (1, '2023-02-20', 15, 750.00),
        (2, '2023-01-10', 5, 250.00),
        (2, '2023-02-25', 8, 400.00);
""")

# Demonstrate window function with cumulative revenue tracking
result = conn.execute("""
    SELECT 
        product_id, 
        sale_date, 
        revenue,
        SUM(revenue) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue
    FROM sales
    ORDER BY product_id, sale_date
""").fetchall()

for row in result:
    print(f"Product {row[0]}: {row[1]} - Revenue: ${row[2]}, Cumulative: ${row[3]}")