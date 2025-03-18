# Generated: 2025-03-17 20:00:04.216554
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create tables for complex join
conn.execute('CREATE TABLE orders (order_id INT, customer_id INT, total_amount DECIMAL)')
conn.execute('CREATE TABLE customers (customer_id INT, name VARCHAR, city VARCHAR)')

# Insert sample data
conn.execute('''
INSERT INTO orders VALUES
    (1, 101, 500.00),
    (2, 102, 750.50),
    (3, 101, 250.75)
''')

conn.execute('''
INSERT INTO customers VALUES
    (101, 'Alice', 'New York'),
    (102, 'Bob', 'San Francisco')
''')

# Complex query with join, aggregation, and window function
query = '''
SELECT 
    c.name, 
    c.city, 
    SUM(o.total_amount) as total_purchases,
    RANK() OVER (ORDER BY SUM(o.total_amount) DESC) as customer_rank
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name, c.city
'''

results = conn.execute(query).fetchall()
for row in results:
    print(row)

conn.close()