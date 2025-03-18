# Generated: 2025-03-16 22:16:58.622323
# Result: [(1, datetime.date(2023, 1, 15), 10, Decimal('1500.50'), Decimal('1500.50'), 1), (3, datetime.date(2023, 3, 10), 8, Decimal('1200.75'), Decimal('3451.50'), 2), (2, datetime.date(2023, 2, 20), 5, Decimal('750.25'), Decimal('2250.75'), 3)]
# Valid: True
import duckdb

# Establish an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table for product sales tracking
con.sql('''
CREATE TABLE product_sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    total_revenue DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
    (1, '2023-01-15', 10, 1500.50),
    (2, '2023-02-20', 5, 750.25),
    (3, '2023-03-10', 8, 1200.75);
''')

# Perform analytical query with window functions
result = con.sql('''
SELECT 
    product_id,
    sale_date,
    quantity,
    total_revenue,
    SUM(total_revenue) OVER (ORDER BY sale_date) AS cumulative_revenue,
    RANK() OVER (ORDER BY quantity DESC) AS sales_rank
FROM product_sales
''').fetchall()

for row in result:
    print(row)