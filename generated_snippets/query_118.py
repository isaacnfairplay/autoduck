# Generated: 2025-03-19 21:29:38.161233
# Result: [(3, 'Sales', Decimal('95.70'), 1), (1, 'Sales', Decimal('92.50'), 2), (5, 'Engineering', Decimal('89.60'), 1), (4, 'Marketing', Decimal('91.20'), 1), (2, 'Marketing', Decimal('88.30'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample table with employee performance data
conn.execute('''CREATE TABLE employee_performance (
    employee_id INT,
    department VARCHAR,
    performance_score DECIMAL(5,2)
)''')

# Insert sample performance data
conn.executemany('INSERT INTO employee_performance VALUES (?, ?, ?)', [
    (1, 'Sales', 92.5),
    (2, 'Marketing', 88.3),
    (3, 'Sales', 95.7),
    (4, 'Marketing', 91.2),
    (5, 'Engineering', 89.6)
])

# Use window functions to rank employees within each department
result = conn.sql('''SELECT 
    employee_id,
    department,
    performance_score,
    RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) as dept_rank
FROM employee_performance
''').fetchall()

print(result)