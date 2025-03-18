# Generated: 2025-03-16 23:55:56.547334
# Result: (102, 1, Decimal('750.25'), 750.25)
# Valid: True
# Variable aggregation_result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create in-memory database connection
con = duckdb.connect(':memory:')

# Create sample sales table
con.execute('''
CREATE TABLE sales (
    product_id INT,
    sale_amount DECIMAL(10,2)
);
INSERT INTO sales VALUES
    (101, 500.50),
    (102, 750.25),
    (101, 600.75);
''')

# Demonstrate aggregation methods
aggregation_result = con.execute('''
SELECT 
    product_id, 
    COUNT(*) as total_sales,
    SUM(sale_amount) as total_revenue,
    AVG(sale_amount) as average_sale
FROM sales
GROUP BY product_id
''').fetchall()

for result in aggregation_result:
    print(f'Product {result[0]}: Total Sales = {result[1]}, Total Revenue = ${result[2]}, Avg Sale = ${result[3]}')