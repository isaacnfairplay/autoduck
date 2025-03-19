# Generated: 2025-03-19 08:48:01.362573
# Result: [('Charlie', 'Sales', Decimal('95.70'), 0.0), ('Alice', 'Sales', Decimal('92.50'), 1.0), ('David', 'Marketing', Decimal('90.10'), 0.0), ('Bob', 'Marketing', Decimal('88.30'), 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate employee performance table
conn.execute('CREATE TABLE employee_performance (employee TEXT, department TEXT, performance_score DECIMAL(5,2), bonus DECIMAL(10,2))')
conn.executemany('INSERT INTO employee_performance VALUES (?, ?, ?, ?)', [
    ('Alice', 'Sales', 92.5, 5000.00),
    ('Bob', 'Marketing', 88.3, 4200.50),
    ('Charlie', 'Sales', 95.7, 5500.25),
    ('David', 'Marketing', 90.1, 4500.75)
])

# Calculate department performance ranking using PERCENT_RANK
result = conn.execute('''
    SELECT 
        employee, 
        department, 
        performance_score,
        PERCENT_RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) as performance_percentile
    FROM employee_performance
''').fetchall()

for row in result:
    print(f"Employee: {row[0]}, Department: {row[1]}, Score: {row[2]}, Percentile: {row[3]:.2%}")