# Generated: 2025-03-17 19:58:18.810333
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create employees table
conn.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')

# Insert sample data
conn.execute('''
INSERT INTO employees VALUES
    (1, 'Alice', 101),
    (2, 'Bob', 102),
    (3, 'Charlie', 101)
''')

# Query to demonstrate table usage
results = conn.execute('SELECT * FROM employees WHERE department_id = 101').fetchall()
for row in results:
    print(row)

conn.close()