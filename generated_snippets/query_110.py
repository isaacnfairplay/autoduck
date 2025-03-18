# Generated: 2025-03-17 19:58:25.509660
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create departments table
conn.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

# Insert sample data
conn.execute('''
INSERT INTO departments VALUES
    (101, 'Sales'),
    (102, 'Marketing'),
    (103, 'Engineering')
''')

# Query to demonstrate table data
results = conn.execute('SELECT * FROM departments').fetchall()
for row in results:
    print(row)

conn.close()