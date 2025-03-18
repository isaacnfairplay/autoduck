# Generated: 2025-03-16 22:46:08.705458
# Result: [('Smartphone', 'Electronics', Decimal('750.25'), 517.1666666666666, 1), ('Laptop', 'Electronics', Decimal('500.50'), 517.1666666666666, 2), ('Laptop', 'Electronics', Decimal('300.75'), 517.1666666666666, 3)]
# Valid: True
import duckdb

# Advanced multi-table JOIN and window function example
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE sales (sale_id INT, product_id INT, sale_amount DECIMAL(10,2), sale_date DATE);
    CREATE TABLE products (product_id INT, product_name VARCHAR, category VARCHAR);

    INSERT INTO sales VALUES 
    (1, 101, 500.50, '2023-01-15'),
    (2, 102, 750.25, '2023-02-20'),
    (3, 101, 300.75, '2023-03-10');

    INSERT INTO products VALUES 
    (101, 'Laptop', 'Electronics'),
    (102, 'Smartphone', 'Electronics');
''')

# Complex query with window function and JOIN
result = con.execute('''
    SELECT 
        p.product_name, 
        p.category, 
        s.sale_amount,
        AVG(s.sale_amount) OVER (PARTITION BY p.category) as category_avg_sale,
        RANK() OVER (ORDER BY s.sale_amount DESC) as sale_rank
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Category: {row[1]}, Sale: ${row[2]}, Category Avg: ${row[3]:.2f}, Rank: {row[4]}")