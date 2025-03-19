# Generated: 2025-03-19 16:59:56.830745
# Result: [('Engineering', 'Frontend', 'Charlie', Decimal('91.70'), 2, 0.0), ('Sales', 'SMB', 'Eve', Decimal('87.20'), 2, 0.0), ('Sales', 'Enterprise', 'David', Decimal('89.60'), 1, 0.0), ('Engineering', 'Backend', 'Bob', Decimal('88.30'), 3, 0.0), ('Engineering', 'Backend', 'Alice', Decimal('92.50'), 1, 1.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create complex organizational hierarchy with nested aggregations
conn.sql('''CREATE TABLE employee_performance (
    department VARCHAR,
    team VARCHAR,
    employee_name VARCHAR,
    performance_score DECIMAL(5,2)
);

INSERT INTO employee_performance VALUES
    ('Engineering', 'Backend', 'Alice', 92.5),
    ('Engineering', 'Backend', 'Bob', 88.3),
    ('Engineering', 'Frontend', 'Charlie', 91.7),
    ('Sales', 'Enterprise', 'David', 89.6),
    ('Sales', 'SMB', 'Eve', 87.2)
''')

# Compute performance metrics using advanced window and ranking functions
result = conn.sql('''SELECT
    department,
    team,
    employee_name,
    performance_score,
    RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) as dept_rank,
    PERCENT_RANK() OVER (PARTITION BY team ORDER BY performance_score) as team_percentile
FROM employee_performance
''').fetchall()

print(result)