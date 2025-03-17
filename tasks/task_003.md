# Task: The DuckDB relational API example demonstrates key techniques for querying and manipulating relations. Some potential follow-up tasks could include:

1. Develop a more complex multi-table join example
2. Showcase window function implementations
3. Create a performance optimization comparison between SQL and relational API approaches
4. Implement a recursive query pattern
5. Build an example that demonstrates data transformation techniques

Which area would you like me to focus on next?

## Step 1: The DuckDB relational API example demonstrates key techniques for querying and manipulating relations. Some potential follow-up tasks could include:

```python
import duckdb

# Advanced multi-table JOIN and window function example
con = duckdb.connect(':memory:')

# Create sample tables
con.execute('''
    CREATE TABLE sales (sale_id INT, product_id INT, sale_amount DECIMAL(10,2), sale_date DATE);
    CREATE TABLE products (product_id INT, product_name VARCHAR, category VARCHAR);

    INSERT INTO sales VALUES 
    (1, 101, 500.50, '2023-01-15'),
    (2, 102, 750.25, '2023-02-20'),
    (3, 101, 300.75, '2023-03-10');

    INSERT INTO products VALUES 
    (101, 'Laptop', 'Electronics'),
    (102, 'Smartphone', 'Electronics');
''')

# Complex query with window function and JOIN
result = con.execute('''
    SELECT 
        p.product_name, 
        p.category, 
        s.sale_amount,
        AVG(s.sale_amount) OVER (PARTITION BY p.category) as category_avg_sale,
        RANK() OVER (ORDER BY s.sale_amount DESC) as sale_rank
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Category: {row[1]}, Sale: ${row[2]}, Category Avg: ${row[3]:.2f}, Rank: {row[4]}")
```

**Result**: [('Smartphone', 'Electronics', Decimal('750.25'), 517.1666666666666, 1), ('Laptop', 'Electronics', Decimal('500.50'), 517.1666666666666, 2), ('Laptop', 'Electronics', Decimal('300.75'), 517.1666666666666, 3)]

**Explanation**: This example demonstrates advanced DuckDB techniques including multi-table JOIN, window functions (AVG and RANK), and analytical querying using the memory-based connection. It shows how to perform complex data analysis with concise SQL.
## Step 2: 1. Develop a more complex multi-table join example

```python
print('Error: Failed to generate response')
```

**Result**: [('Smartphone', 'Electronics', Decimal('750.25'), 517.1666666666666, 1), ('Laptop', 'Electronics', Decimal('500.50'), 517.1666666666666, 2), ('Laptop', 'Electronics', Decimal('300.75'), 517.1666666666666, 3)]

**Explanation**: Fallback due to repeated failures
## Step 3: 2. Showcase window function implementations

```python
import duckdb

# Window function demonstration with sales data
con = duckdb.connect(':memory:')

# Create and populate sales table
con.execute('''
    CREATE TABLE sales (
        sale_id INT, 
        product_name VARCHAR, 
        sale_amount DECIMAL(10,2), 
        sale_date DATE
    );

    INSERT INTO sales VALUES
    (1, 'Laptop', 1200.50, '2023-01-15'),
    (2, 'Smartphone', 800.25, '2023-02-20'),
    (3, 'Tablet', 600.75, '2023-03-10'),
    (4, 'Laptop', 1500.00, '2023-04-05');
''')

# Advanced window function query
result = con.execute('''
    SELECT 
        product_name,
        sale_amount,
        sale_date,
        SUM(sale_amount) OVER (PARTITION BY product_name ORDER BY sale_date) as cumulative_sales,
        AVG(sale_amount) OVER (PARTITION BY product_name) as product_avg_sale,
        RANK() OVER (ORDER BY sale_amount DESC) as sale_rank
    FROM sales
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Sale: ${row[1]}, Date: {row[2]}, Cumulative Sales: ${row[3]}, Avg Sale: ${row[4]:.2f}, Rank: {row[5]}")
```

**Result**: [('Laptop', Decimal('1500.00'), datetime.date(2023, 4, 5), Decimal('2700.50'), 1350.25, 1), ('Laptop', Decimal('1200.50'), datetime.date(2023, 1, 15), Decimal('1200.50'), 1350.25, 2), ('Smartphone', Decimal('800.25'), datetime.date(2023, 2, 20), Decimal('800.25'), 800.25, 3), ('Tablet', Decimal('600.75'), datetime.date(2023, 3, 10), Decimal('600.75'), 600.75, 4)]

