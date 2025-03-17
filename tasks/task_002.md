# Task: Your comprehensive example demonstrates key aspects of the DuckDB relational API effectively. Some additional areas we could explore might include:

1. More complex joins between relations
2. Window function implementations
3. Advanced filtering and transformation techniques
4. Performance benchmarking of different query approaches

Would you like me to expand the example to showcase any of these advanced DuckDB relational API techniques?

## Step 1: Your comprehensive example demonstrates key aspects of the DuckDB relational API effectively. Some additional areas we could explore might include:

```python
import duckdb

# Advanced DuckDB Relational API Example
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE customers (id INT, name VARCHAR);
    CREATE TABLE orders (order_id INT, customer_id INT, amount DECIMAL);

    INSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
    INSERT INTO orders VALUES (101, 1, 250.50), (102, 1, 350.75), (103, 2, 125.25);
''')

# Complex query using relational API
customer_orders = (con.table('customers')
    .join(con.table('orders'), 'customers.id = orders.customer_id')
    .filter('amount > 200')
    .aggregate('customer_id, SUM(amount) as total_spend')
)

print(customer_orders.execute().fetchall())
```

**Result**: [(['name', 'price'],), (['name', 'price'],)]

**Explanation**: Demonstrates advanced DuckDB relational API techniques including table creation, multi-table joins, filtering, and aggregation in a programmatic manner.
## Step 2: 1. More complex joins between relations

```python
import duckdb

# Advanced Multi-Table Join Example
con = duckdb.connect(':memory:')

# Create sample tables with more complex relationships
con.execute('''
    CREATE TABLE employees (emp_id INT, name VARCHAR, dept_id INT);
    CREATE TABLE departments (dept_id INT, dept_name VARCHAR);
    CREATE TABLE salaries (emp_id INT, salary DECIMAL);

    INSERT INTO employees VALUES 
        (1, 'Alice', 10), (2, 'Bob', 20), (3, 'Charlie', 10), (4, 'David', 30);
    INSERT INTO departments VALUES 
        (10, 'Sales'), (20, 'Marketing'), (30, 'Engineering');
    INSERT INTO salaries VALUES 
        (1, 50000), (2, 60000), (3, 55000), (4, 75000);
''')

# Complex multi-table join with filtering and aggregation
multi_join_result = (
    con.table('employees')
    .join(con.table('departments'), 'employees.dept_id = departments.dept_id')
    .join(con.table('salaries'), 'employees.emp_id = salaries.emp_id')
    .filter('salary > 52000')
    .aggregate('dept_name, AVG(salary) as avg_dept_salary, COUNT(*) as employee_count')
)

print(multi_join_result.execute().fetchall())
```

**Result**: [(['name', 'price'],), (['name', 'price'],)]

**Explanation**: Demonstrates a complex multi-table join across three relations (employees, departments, salaries) with advanced filtering and aggregation, showing DuckDB's powerful relational API capabilities.
## Step 3: 2. Window function implementations

```python
import duckdb

# Window Function Demonstration
con = duckdb.connect(':memory:')

# Create and populate sample sales table
con.execute('''CREATE TABLE sales (region VARCHAR, product VARCHAR, sale_amount DECIMAL)''')
con.execute('''INSERT INTO sales VALUES 
    ('North', 'A', 1000), 
    ('North', 'B', 1500), 
    ('South', 'A', 800), 
    ('South', 'B', 1200), 
    ('East', 'A', 1300), 
    ('East', 'B', 1100)''')

# Demonstrate window functions
window_query = '''
SELECT 
    region, 
    product, 
    sale_amount,
    SUM(sale_amount) OVER (PARTITION BY region) as region_total,
    RANK() OVER (ORDER BY sale_amount DESC) as sales_rank
FROM sales
'''

result = con.execute(window_query).fetchall()
for row in result:
    print(row)
```

**Result**: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]

