# Generated: 2025-03-19 13:04:04.396963
# Result: [('Bob', 'Marketing', Decimal('85000.00'), 88, 3, 1, 0.0), ('Alice', 'Sales', Decimal('100000.00'), 95, 5, 1, 0.5), ('Charlie', 'Engineering', Decimal('120000.00'), 92, 7, 1, 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a complex employee performance tracking system
conn.execute('''
CREATE TABLE employee_performance (
    employee_id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2),
    performance_score INT,
    years_of_service INT
);

INSERT INTO employee_performance VALUES
    (1, 'Alice', 'Sales', 100000.00, 95, 5),
    (2, 'Bob', 'Marketing', 85000.00, 88, 3),
    (3, 'Charlie', 'Engineering', 120000.00, 92, 7);
'''
)

# Advanced window function analysis with multi-criteria ranking
result = conn.execute('''
SELECT
    name,
    department,
    salary,
    performance_score,
    years_of_service,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) as performance_rank,
    PERCENT_RANK() OVER (ORDER BY salary) as salary_percentile
FROM employee_performance
''').fetchall()

for row in result:
    print(row)
