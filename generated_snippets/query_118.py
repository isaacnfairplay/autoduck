# Generated: 2025-03-17 20:08:02.342564
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create and populate a sample table
con.execute('''
    CREATE TABLE customers (
        id INT,
        name VARCHAR,
        age INT,
        city VARCHAR
    );

    INSERT INTO customers VALUES
        (1, 'Alice', 30, 'New York'),
        (2, 'Bob', 45, 'Chicago'),
        (3, 'Charlie', 25, 'San Francisco');
''')

# Perform a simple query
results = con.execute('SELECT * FROM customers WHERE age > 30').fetchall()
for row in results:
    print(row)