**Explanation**: This example demonstrates window functions in DuckDB, showing how to compute running totals per region and rank sales amounts across all records.
## Step 4: 3. Advanced filtering and transformation techniques

```python
import duckdb

# Advanced Filtering and Transformation with DuckDB
con = duckdb.connect(':memory:')

# Create sample data
con.execute('''CREATE TABLE products (
    id INT,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL,
    stock INT
)''')

con.execute('''INSERT INTO products VALUES
    (1, 'Laptop', 'Electronics', 1200.50, 50),
    (2, 'Phone', 'Electronics', 800.25, 75),
    (3, 'Tablet', 'Electronics', 500.00, 100),
    (4, 'Headphones', 'Accessories', 150.75, 200)''')

# Advanced filtering with complex conditions
filtered_products = con.query('''
    SELECT 
        name, 
        category, 
        price,
        CASE 
            WHEN price > 1000 THEN 'High-End'
            WHEN price BETWEEN 500 AND 1000 THEN 'Mid-Range'
            ELSE 'Budget'
        END as price_tier,
        stock * price as total_inventory_value
    FROM products
    WHERE category = 'Electronics' AND stock > 25
    ORDER BY total_inventory_value DESC
''')

print(filtered_products.fetchall())
```

**Result**: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]

**Explanation**: Demonstrates advanced filtering techniques in DuckDB using a products table, including complex conditional logic with CASE statement, calculated fields, and multi-condition filtering.
## Step 5: 4. Performance benchmarking of different query approaches

```python
import duckdb
import time

# Performance Benchmarking of Query Approaches
con = duckdb.connect(':memory:')

# Create large sample dataset
con.execute('CREATE TABLE large_data AS SELECT range AS id, random() AS value FROM range(1000000)')

# Benchmark 1: Direct SQL Query
start_time = time.time()
result1 = con.execute('SELECT AVG(value) FROM large_data WHERE id > 500000').fetchone()
sql_time = time.time() - start_time

# Benchmark 2: Relational API
start_time = time.time()
result2 = (con.table('large_data')
    .filter('id > 500000')
    .aggregate('AVG(value)')
    .execute().fetchone())
rel_api_time = time.time() - start_time

print(f'SQL Query Time: {sql_time:.4f} seconds')
print(f'Relational API Time: {rel_api_time:.4f} seconds')
print(f'Results Match: {result1 == result2}')
```

**Result**: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]

**Explanation**: Demonstrates performance comparison between traditional SQL query and DuckDB's relational API by benchmarking average computation on a large dataset, measuring execution times and comparing results.
## Step 6: Would you like me to expand the example to showcase any of these advanced DuckDB relational API techniques?

```python
import duckdb

# Advanced Recursive Common Table Expression (CTE) Example
con = duckdb.connect(':memory:')

# Create a hierarchical organization structure
con.execute('''
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR,
    manager_id INT
);

INSERT INTO employees VALUES 
    (1, 'CEO', NULL),
    (2, 'CTO', 1),
    (3, 'CFO', 1),
    (4, 'Engineering Manager', 2),
    (5, 'Finance Manager', 3)
''')

# Recursive CTE to show organizational hierarchy
recursive_query = '''
WITH RECURSIVE org_hierarchy(emp_id, name, manager_id, level) AS (
    SELECT emp_id, name, manager_id, 0
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.emp_id, e.name, e.manager_id, oh.level + 1
    FROM employees e
    JOIN org_hierarchy oh ON e.manager_id = oh.emp_id
)
SELECT * FROM org_hierarchy
ORDER BY level, emp_id
'''

results = con.execute(recursive_query).fetchall()
for row in results:
    print(f'Level {row[3]}: {row[1]}')
```

**Result**: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]

**Explanation**: Demonstrates a recursive Common Table Expression (CTE) in DuckDB to generate an organizational hierarchy, showing how employees are related through management levels using a self-referencing recursive query.
