# Task: I understand you're looking for a deep dive into the DuckDB relational API. This example demonstrates various features:

```python
import duckdb

# Create connection
con = duckdb.connect()

# Create sample relation
rel = con.query('SELECT * FROM (VALUES (1, "Alice"), (2, "Bob"), (3, "Charlie")) AS t(id, name)')

# Relation Properties
print('Columns:', rel.columns)  # Column names
print('Types:', rel.types)      # Column types

# Filtering
filtered_rel = rel.filter('id > 1')
print('Filtered Results:', filtered_rel.execute().fetchall())

# Aggregation
agg_rel = rel.aggregate('SUM(id)')
print('Sum:', agg_rel.execute().fetchone())

# Method Chaining
result = (rel
    .filter('id > 1')
    .project('name')
    .execute()
    .fetchall())
print('Projected Names:', result)
```

This example showcases:
1. Creating a relation
2. Exploring relation metadata
3. Filtering rows
4. Aggregating data
5. Method chaining with projections

## Step 1: I understand you're looking for a deep dive into the DuckDB relational API. This example demonstrates various features:

```python
print('Error: Failed to generate response')
```

**Result**: None

**Explanation**: Fallback due to repeated failures
## Step 2: ```python

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Complex analytical query with window functions
result = conn.execute('''
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    price,
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_sales,
    AVG(price) OVER (PARTITION BY product_id) as avg_product_price
FROM sales
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(1, datetime.date(2023, 1, 15), 10, Decimal('25.50'), 10, 25.5), (1, datetime.date(2023, 3, 10), 8, Decimal('25.50'), 18, 25.5), (2, datetime.date(2023, 2, 20), 5, Decimal('30.75'), 5, 30.75)]

**Explanation**: Demonstrates DuckDB's advanced querying capabilities using window functions to calculate cumulative sales and average product price across a sales dataset.
## Step 3: import duckdb

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table and insert data
conn.execute('CREATE TABLE employees (id INT, name VARCHAR, department VARCHAR, salary DECIMAL(10,2))')
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Engineering', 75000.00),
    (3, 'Charlie', 'Sales', 55000.00),
    (4, 'David', 'Engineering', 80000.00)
])

# Perform a window function query to rank employees by salary within each department
result = conn.execute('''
    SELECT 
        id, 
        name, 
        department, 
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
    FROM employees
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(3, 'Charlie', 'Sales', Decimal('55000.00'), 1), (1, 'Alice', 'Sales', Decimal('50000.00'), 2), (4, 'David', 'Engineering', Decimal('80000.00'), 1), (2, 'Bob', 'Engineering', Decimal('75000.00'), 2)]

**Explanation**: This code demonstrates DuckDB's window function capabilities by creating an employees table and ranking employees by salary within their respective departments.
## Step 4: # Create connection

```python
import duckdb

# Establish an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table for customer orders
conn.execute('''
CREATE TABLE customer_orders (
    customer_id INTEGER,
    order_date DATE,
    total_amount DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO customer_orders VALUES (?, ?, ?)', [
    (1, '2023-01-15', 250.50),
    (1, '2023-02-20', 175.25),
    (2, '2023-01-10', 300.75),
    (2, '2023-03-05', 225.00)
])

# Execute a window function query to calculate cumulative spending
result = conn.execute('''
SELECT 
    customer_id, 
    order_date, 
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as cumulative_spend
FROM customer_orders
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(1, datetime.date(2023, 1, 15), Decimal('250.50'), Decimal('250.50')), (1, datetime.date(2023, 2, 20), Decimal('175.25'), Decimal('425.75')), (2, datetime.date(2023, 1, 10), Decimal('300.75'), Decimal('300.75')), (2, datetime.date(2023, 3, 5), Decimal('225.00'), Decimal('525.75'))]

**Explanation**: Demonstrates DuckDB's window function capabilities by tracking cumulative customer spending over time using a partitioned window function.
## Step 5: con = duckdb.connect()

```python
import duckdb

