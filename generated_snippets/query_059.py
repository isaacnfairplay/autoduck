# Generated: 2025-03-16 22:46:48.793139
# Result: [('Laptop', Decimal('1500.00'), datetime.date(2023, 4, 5), Decimal('2700.50'), 1350.25, 1), ('Laptop', Decimal('1200.50'), datetime.date(2023, 1, 15), Decimal('1200.50'), 1350.25, 2), ('Smartphone', Decimal('800.25'), datetime.date(2023, 2, 20), Decimal('800.25'), 800.25, 3), ('Tablet', Decimal('600.75'), datetime.date(2023, 3, 10), Decimal('600.75'), 600.75, 4)]
# Valid: True
import duckdb

# Window function demonstration with sales data
con = duckdb.connect(':memory:')

# Create and populate sales table
con.execute('''
    CREATE TABLE sales (
        sale_id INT, 
        product_name VARCHAR, 
        sale_amount DECIMAL(10,2), 
        sale_date DATE
    );

    INSERT INTO sales VALUES
    (1, 'Laptop', 1200.50, '2023-01-15'),
    (2, 'Smartphone', 800.25, '2023-02-20'),
    (3, 'Tablet', 600.75, '2023-03-10'),
    (4, 'Laptop', 1500.00, '2023-04-05');
''')

# Advanced window function query
result = con.execute('''
    SELECT 
        product_name,
        sale_amount,
        sale_date,
        SUM(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_date) as cumulative_sales,
        AVG(sale_amount) OVER (PARTITION BY product_name) as product_avg_sale,
        RANK() OVER (ORDER BY sale_amount DESC) as sale_rank
    FROM sales
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Sale: ${row[1]}, Date: {row[2]}, Cumulative Sales: ${row[3]}, Avg Sale: ${row[4]:.2f}, Rank: {row[5]}")