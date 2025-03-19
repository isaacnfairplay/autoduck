# Generated: 2025-03-19 12:17:50.125377
# Result: [(1, datetime.date(2023, 1, 15), 5, Decimal('50.00'), Decimal('250.00')), (1, datetime.date(2023, 2, 20), 3, Decimal('52.50'), Decimal('407.50')), (2, datetime.date(2023, 1, 10), 7, Decimal('25.00'), Decimal('175.00')), (2, datetime.date(2023, 3, 5), 4, Decimal('27.50'), Decimal('285.00'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    (1, '2023-01-15', 5, 50.00),
    (1, '2023-02-20', 3, 52.50),
    (2, '2023-01-10', 7, 25.00),
    (2, '2023-03-05', 4, 27.50);
''')

# Demonstrate window function for cumulative sales tracking
result = conn.execute('''
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    price,
    SUM(quantity * price) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_revenue
FROM product_sales
''').fetchall()

for row in result:
    print(row)