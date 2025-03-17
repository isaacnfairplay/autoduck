# Generated: 2025-03-16 22:06:23.378525
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), 10, 50.0), (1, datetime.date(2023, 2, 20), 15, Decimal('52.50'), 25, 51.25), (2, datetime.date(2023, 1, 10), 5, Decimal('75.00'), 5, 75.0), (2, datetime.date(2023, 3, 5), 8, Decimal('77.25'), 13, 76.125)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables for advanced analytics
con.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_date DATE,
    quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO sales VALUES
    (1, '2023-01-15', 10, 50.00),
    (1, '2023-02-20', 15, 52.50),
    (2, '2023-01-10', 5, 75.00),
    (2, '2023-03-05', 8, 77.25);
'''
)

# Perform window function analysis
result = con.execute('''
SELECT
    product_id,
    sale_date,
    quantity,
    price,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity,
    AVG(price) OVER (PARTITION BY product_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as rolling_avg_price
FROM sales
ORDER BY product_id, sale_date
''').fetchall()

for row in result:
    print(row)