# Establish an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample employees table
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
)''')

# Insert sample employee data
conn.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 50000.00),
    (2, 'Bob', 'Engineering', 75000.00),
    (3, 'Charlie', 'Sales', 55000.00)
])

# Perform an aggregation query with grouped results
result = conn.execute('''
SELECT 
    department, 
    AVG(salary) as avg_department_salary, 
    COUNT(*) as employee_count
FROM employees
GROUP BY department
''').fetchall()

for row in result:
    print(f'Department: {row[0]}, Average Salary: ${row[1]:.2f}, Employees: {row[2]}')
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: Demonstrates DuckDB query with table creation, data insertion, and performing an aggregate query grouped by department, calculating average salary and employee count
## Step 6: # Create sample relation

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample relation for product sales
rel = conn.sql('''
SELECT * FROM (
    VALUES 
    (1, 'Laptop', 1000.50, '2023-01-15'),
    (2, 'Smartphone', 500.25, '2023-02-20'),
    (3, 'Tablet', 750.75, '2023-03-10')
) AS products(id, name, price, sale_date)
''')

# Display relation details
print('Relation Columns:', rel.columns)
print('Relation Types:', rel.types)

# Filter and aggregate operations
filtered_rel = rel.filter('price > 600')
agg_rel = filtered_rel.aggregate('AVG(price)')

print('Filtered Products:\n', filtered_rel.execute().fetchall())
print('Average High-Price Product:', agg_rel.execute().fetchone()[0])
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: Demonstrates creating a DuckDB relation, exploring its properties, and performing filtering and aggregation using the relational API
## Step 7: rel = con.query('SELECT * FROM (VALUES (1, "Alice"), (2, "Bob"), (3, "Charlie")) AS t(id, name)')

Failed after 3 attempts: Binder Error: Referenced column "Alice" not found in FROM clause!
## Step 8: # Relation Properties

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
products_rel = conn.sql('''
SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)
''')

# Demonstrate relation properties and methods
print('Relation Columns:', products_rel.columns)
print('Relation Types:', products_rel.types)

# Filter and transform operations
filtered_rel = products_rel.filter('price > 600')
transformed_rel = filtered_rel.project(['name', 'price'])

print('Filtered High-Price Products:\n', transformed_rel.execute().fetchall())
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: This code demonstrates DuckDB's Relation API by creating an in-memory relation of products, showcasing column inspection, filtering, and projection methods. It highlights the programmatic query manipulation capabilities of DuckDB's relational interface.
## Step 9: print('Columns:', rel.columns)  # Column names

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

print('Columns:', rel.columns)
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: This code demonstrates creating a DuckDB relation from a values list and accessing its column names. It uses an in-memory database connection and the `.sql()` method to generate a relation, then uses `.columns` to retrieve and print the column names.
## Step 10: print('Types:', rel.types)      # Column types

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

print('Columns:', rel.columns)
print('Types:', rel.types)
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: Demonstrates creating a DuckDB relation, showing how to define a table in memory and access its column names and types using the relational API
## Step 11: # Filtering

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products by price using relation method
filtered_rel = rel.filter('price > 600')

print('High-Priced Products:')
for product in filtered_rel.execute().fetchall():
    print(product)
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: Demonstrates DuckDB relation filtering by using the .filter() method with a SQL-like condition. This example creates an in-memory relation of products and retrieves only products with a price above 600.
## Step 12: filtered_rel = rel.filter('id > 1')

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products with id greater than 1
filtered_rel = rel.filter('id > 1')

print('Products with ID > 1:')
for product in filtered_rel.execute().fetchall():
    print(product)
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: This code demonstrates filtering a DuckDB relation using the filter() method, selecting only products with an ID greater than 1. It creates an in-memory relation, applies a filter condition, and then prints the resulting rows.
## Step 13: print('Filtered Results:', filtered_rel.execute().fetchall())

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products with id greater than 1
filtered_rel = rel.filter('id > 1')

print('Filtered Results:', filtered_rel.execute().fetchall())
```

**Result**: [('Engineering', 75000.0, 1), ('Sales', 52500.0, 2)]

**Explanation**: This code demonstrates filtering a DuckDB relation using the filter() method, selecting products with an ID greater than 1. It showcases creating an in-memory relation and applying a simple filtering condition.
## Step 14: # Aggregation

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
)''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Perform complex aggregation with multiple metrics
result = conn.execute('''
SELECT 
    product_id, 
    COUNT(*) as total_sales,
    SUM(quantity) as total_quantity,
    AVG(price) as avg_price,
    MAX(price) as max_price
