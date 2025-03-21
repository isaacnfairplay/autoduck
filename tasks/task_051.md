# Task: Here's a targeted DuckDB example showcasing array_transform for list element transformation:

```python
import duckdb

con = duckdb.connect()

# Transform numeric array by squaring values
rel = con.query('''
SELECT array_transform([2, 3, 4, 5], x -> x * x) as squared_array
''')

print(rel.execute().fetchall())
```

This concise implementation demonstrates DuckDB's array transformation capability by squaring list elements, highlighting its flexible functional SQL querying approach.

## Step 1: Here's a targeted DuckDB example showcasing array_transform for list element transformation:

**Generated by**: Anthropic

```python
import duckdb

# Create a connection
conn = duckdb.connect(':memory:')

# Create table with list column
conn.execute('CREATE TABLE numbers (values INTEGER[])')
conn.execute("INSERT INTO numbers VALUES ([1,2,3,4]), ([5,6,7,8])")

# Use array_transform to square each list element
result = conn.execute("SELECT array_transform(values, x -> x * x) as squared_values FROM numbers").fetchall()

print(result)
```

**Result**: [([1, 4, 9, 16],), ([25, 36, 49, 64],)]

**Explanation**: Demonstrates DuckDB's array_transform function, which applies a lambda-like transformation to each element of a list column, squaring the values in this example.
## Step 2: ```python

**Generated by**: Anthropic

```python
import duckdb

# Create a connection
conn = duckdb.connect(':memory:')

# Create sample sales data with window functions
conn.execute('''
CREATE TABLE sales (
    product VARCHAR,
    region VARCHAR,
    sales_amount DECIMAL
);

INSERT INTO sales VALUES
    ('Laptop', 'North', 1000),
    ('Laptop', 'South', 1500),
    ('Phone', 'North', 800),
    ('Phone', 'South', 1200),
    ('Tablet', 'North', 600),
    ('Tablet', 'South', 900);
''')

# Calculate cumulative sales and rank products within each region
result = conn.execute('''
SELECT 
    product, 
    region, 
    sales_amount,
    SUM(sales_amount) OVER (PARTITION BY region ORDER BY sales_amount) as cumulative_sales,
    RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as product_rank
FROM sales
''').fetchall()

for row in result:
    print(row)

```

**Result**: [('Laptop', 'South', Decimal('1500.000'), Decimal('3600.000'), 1), ('Phone', 'South', Decimal('1200.000'), Decimal('2100.000'), 2), ('Tablet', 'South', Decimal('900.000'), Decimal('900.000'), 3), ('Laptop', 'North', Decimal('1000.000'), Decimal('2400.000'), 1), ('Phone', 'North', Decimal('800.000'), Decimal('1400.000'), 2), ('Tablet', 'North', Decimal('600.000'), Decimal('600.000'), 3)]

**Explanation**: Demonstrates window functions in DuckDB: calculating cumulative sales and ranking products within regions using PARTITION BY and window aggregate functions.
## Step 3: import duckdb

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a table with time series data
conn.execute('''
CREATE TABLE stock_prices (
    date DATE,
    symbol VARCHAR,
    price DECIMAL(10,2),
    volume INTEGER
);

INSERT INTO stock_prices VALUES
    ('2023-01-01', 'AAPL', 150.25, 1000000),
    ('2023-01-02', 'AAPL', 152.50, 1200000),
    ('2023-01-03', 'AAPL', 149.75, 900000),
    ('2023-01-01', 'GOOGL', 100.50, 500000),
    ('2023-01-02', 'GOOGL', 102.25, 550000);
'''
)

