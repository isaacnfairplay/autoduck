# Generated: 2025-03-17 19:59:35.740873
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create sample relations for demonstrating joins
conn.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')
conn.execute('CREATE TABLE departments (id INT, name VARCHAR)')

# Insert sample data
conn.execute("""INSERT INTO employees VALUES
    (1, 'Alice', 101),
    (2, 'Bob', 102),
    (3, 'Charlie', 101)
""")

conn.execute("""INSERT INTO departments VALUES
    (101, 'Sales'),
    (102, 'Marketing'),
    (103, 'Engineering')
""")

# Perform a JOIN to connect relations
query = '''
SELECT e.name, d.name as department
FROM employees e
JOIN departments d ON e.department_id = d.id
'''

results = conn.execute(query).fetchall()
for row in results:
    print(row)

conn.close()