# Generated: 2025-03-19 17:51:21.232276
# Result: [(4, 'Marketing', Decimal('55000.00'), 'Bob', Decimal('93000.25'), 1), (3, 'Marketing', Decimal('38000.25'), 'Bob', Decimal('93000.25'), 2), (2, 'Sales', Decimal('62000.75'), 'Alice', Decimal('107001.25'), 1), (1, 'Sales', Decimal('45000.50'), 'Alice', Decimal('107001.25'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with employee performance data
conn.execute('''CREATE TABLE employee_performance (
    employee_id INT,
    department VARCHAR,
    quarterly_sales DECIMAL(10,2),
    manager VARCHAR
)''')

# Insert sample performance data
conn.executemany('INSERT INTO employee_performance VALUES (?, ?, ?, ?)', [
    (1, 'Sales', 45000.50, 'Alice'),
    (2, 'Sales', 62000.75, 'Alice'),
    (3, 'Marketing', 38000.25, 'Bob'),
    (4, 'Marketing', 55000.00, 'Bob')
])

# Calculate cumulative sales and rank within departments using window functions
result = conn.execute('''SELECT 
    employee_id,
    department,
    quarterly_sales,
    manager,
    SUM(quarterly_sales) OVER (PARTITION BY department) as department_total_sales,
    RANK() OVER (PARTITION BY department ORDER BY quarterly_sales DESC) as department_sales_rank
FROM employee_performance
ORDER BY department, department_sales_rank''').fetchall()

for row in result:
    print(row)