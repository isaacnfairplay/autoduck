# Generated: 2025-03-19 19:03:21.750185
# Result: [(3, 'Marketing', Decimal('85.70'), 0.0), (4, 'Marketing', Decimal('91.20'), 1.0), (1, 'Sales', Decimal('88.50'), 0.0), (2, 'Sales', Decimal('92.30'), 1.0)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create and populate employee performance table
conn.sql('''
CREATE TABLE employee_performance (
    employee_id INTEGER,
    department VARCHAR,
    quarterly_score DECIMAL(5,2)
);

INSERT INTO employee_performance VALUES
    (1, 'Sales', 88.5),
    (2, 'Sales', 92.3),
    (3, 'Marketing', 85.7),
    (4, 'Marketing', 91.2);
'''
)

# Calculate percentile rank of performance within department
result = conn.sql('''
SELECT
    employee_id,
    department,
    quarterly_score,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY quarterly_score) as performance_percentile
FROM employee_performance
ORDER BY department, performance_percentile
''').fetchall()

for row in result:
    print(f"Employee {row[0]} in {row[1]}: Score {row[2]}, Percentile {row[3]*100:.2f}%")