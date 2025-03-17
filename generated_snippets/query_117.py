# Generated: 2025-03-17 19:59:06.298706
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create departments table
conn.execute('CREATE TABLE departments (id INT, dept_name VARCHAR)')

# Insert specific department tuple
conn.execute("INSERT INTO departments VALUES (1, 'Sales')")

# Query and display results
results = conn.execute('SELECT * FROM departments').fetchall()
for row in results:
    print(row)

conn.close()