**Explanation**: This example demonstrates multiple window functions in DuckDB: cumulative sum, average, and ranking across product sales, showcasing partitioning and ordering capabilities within window functions.
## Step 4: 3. Create a performance optimization comparison between SQL and relational API approaches

Failed after 3 attempts: This relation does not contain a column by the name of 'group_by'
## Step 5: 4. Implement a recursive query pattern

```python
import duckdb

con = duckdb.connect(':memory:')

# Create an employee hierarchy table
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
    (4, 'Senior Engineer', 2),
    (5, 'Junior Engineer', 4);
''')

# Recursive query to find entire management chain
result = con.execute('''
    WITH RECURSIVE management_chain AS (
        SELECT emp_id, name, manager_id, 0 as depth
        FROM employees
        WHERE emp_id = 5

        UNION ALL

        SELECT e.emp_id, e.name, e.manager_id, mc.depth + 1
        FROM employees e
        JOIN management_chain mc ON e.emp_id = mc.manager_id
    )
    SELECT name, depth FROM management_chain
    ORDER BY depth
''').fetchall()

for employee, level in result:
    print(f'Level {level}: {employee}')
```

**Result**: [('Junior Engineer', 0), ('Senior Engineer', 1), ('CTO', 2), ('CEO', 3)]

**Explanation**: Demonstrates a recursive Common Table Expression (CTE) in DuckDB to traverse an employee hierarchy, finding the complete management chain for a specific employee by recursively following manager relationships.
## Step 6: 5. Build an example that demonstrates data transformation techniques

```python
import duckdb

con = duckdb.connect(':memory:')

# Create source data
con.execute('''
    CREATE TABLE raw_transactions (
        transaction_id INT,
        amount DECIMAL(10,2),
        category VARCHAR,
        timestamp TIMESTAMP
    );

    INSERT INTO raw_transactions VALUES
    (1, 100.50, 'Groceries', '2023-01-15 10:30:00'),
    (2, 250.75, 'Electronics', '2023-02-20 14:45:00'),
    (3, 50.25, 'Groceries', '2023-03-10 09:15:00');
''')

# Data transformation query
transformed_data = con.execute('''
    SELECT 
        transaction_id,
        amount,
        category,
        DATE_TRUNC('month', timestamp) as month,
        CASE 
            WHEN amount < 100 THEN 'Low'
            WHEN amount BETWEEN 100 AND 200 THEN 'Medium'
            ELSE 'High'
        END as spend_category
    FROM raw_transactions
''').fetchall()

for row in transformed_data:
    print(f'Transaction: {row[0]}, Amount: ${row[1]}, Category: {row[2]}, Month: {row[3]}, Spend Level: {row[4]}')
```

**Result**: [('Junior Engineer', 0), ('Senior Engineer', 1), ('CTO', 2), ('CEO', 3)]

**Explanation**: Demonstrates data transformation techniques using DuckDB, including time-based truncation, categorical mapping, and data enrichment through CASE statements.
## Step 7: Which area would you like me to focus on next?

```python
import duckdb

# Performance-optimized analytical query with indexing
con = duckdb.connect(':memory:')

# Create large transaction table
con.execute('''
    CREATE TABLE large_transactions (
        transaction_id BIGINT,
        amount DECIMAL(15,2),
        category VARCHAR,
        timestamp TIMESTAMP
    );

    -- Create index for faster filtering
    CREATE INDEX category_idx ON large_transactions(category);
''')

# Complex analytical query demonstrating performance optimization
result = con.execute('''
    SELECT 
        category, 
        COUNT(*) as transaction_count,
        SUM(amount) as total_amount,
        AVG(amount) as avg_transaction
    FROM large_transactions
    WHERE timestamp BETWEEN '2023-01-01' AND '2023-12-31'
    GROUP BY category
    ORDER BY total_amount DESC
    LIMIT 5
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Transactions: {row[1]}, Total: ${row[2]}, Avg: ${row[3]:.2f}")
```

**Result**: None

**Explanation**: Demonstrates DuckDB performance optimization techniques using indexing, complex aggregations, and analytical query patterns for large-scale transaction analysis.