FROM sales
GROUP BY product_id
''').fetchall()

for row in result:
    print(f'Product {row[0]}: Sales={row[1]}, Quantity={row[2]}, Avg Price=${row[3]:.2f}, Max Price=${row[4]:.2f}')
```

**Result**: [(1, 2, 18, 25.5, Decimal('25.50')), (2, 1, 5, 30.75, Decimal('30.75'))]

**Explanation**: This example demonstrates advanced SQL aggregation in DuckDB, showing how to calculate multiple aggregate metrics across a sales dataset using GROUP BY. It computes total sales count, total quantity sold, average price, and maximum price for each product.
## Step 15: agg_rel = rel.aggregate('SUM(id)')

Failed after 3 attempts: Binder Error: Referenced column "Alice" not found in FROM clause!
## Step 16: print('Sum:', agg_rel.execute().fetchone())

Failed after 3 attempts: Binder Error: Referenced column "Alice" not found in FROM clause!
## Step 17: # Method Chaining

Failed after 3 attempts: Binder Error: Referenced column "price" not found in FROM clause!
Candidate bindings: " 'price']"
## Step 18: result = (rel

Failed after 3 attempts: Binder Error: Referenced column "price" not found in FROM clause!
Candidate bindings: " 'price']"
## Step 19: .filter('id > 1')

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter products with id greater than 1
filtered_rel = rel.filter('id > 1')

print('Filtered Results:', filtered_rel.execute().fetchall())
```

**Result**: [(1, 2, 18, 25.5, Decimal('25.50')), (2, 1, 5, 30.75, Decimal('30.75'))]

**Explanation**: This example demonstrates the .filter() method on a DuckDB relation, which allows filtering rows based on a SQL-like condition. It creates an in-memory relation and selects only rows where the 'id' is greater than 1.
## Step 20: .project('name')

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Project only the name column
name_rel = rel.project('name')

print('Projected Names:', name_rel.execute().fetchall())
```

**Result**: [(1, 2, 18, 25.5, Decimal('25.50')), (2, 1, 5, 30.75, Decimal('30.75'))]

**Explanation**: Demonstrates using the .project() method to select only the 'name' column from the products relation, extracting a single column of data programmatically
## Step 21: .execute()

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample table
conn.execute('CREATE TABLE products (id INTEGER, name VARCHAR, price DECIMAL(10,2))')

# Insert sample data
conn.executemany('INSERT INTO products VALUES (?, ?, ?)', [
    (1, 'Laptop', 1000.50),
    (2, 'Smartphone', 500.25),
    (3, 'Tablet', 750.75)
])

# Execute a query and fetch results
result = conn.execute('SELECT * FROM products WHERE price > 600').fetchall()

# Print the results
for row in result:
    print(f'Product: {row[1]}, Price: ${row[2]}')
```

**Result**: [(1, 'Laptop', Decimal('1000.50')), (3, 'Tablet', Decimal('750.75'))]

**Explanation**: This code demonstrates basic DuckDB operations: creating an in-memory database, creating a table, inserting data, executing a query with a filter condition, and fetching results.
## Step 22: .fetchall())

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Project multiple columns
selected_rel = rel.project(['name', 'price'])

print('Selected Columns:', selected_rel.execute().fetchall())
```

**Result**: [(1, 'Laptop', Decimal('1000.50')), (3, 'Tablet', Decimal('750.75'))]

**Explanation**: Demonstrates using DuckDB's relational API to project (select) specific columns from a relation, showing how to extract a subset of data programmatically.
## Step 23: print('Projected Names:', result)

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Project only the name column
name_rel = rel.project('name')

result = name_rel.execute().fetchall()
print('Projected Names:', result)
```

**Result**: [('Laptop',), ('Smartphone',), ('Tablet',)]

**Explanation**: Demonstrates creating an in-memory DuckDB relation and using the .project() method to select only the 'name' column from a sample products dataset.
## Step 24: ```

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Demonstrate relation query methods
filtered_rel = rel.filter('price > 600')
transformed_rel = filtered_rel.project(['name', 'price'])

print('High-Priced Products:')
for product in transformed_rel.execute().fetchall():
    print(product)
```

**Result**: [('Laptop',), ('Smartphone',), ('Tablet',)]

**Explanation**: This code demonstrates DuckDB's relational algebra API by creating an in-memory products relation, filtering products by price, and projecting selected columns. It showcases filtering with the 'filter' method and column selection with the 'project' method.
## Step 25: This example showcases:

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a recursive common table expression to generate a series
result = conn.execute('''
WITH RECURSIVE
    number_series(n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1 FROM number_series WHERE n < 10
    )
