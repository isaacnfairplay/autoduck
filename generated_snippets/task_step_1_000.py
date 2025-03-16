# Generated: 2025-03-15 22:10:45.539206
# Result: [('Marketing', 55000.0, 1), ('Sales', 51000.0, 2), ('IT', 60000.0, 1)]
# Valid: True
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute("""
    CREATE TABLE employees (
        employee_id INTEGER,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    )
""")

# Insert sample data
conn.executemany("""
    INSERT INTO employees VALUES (?, ?, ?, ?)
""", [
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Marketing', 55000.00),
    (3, 'Charlie', 'Sales', 52000.00),
    (4, 'David', 'IT', 60000.00)
])

# Perform a simple query
result = conn.execute("""
    SELECT department, 
           AVG(salary) as avg_salary, 
           COUNT(*) as employee_count
    FROM employees
    GROUP BY department
""").fetchall()

# Print results
for row in result:
    print(f"Department: {row[0]}, Average Salary: ${row[1]:.2f}, Employees: {row[2]}")

# Close the connection
conn.close()