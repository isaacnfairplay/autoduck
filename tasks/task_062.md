# Task: ```python
import duckdb

con = duckdb.connect()

# Transform numeric array by adding 10 to each element
rel = con.query('''
SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array
''')

print(rel.execute().fetchall())
```

This targeted implementation demonstrates DuckDB's array_transform capability by incrementing list elements, highlighting its flexible functional SQL querying approach.

## Step 1: ```python

**Generated by**: Anthropic

```python
import duckdb

# Create an in-memory database and connect
conn = duckdb.connect(':memory:')

# Create a table with sales data
conn.execute('''
    CREATE TABLE sales (
        product_id INTEGER,
        category VARCHAR,
        sale_amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
        (1, 'Electronics', 500.50),
        (2, 'Clothing', 250.75),
        (3, 'Electronics', 1200.00),
        (4, 'Books', 75.25),
        (5, 'Electronics', 350.00);
''')

# Perform window function to rank sales by category
result = conn.execute('''
    SELECT
        product_id,
        category,
        sale_amount,
        RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as category_rank
    FROM sales
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(3, 'Electronics', Decimal('1200.00'), 1), (1, 'Electronics', Decimal('500.50'), 2), (5, 'Electronics', Decimal('350.00'), 3), (4, 'Books', Decimal('75.25'), 1), (2, 'Clothing', Decimal('250.75'), 1)]

**Explanation**: Demonstrates window function (RANK) with partitioning by category, ranking sales within each product category by sale amount.
## Step 2: import duckdb

**Generated by**: Anthropic

```python
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a sample table of customer orders
conn.execute('''
    CREATE TABLE orders (
        order_id INTEGER,
        customer_id INTEGER,
        total_amount DECIMAL(10,2)
    );

    INSERT INTO orders VALUES
        (1, 101, 150.50),
        (2, 102, 275.25),
        (3, 101, 89.99),
        (4, 103, 450.00);
''')

# Use window function to calculate running total for each customer
result = conn.execute('''
    SELECT 
        order_id, 
        customer_id, 
        total_amount,
        SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_id) as cumulative_total
    FROM orders
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(2, 102, Decimal('275.25'), Decimal('275.25')), (1, 101, Decimal('150.50'), Decimal('150.50')), (3, 101, Decimal('89.99'), Decimal('240.49')), (4, 103, Decimal('450.00'), Decimal('450.00'))]

**Explanation**: Demonstrates a window function (SUM OVER) to calculate a running total of order amounts for each customer, showing how DuckDB supports advanced analytical queries with simple syntax.
## Step 3: con = duckdb.connect()

**Generated by**: Anthropic

```python
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create time series data with temperature measurements
conn.execute('''
    CREATE TABLE weather_data (
        timestamp TIMESTAMP,
        city VARCHAR,
        temperature FLOAT
    );

    INSERT INTO weather_data VALUES
        ('2023-06-01 10:00:00', 'New York', 72.5),
        ('2023-06-01 11:00:00', 'New York', 75.2),
        ('2023-06-01 12:00:00', 'New York', 77.0),
        ('2023-06-01 10:00:00', 'Los Angeles', 68.3),
        ('2023-06-01 11:00:00', 'Los Angeles', 69.7);
''');

# Calculate moving average of temperature with 2-hour window
result = conn.execute('''
    SELECT 
        timestamp, 
        city, 
        temperature,
        AVG(temperature) OVER (
            PARTITION BY city 
            ORDER BY timestamp 
            RANGE BETWEEN INTERVAL 1 HOUR PRECEDING AND INTERVAL 1 HOUR FOLLOWING
        ) as temperature_moving_avg
    FROM weather_data
''').fetchall()

for row in result:
    print(row)
```

**Result**: [(datetime.datetime(2023, 6, 1, 10, 0), 'Los Angeles', 68.30000305175781, 69.0), (datetime.datetime(2023, 6, 1, 11, 0), 'Los Angeles', 69.69999694824219, 69.0), (datetime.datetime(2023, 6, 1, 10, 0), 'New York', 72.5, 73.8499984741211), (datetime.datetime(2023, 6, 1, 11, 0), 'New York', 75.19999694824219, 74.89999898274739), (datetime.datetime(2023, 6, 1, 12, 0), 'New York', 77.0, 76.0999984741211)]

**Explanation**: Demonstrates a time series window function using a moving average calculation with temporal partitioning and windowing.
## Step 4: # Transform numeric array by adding 10 to each element

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create array and transform elements
result = conn.execute("""
    SELECT [1, 2, 3, 4, 5] as original_array,
           array_transform([1, 2, 3, 4, 5], x -> x + 10) as transformed_array
""").fetchone()

print(f"Original Array: {result[0]}")
print(f"Transformed Array: {result[1]}")
```

**Result**: ([1, 2, 3, 4, 5], [11, 12, 13, 14, 15])

**Explanation**: Demonstrates DuckDB's array_transform function to add 10 to each element, showcasing functional array manipulation in a single SQL statement
## Step 5: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a table with employee data
conn.execute('''
    CREATE TABLE employees (
        id INTEGER,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    );

    INSERT INTO employees VALUES
        (1, 'Alice', 'Sales', 55000.00),
        (2, 'Bob', 'Marketing', 60000.00),
        (3, 'Charlie', 'Sales', 52000.00),
        (4, 'David', 'Marketing', 65000.00);
''')

# Perform lateral join to get top 2 salaries per department
result = conn.execute('''
    SELECT 
        e.department, 
        e.name, 
        e.salary
    FROM employees e,
    LATERAL (
        SELECT name, salary
        FROM employees
        WHERE department = e.department
        ORDER BY salary DESC
        LIMIT 2
    ) top_salaries
    GROUP BY e.department, e.name, e.salary
    ORDER BY e.department, e.salary DESC
''').fetchall()

for row in result:
    print(row)
```

**Result**: [('Marketing', 'David', Decimal('65000.00')), ('Marketing', 'Bob', Decimal('60000.00')), ('Sales', 'Alice', Decimal('55000.00')), ('Sales', 'Charlie', Decimal('52000.00'))]

**Explanation**: Demonstrates a lateral join to find the top 2 highest-paid employees in each department using a subquery that correlates with the outer query's department. This showcases DuckDB's support for lateral joins and correlated subqueries.
## Step 6: SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array").fetchone()
print(result[0])
```

**Result**: ([11, 12, 13, 14],)

**Explanation**: Uses array_transform() to increment each array element by 10, demonstrating DuckDB's array manipulation capabilities
## Step 7: ''')

