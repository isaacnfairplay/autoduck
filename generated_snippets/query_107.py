# Generated: 2025-03-17 19:57:05.755077
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('CREATE TABLE products (id INT, name VARCHAR, price DECIMAL)')

# Insert data
conn.execute('''
INSERT INTO products VALUES
    (1, 'Laptop', 1200.50),
    (2, 'Phone', 800.25),
    (3, 'Tablet', 450.75)
''')

# Perform analytical query with window function
query = '''
SELECT 
    name, 
    price, 
    RANK() OVER (ORDER BY price DESC) as price_rank
FROM products
'''

results = conn.execute(query).fetchall()
for row in results:
    print(row)

conn.close()