# Generated: 2025-03-19 11:13:31.487921
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Engineering', 85000.50),
    (2, 'Bob', 'Sales', 72000.75),
    (3, 'Charlie', 'Engineering', 92000.25);

SELECT * FROM employees e
WHERE e.department = 'Engineering';
''').fetchall()