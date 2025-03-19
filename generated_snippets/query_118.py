# Generated: 2025-03-19 18:34:56.282776
# Result: [(1, datetime.date(2023, 1, 15), Decimal('150.50'), Decimal('150.50')), (1, datetime.date(2023, 2, 20), Decimal('200.75'), Decimal('351.25')), (2, datetime.date(2023, 1, 10), Decimal('100.25'), Decimal('100.25')), (2, datetime.date(2023, 3, 5), Decimal('175.80'), Decimal('276.05'))]
# Valid: True
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, '2023-01-15', 150.50),
        (1, '2023-02-20', 200.75),
        (2, '2023-01-10', 100.25),
        (2, '2023-03-05', 175.80)
''');

# Use window function to calculate cumulative sales per product
result = conn.execute('''
    SELECT 
        product_id, 
        sale_date, 
        amount,
        SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales
    FROM sales
''').fetchall()

for row in result:
    print(row)