**Generated by**: Anthropic

```python
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create and populate table with geographic data
conn.execute('''
    CREATE TABLE countries (
        name VARCHAR,
        continent VARCHAR,
        population INTEGER
    );

    INSERT INTO countries VALUES
        ('USA', 'North America', 331000000),
        ('China', 'Asia', 1439323776),
        ('Brazil', 'South America', 212559417),
        ('India', 'Asia', 1380004385);
''')

# Use QUALIFY window function to select top country by population per continent
result = conn.execute('''
    SELECT name, continent, population
    FROM (
        SELECT 
            name, 
            continent, 
            population,
            RANK() OVER (PARTITION BY continent ORDER BY population DESC) as pop_rank
        FROM countries
    ) ranked_countries
    WHERE pop_rank = 1
''').fetchall()

for row in result:
    print(row)
```

**Result**: [('Brazil', 'South America', 212559417), ('China', 'Asia', 1439323776), ('USA', 'North America', 331000000)]

**Explanation**: Demonstrates a window function (RANK) with QUALIFY to find the most populous country in each continent by partitioning and ranking population data.
## Step 8: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.table('duckdb_tables')
print(rel.execute().fetchall())
```

**Result**: [('Brazil', 'South America', 212559417), ('China', 'Asia', 1439323776), ('USA', 'North America', 331000000)]

**Explanation**: Retrieves and prints system table metadata for all tables in the current DuckDB connection using the relational API's table() method
## Step 9: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create nested data and extract substructures
result = conn.execute("""
    SELECT 
        {'name': 'Alice', 'skills': ['Python', 'SQL']} as person,
        person['name'] as extracted_name,
        person['skills'][1] as second_skill
""").fetchone()

print(f"Full Person: {result[0]}")
print(f"Name: {result[1]}")
print(f"Second Skill: {result[2]}")
```

**Result**: ({'name': 'Alice', 'skills': ['Python', 'SQL']}, 'Alice', 'Python')

**Explanation**: Demonstrates DuckDB's ability to work with nested JSON-like structures, showing object and array access within a single SQL query. Highlights the flexibility of DuckDB in handling complex data types.
## Step 10: This targeted implementation demonstrates DuckDB's array_transform capability by incrementing list elements, highlighting its flexible functional SQL querying approach.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT array_transform([5, 10, 15, 20], x -> x * 2) as doubled_array").fetchone()
print(result[0])
```

**Result**: ([10, 20, 30, 40],)

**Explanation**: Demonstrates array_transform by doubling each element in a list using an anonymous lambda function, showcasing DuckDB's functional array manipulation capabilities
