# Generated: 2025-03-18 05:44:14.413525
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), Decimal('500.00')), (1, datetime.date(2023, 2, 20), 15, Decimal('52.50'), Decimal('1287.50')), (2, datetime.date(2023, 1, 10), 5, Decimal('75.00'), Decimal('375.00')), (2, datetime.date(2023, 2, 25), 8, Decimal('80.00'), Decimal('1015.00'))]
# Valid: True
import duckdb

# Create an in-memory database and generate sample sales data
conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.sql("""
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        price DECIMAL(10,2)
    );
    INSERT INTO sales VALUES
        (1, '2023-01-15', 10, 50.00),
        (1, '2023-02-20', 15, 52.50),
        (2, '2023-01-10', 5, 75.00),
        (2, '2023-02-25', 8, 80.00);
""")

# Use window function to calculate running total of sales
result = conn.sql("""
    SELECT 
        product_id, 
        sale_date, 
        quantity, 
        price,
        SUM(quantity * price) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales
    FROM sales
""").fetchall()

for row in result:
    print(row)
