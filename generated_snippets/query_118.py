# Generated: 2025-03-19 13:01:33.077857
# Result: [('Alice', 'Sales', 100000, 85, 0.0), ('Charlie', 'Sales', 95000, 90, 1.0), ('David', 'Engineering', 120000, 95, 0.0), ('Bob', 'Marketing', 90000, 75, 0.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create complex employee performance data
conn.execute('''
CREATE TABLE employee_performance AS
SELECT * FROM (VALUES
    (1, 'Alice', 'Sales', 100000, 85),
    (2, 'Bob', 'Marketing', 90000, 75),
    (3, 'Charlie', 'Sales', 95000, 90),
    (4, 'David', 'Engineering', 120000, 95)
) AS t(id, name, department, salary, performance_score);
''')

# Use WINDOW function to calculate relative performance
result = conn.execute('''
SELECT
    name,
    department,
    salary,
    performance_score,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY performance_score) as performance_percentile
FROM employee_performance
''').fetchall()

for row in result:
    print(row)