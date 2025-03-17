# Generated: 2025-03-16 22:49:24.178656
# Result: [(2, datetime.date(2023, 2, 25), 8, Decimal('110.00'), Decimal('1380.00'), 1), (1, datetime.date(2023, 2, 20), 15, Decimal('55.00'), Decimal('1325.00'), 2), (1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), Decimal('500.00'), 3), (2, datetime.date(2023, 1, 10), 5, Decimal('100.00'), Decimal('500.00'), 3)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table with complex data
con.execute('''
CREATE TABLE product_sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    (1, '2023-01-15', 10, 50.00),
    (1, '2023-02-20', 15, 55.00),
    (2, '2023-01-10', 5, 100.00),
    (2, '2023-02-25', 8, 110.00);
''');

# Advanced analytical query using window functions
result = con.execute('''
SELECT 
    product_id,
    sale_date,
    quantity,
    price,
    SUM(quantity * price) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue,
    RANK() OVER (ORDER BY quantity * price DESC) as sales_rank
FROM product_sales
''').fetchall()

print(result)