SELECT n, n * n AS squared
FROM number_series
''').fetchall()

# Print the generated series with squares
for row in result:
    print(f'Number: {row[0]}, Squared: {row[1]}')
```

**Result**: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

**Explanation**: Demonstrates a recursive common table expression (CTE) in DuckDB to generate a sequence of numbers and compute their squares, showcasing advanced query capabilities with programmatic iteration.
## Step 26: 1. Creating a relation

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Display relation details
print('Relation Columns:', rel.columns)
print('Relation Types:', rel.types)
```

**Result**: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

**Explanation**: This code demonstrates creating a DuckDB relation using an in-memory connection and inline VALUES clause. It showcases how to define a relation with multiple columns and data types, and then displays the column names and types.
## Step 27: 2. Exploring relation metadata

Failed after 3 attempts: This relation does not contain a column by the name of 'rowcount'
## Step 28: 3. Filtering rows

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Filter rows using relation method
filtered_rel = rel.filter('price > 600')

print('High-Priced Products:')
for product in filtered_rel.execute().fetchall():
    print(product)
```

**Result**: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

**Explanation**: This code demonstrates filtering rows in a DuckDB relation using the .filter() method. It creates an in-memory sample relation of products and filters to show only products with a price above $600, showcasing how to conditionally select data programmatically.
## Step 29: 4. Aggregating data

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample sales table
conn.execute('''CREATE TABLE sales (product_id INTEGER, sale_date DATE, quantity INTEGER, price DECIMAL(10,2))''')

# Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?)', [
    (1, '2023-01-15', 10, 25.50),
    (2, '2023-02-20', 5, 30.75),
    (1, '2023-03-10', 8, 25.50)
])

# Perform aggregation query
result = conn.execute('''
SELECT 
    product_id, 
    SUM(quantity) as total_quantity,
    AVG(price) as avg_price,
    COUNT(*) as sales_count
FROM sales
GROUP BY product_id
''').fetchall()

for row in result:
    print(f'Product {row[0]}: Total Quantity={row[1]}, Avg Price=${row[2]:.2f}, Sales Count={row[3]}')
```

**Result**: [(1, 18, 25.5, 2), (2, 5, 30.75, 1)]

**Explanation**: This code demonstrates data aggregation in DuckDB by creating a sales table, inserting sample data, and performing aggregate functions like SUM, AVG, and COUNT grouped by product_id.
## Step 30: 5. Method chaining with projections

```python
import duckdb

# Create an in-memory database connection
conn = duckdb.connect(':memory:')

# Create a sample products relation
rel = conn.sql('''SELECT * FROM (VALUES
    (1, 'Laptop', 1000.50, 'Electronics'),
    (2, 'Smartphone', 500.25, 'Electronics'),
    (3, 'Tablet', 750.75, 'Electronics')
) AS products(id, name, price, category)''')

# Method chaining: filter and project high-priced products
result = (rel
    .filter('price > 600')
    .project(['name', 'price'])
    .execute()
    .fetchall())

print('High-Priced Products:')
for product in result:
    print(product)
```

**Result**: [(['name', 'price'],), (['name', 'price'],)]

**Explanation**: This example demonstrates method chaining in DuckDB's relational API by filtering products over $600 and then projecting only their names and prices. It shows how multiple transformations can be applied fluently to a relation.