# Calculate 2-day moving average of stock prices
result = conn.execute('''
SELECT 
    date, 
    symbol, 
    price,
    AVG(price) OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM stock_prices
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(datetime.date(2023, 1, 1), 'GOOGL', Decimal('100.50'), 100.5), (datetime.date(2023, 1, 2), 'GOOGL', Decimal('102.25'), 101.375), (datetime.date(2023, 1, 1), 'AAPL', Decimal('150.25'), 150.25), (datetime.date(2023, 1, 2), 'AAPL', Decimal('152.50'), 151.375), (datetime.date(2023, 1, 3), 'AAPL', Decimal('149.75'), 151.125)]

**Explanation**: Demonstrates using window functions to calculate a 2-day moving average of stock prices across different symbols, showcasing DuckDB's time series and analytical capabilities.
## Step 4: con = duckdb.connect()

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table of employees
conn.execute('''
CREATE TABLE employees (
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'Marketing', 55000),
    (3, 'Charlie', 'Sales', 52000),
    (4, 'David', 'Marketing', 60000);
'''
)

# Demonstrate group-level aggregation with filtering
result = conn.execute('''
SELECT 
    department, 
    AVG(salary) as avg_salary,
    COUNT(*) as employee_count
FROM employees
GROUP BY department
HAVING AVG(salary) > 52000
''').fetchall()

for row in result:
    print(row)
```

**Result**: [('Marketing', 57500.0, 2)]

**Explanation**: This example demonstrates DuckDB's group-level aggregation with HAVING clause filtering, showing average salary and employee count for departments with average salaries above $52,000.
## Step 5: # Transform numeric array by squaring values

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create list array and square each element
result = conn.execute("""
WITH nums(values) AS (VALUES ([1,2,3,4,5]))
SELECT array_transform(values, x -> x * x) as squared_values FROM nums
""").fetchall()

print(result)
```

**Result**: [([1, 4, 9, 16, 25],)]

**Explanation**: Demonstrates array transformation using array_transform() to square each numeric element in a list, showcasing DuckDB's inline function application on array data types.
## Step 6: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a sample table of customer orders
conn.execute('''
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    product VARCHAR,
    order_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO orders VALUES
    (1, 101, 'Widget', '2023-01-15', 50.00),
    (2, 102, 'Gadget', '2023-02-20', 75.50),
    (3, 101, 'Sprocket', '2023-03-10', 25.75);
''')

# Demonstrate nested subquery with multiple aggregations
result = conn.execute('''
WITH customer_totals AS (
    SELECT 
        customer_id, 
        SUM(amount) as total_spend,
        COUNT(order_id) as order_count
    FROM orders
    GROUP BY customer_id
)
SELECT 
    customer_id, 
    total_spend,
    order_count,
    total_spend / order_count as avg_order_value
FROM customer_totals
WHERE total_spend > (
    SELECT AVG(total_spend) FROM customer_totals
)
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(101, Decimal('75.75'), 2, 37.875)]

**Explanation**: Demonstrates a nested subquery with multiple levels of aggregation, calculating customer spend metrics and filtering based on an aggregate comparison. Shows advanced SQL querying capabilities in DuckDB with common table expressions (CTE), multiple aggregations, and subquery filtering.
## Step 7: SELECT array_transform([2, 3, 4, 5], x -> x * x) as squared_array

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([2, 3, 4, 5], x -> x * x) as squared_array").fetchall()
print(result)
```

**Result**: [([4, 9, 16, 25],)]

**Explanation**: Uses array_transform() to square each element in a list, demonstrating DuckDB's array manipulation capabilities with a lambda function
## Step 8: ''')

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory connection
conn = duckdb.connect(':memory:')

# Create a recursive common table expression to generate a Fibonacci sequence
result = conn.execute('''
WITH RECURSIVE fibonacci(n, current, next) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, next, current + next
    FROM fibonacci
    WHERE n < 10
)
SELECT current AS fibonacci_number FROM fibonacci
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(0,), (1,), (1,), (2,), (3,), (5,), (8,), (13,), (21,), (34,)]

**Explanation**: This example demonstrates a recursive CTE (Common Table Expression) to generate the first 10 Fibonacci numbers using DuckDB's advanced SQL capabilities, showing how complex sequences can be computed directly in a query
## Step 9: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE users (id INTEGER, name VARCHAR)')
conn.execute("INSERT INTO users VALUES (1, 'Alice'), (2, 'Bob')")
rel = conn.table('users').filter('id > 0')
print(rel.execute().fetchall())
```

**Result**: [(0,), (1,), (1,), (2,), (3,), (5,), (8,), (13,), (21,), (34,)]

**Explanation**: Creates an in-memory table, inserts two rows, uses relational API to filter rows where id is positive, and prints the result set
## Step 10: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Generate unique sequence of prime numbers using recursive CTE
result = conn.execute('''
WITH RECURSIVE primes(n, candidate) AS (
    SELECT 2, 3
    UNION ALL
    SELECT n + 1, candidate + 2
    FROM primes
    WHERE NOT EXISTS (
        SELECT 1 FROM primes p2 
        WHERE p2.n < primes.n AND candidate % p2.candidate = 0
    ) AND n < 10
)
SELECT candidate FROM primes
''').fetchall()

for prime in result:
    print(prime[0])
```

**Result**: [(3,), (5,), (7,), (9,), (11,), (13,), (15,), (17,), (19,)]

**Explanation**: Demonstrates a recursive CTE for generating prime numbers by checking divisibility, showcasing DuckDB's support for complex, algorithmic SQL queries with recursive logic
## Step 11: This concise implementation demonstrates DuckDB's array transformation capability by squaring list elements, highlighting its flexible functional SQL querying approach.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([1,2,3,4,5], x -> x * x) as squared_values").fetchall()
print(result)
```

**Result**: [([1, 4, 9, 16, 25],)]

**Explanation**: Demonstrates DuckDB's array_transform function by creating an in-memory database and using a functional transformation to square list elements, showcasing the built-in array manipulation capabilities.
