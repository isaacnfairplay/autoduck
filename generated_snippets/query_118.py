# Generated: 2025-03-17 20:07:56.439196
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample sales table
con.execute('''
    CREATE TABLE sales (
        product_id INT,
        sale_date DATE,
        quantity INT,
        price DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, '2023-01-15', 10, 50.00),
        (1, '2023-02-20', 15, 55.00),
        (2, '2023-01-10', 5, 100.00),
        (2, '2023-03-05', 8, 110.00);
''')

# Perform complex analytical query with window functions
query = '''
    SELECT 
        product_id,
        FIRST_VALUE(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) as first_sale_date,
        LAST_VALUE(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) as last_sale_date,
        SUM(quantity * price) OVER (PARTITION BY product_id) as total_product_revenue
    FROM sales
'''

results = con.execute(query).fetchall()
for row in results:
    print(row)