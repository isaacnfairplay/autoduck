# Generated: 2025-03-17 20:07:41.743113
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
# Variable results: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Create in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE sales (
        product_id INT,
        sale_date DATE,
        amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, '2023-01-15', 500.50),
        (1, '2023-02-20', 750.25),
        (2, '2023-01-10', 300.75),
        (2, '2023-03-05', 450.00);
''')

# Advanced window function with cumulative sum and ranking
query = '''
    SELECT 
        product_id,
        sale_date,
        amount,
        SUM(amount) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales,
        RANK() OVER (ORDER BY amount DESC) as sales_rank
    FROM sales
    ORDER BY product_id, sale_date
'''

results = con.execute(query).fetchall()
for row in results:
    print(row)