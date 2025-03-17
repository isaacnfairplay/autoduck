# Generated: 2025-03-17 19:56:58.433363
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('CREATE TABLE users (id INT, name VARCHAR, age INT)')

# Insert sample data
conn.execute('''
INSERT INTO users VALUES
    (1, 'Alice', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 35)
''')

# Execute a simple query
results = conn.execute('SELECT * FROM users WHERE age > 28').fetchall()
for row in results:
    print(row)

conn.close()