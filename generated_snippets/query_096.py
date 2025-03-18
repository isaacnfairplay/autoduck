# Generated: 2025-03-16 23:55:48.069425
# Result: [(102, Decimal('750.25'), datetime.date(2023, 2, 20), Decimal('750.25')), (101, Decimal('500.50'), datetime.date(2023, 1, 15), Decimal('500.50')), (101, Decimal('600.75'), datetime.date(2023, 3, 10), Decimal('1101.25'))]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

# Create sample sales data
con.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_amount DECIMAL(10,2),
    sale_date DATE
);
INSERT INTO sales VALUES
    (101, 500.50, '2023-01-15'),
    (102, 750.25, '2023-02-20'),
    (101, 600.75, '2023-03-10');
''')

# Perform window function with cumulative sales
result = con.execute('''
SELECT 
    product_id, 
    sale_amount, 
    sale_date,
    SUM(sale_amount) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales
FROM sales
''').fetchall()

# Print cumulative sales results
for row in result:
    print(row)