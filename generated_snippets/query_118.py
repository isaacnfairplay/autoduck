# Generated: 2025-03-19 19:52:21.182337
# Result: [(1, 'Alice', 28), (2, 'Bob', 35), (3, 'Charlie', 42)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('''
CREATE TABLE customers (
    id INT,
    name VARCHAR,
    age INT
);

INSERT INTO customers VALUES
(1, 'Alice', 28),
(2, 'Bob', 35),
(3, 'Charlie', 42);
''')

# Simple SELECT * query
result = conn.execute('SELECT * FROM customers').fetchall()
print(result)