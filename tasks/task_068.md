# Task: I'll create a focused example demonstrating DuckDB's array_transform function for list manipulation:

```python
import duckdb

con = duckdb.connect()

# Transform numeric array by adding 10 to each element
rel = con.query('''
SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array
''')

print(rel.execute().fetchall())
```

This targeted implementation showcases DuckDB's array_transform capability by incrementing list elements, highlighting its flexible functional SQL querying approach.

## Step 1: I'll create a focused example demonstrating DuckDB's array_transform function for list manipulation:

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with array column
conn.sql("""
CREATE TABLE numbers (nums INTEGER[]);

INSERT INTO numbers VALUES
([1, 2, 3]), 
([4, 5, 6]), 
([7, 8, 9]);

SELECT nums, array_transform(nums, x -> x * 2) AS doubled_nums
FROM numbers;
""").show()
```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates DuckDB's array_transform function by doubling each element in integer arrays using a lambda function. Shows how to manipulate list columns with functional-style transformations.
## Step 2: ```python

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.sql("""
CREATE TABLE sales (
    product_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price DECIMAL(10,2)
);

INSERT INTO sales VALUES
(1, '2023-01-15', 5, 10.50),
(1, '2023-02-20', 3, 10.50),
(2, '2023-01-22', 2, 25.00),
(2, '2023-03-10', 4, 25.00);

-- Calculate running total of sales by product using window function
SELECT 
    product_id, 
    sale_date, 
    quantity, 
    SUM(quantity * price) OVER (PARTITION BY product_id ORDER BY sale_date) AS cumulative_sales
FROM sales
ORDER BY product_id, sale_date;
""")
```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates a window function calculating cumulative sales per product over time, showcasing DuckDB's ability to perform advanced analytical queries with partition and ordered window functions.
## Step 3: import duckdb

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.sql("""
CREATE TABLE cities (
    city_name VARCHAR,
    population INTEGER,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

INSERT INTO cities VALUES
('New York', 8400000, 40.7128, -74.0060),
('Los Angeles', 3900000, 34.0522, -118.2437),
('Chicago', 2700000, 41.8781, -87.6298);

-- Find cities within a bounding box using spatial predicate
SELECT city_name, population
FROM cities
WHERE latitude BETWEEN 30 AND 45
  AND longitude BETWEEN -120 AND -70;
""").show()

```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates creating a geographic table and performing a spatial query by filtering cities within a specific latitude and longitude range using simple SQL predicates.
## Step 4: con = duckdb.connect()

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate a table with product inventory
conn.sql("""
CREATE TABLE inventory (
    product_id INTEGER,
    warehouse_id INTEGER,
    stock_quantity INTEGER
);

INSERT INTO inventory VALUES
(1, 101, 500),
(1, 102, 750),
(2, 101, 250),
(2, 103, 350);

-- Calculate total stock per product using group by and sum
SELECT 
    product_id, 
    SUM(stock_quantity) AS total_stock,
    COUNT(DISTINCT warehouse_id) AS warehouse_count
FROM inventory
GROUP BY product_id
HAVING total_stock > 500;
""").show()
```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates grouping, aggregation, and filtering of inventory data across multiple warehouses, showing how to calculate total stock per product and count unique warehouses while applying a HAVING clause to filter results
## Step 5: # Transform numeric array by adding 10 to each element

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table with numeric arrays
conn.sql("""
CREATE TABLE numeric_arrays (nums INTEGER[]);

INSERT INTO numeric_arrays VALUES
([1, 2, 3]), 
([4, 5, 6]), 
([7, 8, 9]);

SELECT nums, array_transform(nums, x -> x + 10) AS transformed_nums
FROM numeric_arrays;
""").show()
```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates array_transform() function to add 10 to each array element using DuckDB's SQL syntax with lambda transformation
## Step 6: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a graph-like dataset of users and connections
conn.sql("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE connections (
    user_id INTEGER,
    connected_user_id INTEGER
);

INSERT INTO users VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');

INSERT INTO connections VALUES
(1, 2), (1, 3),
(2, 1), (2, 4),
(3, 1), (4, 2);

-- Demonstrate recursive query to find network connections
WITH RECURSIVE network(user_id, depth) AS (
    SELECT user_id, 0 FROM users WHERE name = 'Alice'
    UNION ALL
    SELECT c.connected_user_id, n.depth + 1
    FROM connections c
    JOIN network n ON c.user_id = n.user_id
    WHERE depth < 2
)
SELECT DISTINCT u.name, network.depth
FROM network
JOIN users u ON network.user_id = u.user_id;
""").show()
```

**Result**: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]

**Explanation**: Demonstrates DuckDB's recursive query capabilities by exploring a social network connection graph, finding users connected to 'Alice' within 2 degrees of separation
## Step 7: SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql('SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array').fetchone()[0]
print(result)
```

**Result**: [11, 12, 13, 14]

**Explanation**: Uses DuckDB's SQL array_transform() function to increment each array element by 10, demonstrating inline lambda transformation of array elements.
## Step 8: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a product reviews table with sentiment analysis
conn.sql("""
CREATE TABLE reviews (
    product_id INTEGER,
    review_text VARCHAR,
    rating DECIMAL(2,1)
);

INSERT INTO reviews VALUES
(1, 'Great product!', 4.5),
(1, 'Amazing quality', 5.0),
(2, 'Not impressed', 2.0);

-- Calculate average rating and count of reviews per product
SELECT 
    product_id, 
    ROUND(AVG(rating), 1) AS avg_rating,
    COUNT(*) AS review_count,
    LIST(review_text) AS review_texts
FROM reviews
GROUP BY product_id
HAVING review_count > 1;
""").show()
```

**Result**: [11, 12, 13, 14]

**Explanation**: Demonstrates DuckDB's aggregation capabilities by creating a reviews table, calculating product ratings, and using list aggregation to collect review texts, with a filter to show products with multiple reviews.
## Step 9: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array')
print(rel.execute().fetchall())
```

**Result**: [11, 12, 13, 14]

**Explanation**: This code creates an in-memory DuckDB connection, uses the relational API to generate an array transformation where each element is incremented by 10, and then prints the result using fetchall() to return all rows.
## Step 10: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a time series table with hourly temperature readings
conn.sql("""
CREATE TABLE temperature_readings (
    timestamp TIMESTAMP,
    temperature DECIMAL(5,2)
);

INSERT INTO temperature_readings VALUES
('2023-06-01 00:00:00', 22.5),
('2023-06-01 01:00:00', 21.8),
('2023-06-01 02:00:00', 20.9),
('2023-06-01 03:00:00', 20.1);

-- Calculate rolling 2-hour average temperature
SELECT 
    timestamp, 
    temperature,
    AVG(temperature) OVER (ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_2hr_avg
FROM temperature_readings;
""")

```

**Result**: [11, 12, 13, 14]

**Explanation**: Demonstrates window function for calculating rolling average over time series data, showing DuckDB's ability to perform time-based aggregations with ROWS BETWEEN clause
## Step 11: This targeted implementation showcases DuckDB's array_transform capability by incrementing list elements, highlighting its flexible functional SQL querying approach.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
result = conn.sql('SELECT array_transform([1, 2, 3, 4], x -> x + 10) as incremented_array').fetchone()[0]
print(result)
```

**Result**: [11, 12, 13, 14]

**Explanation**: Demonstrates DuckDB's array_transform function to increment each element of a list by 10, showcasing its inline lambda-like transformation capabilities within SQL.
