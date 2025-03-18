# Generated: 2025-03-16 23:53:40.495516
# Result: [('Smartphone', 'Electronics', Decimal('750.25'), 617.1666666666666, 1), ('Laptop', 'Electronics', Decimal('600.75'), 617.1666666666666, 2), ('Laptop', 'Electronics', Decimal('500.50'), 617.1666666666666, 3)]
# Valid: True
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
import duckdb

# Demonstrate advanced multi-table JOIN and window function
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE sales (sale_id INT, product_id INT, sale_amount DECIMAL(10,2), sale_date DATE);
    CREATE TABLE products (product_id INT, product_name VARCHAR, category VARCHAR);

    INSERT INTO sales VALUES 
        (1, 101, 500.50, '2023-01-15'),
        (2, 102, 750.25, '2023-02-20'),
        (3, 101, 600.75, '2023-03-10');

    INSERT INTO products VALUES 
        (101, 'Laptop', 'Electronics'),
        (102, 'Smartphone', 'Electronics');
''')

# Advanced analytical query with window functions and JOIN
query = '''
    SELECT 
        p.product_name, 
        p.category, 
        s.sale_amount,
        AVG(s.sale_amount) OVER (PARTITION BY p.category) as category_avg_sale,
        RANK() OVER (ORDER BY s.sale_amount DESC) as sale_rank
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    ORDER BY sale_rank
'''

result = con.execute(query).fetchall()
for row in result:
    print(row)