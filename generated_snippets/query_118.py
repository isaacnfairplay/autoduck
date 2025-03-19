# Generated: 2025-03-19 19:51:30.890043
# Result: [('Engineering', 95.1, 1, True), ('Marketing', 88.75, 2, True), ('Sales', 83.05, 3, True), ('Marketing', 88.75, 4, True), ('Sales', 83.05, 5, False)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking employee performance
conn.execute('''
CREATE TABLE employee_performance (
    employee_id INT,
    department VARCHAR,
    performance_score DECIMAL(5,2),
    bonus_eligible BOOLEAN
);

INSERT INTO employee_performance VALUES
(1, 'Sales', 87.5, TRUE),
(2, 'Marketing', 92.3, TRUE),
(3, 'Engineering', 95.1, TRUE),
(4, 'Sales', 78.6, FALSE),
(5, 'Marketing', 85.2, TRUE);
''')

# Calculate performance metrics using window functions
result = conn.execute('''
SELECT 
    department,
    AVG(performance_score) OVER (PARTITION BY department) as dept_avg_score,
    RANK() OVER (ORDER BY performance_score DESC) as performance_rank,
    bonus_eligible
FROM employee_performance
''').fetchall()

print(result)