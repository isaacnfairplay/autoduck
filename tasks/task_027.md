# Task: I've prepared a concise DuckDB example demonstrating a specialized technique - here's a targeted implementation showing a custom window function to calculate percentage of total within categories:

```python
import duckdb

con = duckdb.connect()

# Create sales data
con.execute('''
CREATE TABLE sales AS 
SELECT * FROM (VALUES 
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 100)
) AS t(category, product, amount)
''')

# Calculate percentage of total sales per category
rel = con.query('''
SELECT 
    category, 
    product, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as percentage_of_category_total
FROM sales
''')

print(rel.execute().fetchall())
```

This example demonstrates a window function calculating each product's sales percentage within its category, showcasing DuckDB's flexible analytical capabilities.

## Step 1: I've prepared a concise DuckDB example demonstrating a specialized technique - here's a targeted implementation showing a custom window function to calculate percentage of total within categories:

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute("""
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
""")

# Calculate percentage of total sales within each category
result = conn.execute("""
SELECT 
    category, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as category_percentage
FROM sales
""").fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}, Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', 1500, 39.473684210526315), ('Electronics', 2300, 60.526315789473685), ('Clothing', 1000, 36.36363636363637), ('Clothing', 1750, 63.63636363636363)]

**Explanation**: Demonstrates a window function to calculate percentage of total within sales categories, showing dynamic percentage computation across grouped data
## Step 2: ```python

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create shipping and orders tables
conn.execute('''
CREATE TABLE shipping (
    order_id INTEGER,
    carrier VARCHAR,
    shipping_cost DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INTEGER,
    total_amount DECIMAL(10,2)
);

INSERT INTO shipping VALUES
(1, 'FedEx', 15.50),
(2, 'UPS', 22.75),
(3, 'USPS', 8.25);

INSERT INTO orders VALUES
(1, 250.00),
(2, 525.50),
(3, 125.75);
'''
)

# Calculate shipping cost percentage relative to order total
result = conn.execute('''
SELECT 
    o.order_id, 
    s.carrier, 
    s.shipping_cost, 
    o.total_amount,
    (s.shipping_cost / o.total_amount * 100) AS shipping_percentage
FROM orders o
JOIN shipping s ON o.order_id = s.order_id
ORDER BY shipping_percentage DESC
''').fetchall()

for row in result:
    print(f"Order {row[0]} via {row[1]}: ${row[2]} shipping on ${row[3]} order ({row[4]:.2f}% of total)")
```

**Result**: [(3, 'USPS', Decimal('8.25'), Decimal('125.75'), 6.560636182902585), (1, 'FedEx', Decimal('15.50'), Decimal('250.00'), 6.2), (2, 'UPS', Decimal('22.75'), Decimal('525.50'), 4.329210275927688)]

**Explanation**: Demonstrates multi-table join to calculate shipping cost percentage relative to order total, showing how DuckDB can perform percentage calculations across related tables
## Step 3: import duckdb

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of products
conn.execute('''
CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 1200.00),
(2, 'Smartphone', 'Electronics', 800.50),
(3, 'Headphones', 'Electronics', 150.25),
(4, 'Running Shoes', 'Sports', 120.00);
'''
)

# Analytical query using window functions to rank products by price within category
result = conn.execute('''
SELECT
    name,
    category,
    price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
FROM products
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): ${row[2]} - Rank: {row[3]}")
```

**Result**: [('Laptop', 'Electronics', Decimal('1200.00'), 1), ('Smartphone', 'Electronics', Decimal('800.50'), 2), ('Headphones', 'Electronics', Decimal('150.25'), 3), ('Running Shoes', 'Sports', Decimal('120.00'), 1)]

**Explanation**: Demonstrates DuckDB's window function capabilities by ranking products by price within their respective categories, showcasing analytical query potential.
## Step 4: con = duckdb.connect()

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create time series data
conn.execute('''
CREATE TABLE temperature_readings (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
);

INSERT INTO temperature_readings VALUES
('2023-06-01 10:00:00', 1, 22.5),
('2023-06-01 11:00:00', 1, 23.1),
('2023-06-01 12:00:00', 1, 23.8),
('2023-06-01 10:00:00', 2, 21.7);
''')

# Calculate moving average with window function
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM temperature_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]} at {row[1]}: {row[2]}�C (Moving Avg: {row[3]:.2f}�C)")
```

**Result**: [(1, datetime.datetime(2023, 6, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 6, 1, 11, 0), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 6, 1, 12, 0), 23.799999237060547, 23.449999809265137), (2, datetime.datetime(2023, 6, 1, 10, 0), 21.700000762939453, 21.700000762939453)]

**Explanation**: Demonstrates time series analysis using DuckDB's window functions to calculate a moving average temperature per sensor, showcasing time-based windowing and partitioning capabilities
## Step 5: # Create sales data

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create monthly sales data
conn.execute('''
CREATE TABLE monthly_sales (
    month VARCHAR,
    product VARCHAR,
    revenue DECIMAL(10,2)
);

INSERT INTO monthly_sales VALUES
('January', 'Laptop', 45000.00),
('January', 'Smartphone', 30000.50),
('February', 'Laptop', 52000.25),
('February', 'Smartphone', 35000.75);
'''
)

# Calculate total revenue per product
result = conn.execute('''
SELECT 
    product, 
    SUM(revenue) as total_revenue,
    AVG(revenue) as avg_monthly_revenue
FROM monthly_sales
GROUP BY product
ORDER BY total_revenue DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: Total Revenue ${row[1]}, Avg Monthly ${row[2]:.2f}")
```

**Result**: [('Laptop', Decimal('97000.25'), 48500.125), ('Smartphone', Decimal('65001.25'), 32500.625)]

**Explanation**: Creates a monthly sales table with two products, demonstrates SQL aggregation with SUM and AVG to calculate total and average monthly revenues, ordered by total revenue descending
## Step 6: con.execute('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a table tracking student grades
conn.execute('''
CREATE TABLE student_grades (
    student_id INTEGER,
    subject VARCHAR,
    grade DECIMAL(5,2)
);

INSERT INTO student_grades VALUES
(1, 'Math', 85.5),
(1, 'Science', 92.3),
(2, 'Math', 78.2),
(2, 'Science', 88.7);
''')

# Use window functions to calculate grade percentiles
result = conn.execute('''
SELECT 
    student_id, 
    subject, 
    grade,
    PERCENT_RANK() OVER (PARTITION BY subject ORDER BY grade) as percentile
FROM student_grades
''').fetchall()

for row in result:
    print(f"Student {row[0]} in {row[1]}: Grade {row[2]} (Percentile: {row[3]:.2%})")
```

**Result**: [(2, 'Math', Decimal('78.20'), 0.0), (1, 'Math', Decimal('85.50'), 1.0), (2, 'Science', Decimal('88.70'), 0.0), (1, 'Science', Decimal('92.30'), 1.0)]

**Explanation**: Demonstrates window function PERCENT_RANK() to calculate relative standing of student grades within each subject, showing how students compare percentile-wise across different classes.
## Step 7: CREATE TABLE sales AS

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with various attributes
conn.execute('''
CREATE TABLE sales AS
SELECT 'Laptop' as product, 'Electronics' as category, 1500.00 as price, '2023-01-15' as sale_date
UNION ALL
SELECT 'Smartphone', 'Electronics', 850.50, '2023-02-20'
UNION ALL
SELECT 'Running Shoes', 'Sports', 120.00, '2023-03-10'
UNION ALL
SELECT 'Headphones', 'Electronics', 199.99, '2023-01-25'
''')

# Verify table creation
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(row)
```

**Result**: [('Laptop', 'Electronics', Decimal('1500.00'), '2023-01-15'), ('Smartphone', 'Electronics', Decimal('850.50'), '2023-02-20'), ('Running Shoes', 'Sports', Decimal('120.00'), '2023-03-10'), ('Headphones', 'Electronics', Decimal('199.99'), '2023-01-25')]

**Explanation**: Creates an in-memory sales table with multiple columns and sample data using UNION ALL, demonstrating DuckDB's flexible table creation syntax and immediate querying capability.
## Step 8: SELECT * FROM (VALUES

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate direct VALUES usage in query
result = conn.execute("SELECT * FROM (VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')) AS names(id, name)").fetchall()

for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}")
```

**Result**: [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]

**Explanation**: Demonstrates DuckDB's ability to create inline table with VALUES clause, showing direct row construction without pre-existing table. Useful for quick data generation or testing.
## Step 9: ('Electronics', 'Laptop', 1200),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics products table
conn.execute('''
CREATE TABLE electronics_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO electronics_products VALUES
('Electronics', 'Laptop', 1200.00),
('Electronics', 'Smartphone', 800.50),
('Electronics', 'Tablet', 500.75);
''')

# Query to filter and analyze Electronics category
result = conn.execute('''
SELECT 
    category, 
    product, 
    price,
    ROUND(price / (SELECT AVG(price) FROM electronics_products) * 100, 2) as price_percentage
FROM electronics_products
ORDER BY price DESC
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} ({row[3]}% of avg price)")
```

**Result**: [('Electronics', 'Laptop', Decimal('1200.00'), 143.93), ('Electronics', 'Smartphone', Decimal('800.50'), 96.01), ('Electronics', 'Tablet', Decimal('500.75'), 60.06)]

**Explanation**: Demonstrates creating an in-memory table of electronics products, inserting sample data, and performing a relative price analysis using a subquery and percentage calculation
## Step 10: ('Electronics', 'Phone', 800),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics table
conn.execute('''
CREATE TABLE electronics (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO electronics VALUES
('Electronics', 'Phone', 800.00),
('Electronics', 'Laptop', 1200.50),
('Electronics', 'Tablet', 500.75);
''')

# Analyze products in Electronics category
result = conn.execute('''
SELECT 
    product, 
    price, 
    price - AVG(price) OVER () as price_diff
FROM electronics
WHERE category = 'Electronics'
ORDER BY price_diff DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} (Difference from Avg: ${row[2]:.2f})")
```

**Result**: [('Laptop', Decimal('1200.50'), 366.75), ('Phone', Decimal('800.00'), -33.75), ('Tablet', Decimal('500.75'), -333.0)]

**Explanation**: Demonstrates creating an electronics table, inserting data, and using a window function to calculate price differences from the overall category average
## Step 11: ('Clothing', 'Shirt', 50),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing products table
conn.execute('''
CREATE TABLE clothing_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO clothing_products VALUES
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50),
('Clothing', 'Jacket', 120.25);
''');

# Analyze clothing category with price comparison
result = conn.execute('''
SELECT 
    product, 
    price, 
    ROUND(price / (SELECT AVG(price) FROM clothing_products) * 100, 2) as price_percentage
FROM clothing_products
WHERE category = 'Clothing'
ORDER BY price DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} ({row[2]}% of category avg)")
```

**Result**: [('Jacket', Decimal('120.25'), 146.8), ('Jeans', Decimal('75.50'), 92.17), ('Shirt', Decimal('50.00'), 61.04)]

**Explanation**: Demonstrates creating a clothing products table, inserting data, and performing a price percentage analysis relative to category average using DuckDB's SQL capabilities
## Step 12: ('Clothing', 'Pants', 100)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing products table with new entry
conn.execute('''
CREATE TABLE clothing_products (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO clothing_products VALUES
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50),
('Clothing', 'Jacket', 120.25),
('Clothing', 'Pants', 100.00);
''')

# Analyze clothing category with price comparison
result = conn.execute('''
SELECT 
    product, 
    price, 
    ROUND(price / (SELECT AVG(price) FROM clothing_products) * 100, 2) as price_percentage
FROM clothing_products
WHERE category = 'Clothing' AND product = 'Pants'
''').fetchall()

for row in result:
    print(f"{row[0]}: ${row[1]} ({row[2]}% of category avg)")
```

**Result**: [('Pants', Decimal('100.00'), 115.69)]

**Explanation**: Demonstrates adding a new 'Pants' entry to the clothing_products table and calculating its price percentage relative to the category average using DuckDB SQL
## Step 13: ) AS t(category, product, amount)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create temporary product sales table
conn.execute('''
CREATE TABLE product_sales AS
SELECT 'Electronics' as category, 'Laptop' as product, 1500.00 as amount
UNION ALL
SELECT 'Electronics', 'Smartphone', 850.50
UNION ALL
SELECT 'Clothing', 'Jeans', 75.50
UNION ALL
SELECT 'Clothing', 'Shirt', 50.00
''')

# Analyze product sales with total and percentage
result = conn.execute('''
SELECT
    category,
    product,
    amount,
    ROUND(amount / SUM(amount) OVER (PARTITION BY category) * 100, 2) as category_percentage
FROM product_sales
ORDER BY category, amount DESC
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} ({row[3]}% of category sales)")
```

**Result**: [('Clothing', 'Jeans', Decimal('75.50'), 60.16), ('Clothing', 'Shirt', Decimal('50.00'), 39.84), ('Electronics', 'Laptop', Decimal('1500.00'), 63.82), ('Electronics', 'Smartphone', Decimal('850.50'), 36.18)]

**Explanation**: Creates an in-memory product sales table, calculates total sales and percentage for each product within its category, demonstrating window function and percentage calculation in DuckDB
## Step 14: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table with geographic data
conn.execute('''
CREATE TABLE cities (
    city VARCHAR,
    country VARCHAR,
    population INTEGER
);

INSERT INTO cities VALUES
('New York', 'USA', 8400000),
('London', 'UK', 9000000),
('Tokyo', 'Japan', 13900000),
('Paris', 'France', 2140000);
''')

# Rank cities by population within their country
result = conn.execute('''
SELECT
    city,
    country,
    population,
    DENSE_RANK() OVER (PARTITION BY country ORDER BY population DESC) as population_rank
FROM cities
ORDER BY country, population_rank
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): {row[2]} people - Rank: {row[3]}")
```

**Result**: [('Paris', 'France', 2140000, 1), ('Tokyo', 'Japan', 13900000, 1), ('London', 'UK', 9000000, 1), ('New York', 'USA', 8400000, 1)]

**Explanation**: Demonstrates using window function DENSE_RANK() to rank cities within their respective countries by population, showcasing multi-level analytical querying in DuckDB
## Step 15: # Calculate percentage of total sales per category

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data table
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Calculate percentage of total sales within each category
result = conn.execute('''
SELECT 
    category, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as category_percentage
FROM sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}, Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', 1500, 39.473684210526315), ('Electronics', 2300, 60.526315789473685), ('Clothing', 1000, 36.36363636363637), ('Clothing', 1750, 63.63636363636363)]

**Explanation**: Demonstrates calculating sales percentage within each product category using a window function, showing relative contribution of each sale to its category total.
## Step 16: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sensor monitoring data
conn.execute('''
CREATE TABLE sensor_readings (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT,
    humidity FLOAT
);

INSERT INTO sensor_readings VALUES
('2023-07-01 10:00:00', 1, 22.5, 45.3),
('2023-07-01 11:00:00', 1, 23.1, 44.8),
('2023-07-01 10:00:00', 2, 21.7, 46.2);
''')

# Use window function to calculate sensor variance
result = conn.execute('''
SELECT
    sensor_id,
    timestamp,
    temperature,
    ROUND(VARIANCE(temperature) OVER (PARTITION BY sensor_id), 2) as temp_variance
FROM sensor_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]} at {row[1]}: {row[2]}�C (Variance: {row[3]})")
```

**Result**: [(1, datetime.datetime(2023, 7, 1, 10, 0), 22.5, 0.18), (1, datetime.datetime(2023, 7, 1, 11, 0), 23.100000381469727, 0.18), (2, datetime.datetime(2023, 7, 1, 10, 0), 21.700000762939453, None)]

**Explanation**: Demonstrates using DuckDB's window function (VARIANCE) to calculate temperature variance per sensor, showing how analytical functions can be applied to time-series sensor data
## Step 17: SELECT

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample courses table
conn.execute('''
CREATE TABLE courses (
    course_id INTEGER,
    name VARCHAR,
    department VARCHAR,
    credits INTEGER
);

INSERT INTO courses VALUES
(1, 'Calculus', 'Mathematics', 4),
(2, 'Computer Science', 'CS', 3),
(3, 'Physics', 'Science', 4),
(4, 'Statistics', 'Mathematics', 3);
''')

# Select courses by department with advanced filtering
result = conn.execute('''
SELECT 
    course_id, 
    name, 
    credits
FROM courses
WHERE department = 'Mathematics'
ORDER BY credits DESC
''').fetchall()

for row in result:
    print(f"Course {row[0]}: {row[1]} ({row[2]} credits)")
```

**Result**: [(1, 'Calculus', 4), (4, 'Statistics', 3)]

**Explanation**: Demonstrates SELECT with filtering, ordering, and projection, showing how to retrieve specific columns from a table based on a department condition and sort by credits in descending order.
## Step 18: category,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and analyze product categories
conn.execute('''
CREATE TABLE product_categories (
    category VARCHAR,
    product VARCHAR,
    price DECIMAL(10,2)
);

INSERT INTO product_categories VALUES
('Electronics', 'Laptop', 1200.00),
('Electronics', 'Smartphone', 800.50),
('Clothing', 'Shirt', 50.00),
('Clothing', 'Jeans', 75.50);
''')

# Rank products by price within each category
result = conn.execute('''
SELECT
    category,
    product,
    price,
    RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
FROM product_categories
ORDER BY category, price_rank
''').fetchall()

for row in result:
    print(f"{row[1]} ({row[0]}): ${row[2]} - Rank: {row[3]}")
```

**Result**: [('Clothing', 'Jeans', Decimal('75.50'), 1), ('Clothing', 'Shirt', Decimal('50.00'), 2), ('Electronics', 'Laptop', Decimal('1200.00'), 1), ('Electronics', 'Smartphone', Decimal('800.50'), 2)]

**Explanation**: Demonstrates window function RANK() to order products by price within their category, showing relative pricing across different product groups
## Step 19: product,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product inventory table
conn.execute('''
CREATE TABLE products (
    product_id INTEGER,
    name VARCHAR,
    category VARCHAR,
    stock_quantity INTEGER,
    unit_price DECIMAL(10,2)
);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 50, 1200.00),
(2, 'Smartphone', 'Electronics', 100, 800.50),
(3, 'Running Shoes', 'Sports', 75, 120.00);
''')

# Analyze inventory valuation by category
result = conn.execute('''
SELECT
    category,
    SUM(stock_quantity * unit_price) as total_inventory_value,
    AVG(unit_price) as avg_product_price
FROM products
GROUP BY category
ORDER BY total_inventory_value DESC
''').fetchall()

for row in result:
    print(f"{row[0]}: Inventory Value ${row[1]:.2f}, Avg Price ${row[2]:.2f}")
```

**Result**: [('Electronics', Decimal('140050.00'), 1000.25), ('Sports', Decimal('9000.00'), 120.0)]

**Explanation**: Demonstrates creating a product inventory table and performing aggregation analysis across product categories, calculating total inventory value and average product price per category.
## Step 20: amount,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create temperature tracking table with anomaly detection
conn.execute('''CREATE TABLE temperature_log (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
);

INSERT INTO temperature_log VALUES
('2023-07-01 10:00:00', 1, 22.5),
('2023-07-01 11:00:00', 1, 23.1),
('2023-07-01 12:00:00', 1, 45.8);
''')

# Detect temperature anomalies using window function
result = conn.execute('''
SELECT 
    timestamp,
    sensor_id,
    temperature,
    ABS(temperature - AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)) as temp_deviation
FROM temperature_log
''').fetchall()

for row in result:
    print(f"Sensor {row[1]} at {row[0]}: {row[2]}�C (Deviation: {row[3]:.2f}�C)")
```

**Result**: [(datetime.datetime(2023, 7, 1, 10, 0), 1, 22.5, 0.3000001907348633), (datetime.datetime(2023, 7, 1, 11, 0), 1, 23.100000381469727, 7.366666158040363), (datetime.datetime(2023, 7, 1, 12, 0), 1, 45.79999923706055, 11.34999942779541)]

**Explanation**: Demonstrates temperature tracking with sensor anomaly detection using window function to calculate localized temperature deviations
## Step 21: amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as percentage_of_category_total

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Calculate percentage of total sales within each category
result = conn.execute('''
SELECT 
    category, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as category_percentage
FROM sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}, Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', 1500, 39.473684210526315), ('Electronics', 2300, 60.526315789473685), ('Clothing', 1000, 36.36363636363637), ('Clothing', 1750, 63.63636363636363)]

**Explanation**: Demonstrates calculating percentage of total sales for each category using a window function, partitioning by category and computing relative contribution of each sale amount.
## Step 22: FROM sales

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data table
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Fetch and display sales data
result = conn.execute('SELECT * FROM sales').fetchall()
for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}")
```

**Result**: [('Electronics', 1500), ('Electronics', 2300), ('Clothing', 1000), ('Clothing', 1750)]

**Explanation**: Creates an in-memory sales table with categories and amounts, then retrieves and prints all rows to demonstrate basic table creation and data retrieval in DuckDB
## Step 23: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table with inventory data
conn.execute('''
CREATE TABLE inventory (
    product_id INTEGER,
    product_name VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    unit_price DECIMAL(10,2)
);

INSERT INTO inventory VALUES
(1, 'Laptop', 'Electronics', 50, 1200.00),
(2, 'Smartphone', 'Electronics', 100, 800.50),
(3, 'Headphones', 'Electronics', 200, 150.25);
''')

# Analyze inventory with cumulative calculation
result = conn.execute('''
SELECT
    product_name,
    category,
    quantity,
    unit_price,
    SUM(quantity * unit_price) OVER (PARTITION BY category ORDER BY quantity) as cumulative_value
FROM inventory
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): Qty {row[2]}, Price ${row[3]}, Cumulative Value ${row[4]:.2f}")
```

**Result**: [('Laptop', 'Electronics', 50, Decimal('1200.00'), Decimal('60000.00')), ('Smartphone', 'Electronics', 100, Decimal('800.50'), Decimal('140050.00')), ('Headphones', 'Electronics', 200, Decimal('150.25'), Decimal('170100.00'))]

**Explanation**: Demonstrates DuckDB window function with cumulative value calculation across a product category, showing how to progressively aggregate inventory values while maintaining per-category context.
## Step 24: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')
rel = conn.sql('SELECT 1 AS column')
print(rel.execute().fetchall())
```

**Result**: [('Laptop', 'Electronics', 50, Decimal('1200.00'), Decimal('60000.00')), ('Smartphone', 'Electronics', 100, Decimal('800.50'), Decimal('140050.00')), ('Headphones', 'Electronics', 200, Decimal('150.25'), Decimal('170100.00'))]

**Explanation**: Basic DuckDB relational algebra query demonstrating simple column projection and result fetching
## Step 25: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a simple time series of temperature readings
conn.execute('''
CREATE TABLE temperature_readings (
    timestamp TIMESTAMP,
    sensor_id INTEGER,
    temperature FLOAT
);

INSERT INTO temperature_readings VALUES
('2023-07-01 10:00:00', 1, 22.5),
('2023-07-01 11:00:00', 1, 23.1),
('2023-07-01 12:00:00', 1, 23.8);
''')

# Calculate moving average with window function
result = conn.execute('''
SELECT 
    sensor_id, 
    timestamp, 
    temperature,
    AVG(temperature) OVER (PARTITION BY sensor_id ORDER BY timestamp ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg
FROM temperature_readings
''').fetchall()

for row in result:
    print(f"Sensor {row[0]} at {row[1]}: {row[2]}�C (Moving Avg: {row[3]:.2f}�C)")
```

**Result**: [(1, datetime.datetime(2023, 7, 1, 10, 0), 22.5, 22.5), (1, datetime.datetime(2023, 7, 1, 11, 0), 23.100000381469727, 22.800000190734863), (1, datetime.datetime(2023, 7, 1, 12, 0), 23.799999237060547, 23.449999809265137)]

**Explanation**: Demonstrates DuckDB's window function capability by calculating a simple moving average of temperature readings for a specific sensor, showcasing time series analysis
## Step 26: This example demonstrates a window function calculating each product's sales percentage within its category, showcasing DuckDB's flexible analytical capabilities.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales data table
conn.execute('''
CREATE TABLE sales AS
SELECT 'Electronics' as category, 1500 as amount
UNION ALL
SELECT 'Electronics', 2300
UNION ALL
SELECT 'Clothing', 1000
UNION ALL
SELECT 'Clothing', 1750
''')

# Calculate percentage of total sales within each category
result = conn.execute('''
SELECT 
    category, 
    amount,
    amount * 100.0 / SUM(amount) OVER (PARTITION BY category) as category_percentage
FROM sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: {row[1]}, Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', 1500, 39.473684210526315), ('Electronics', 2300, 60.526315789473685), ('Clothing', 1000, 36.36363636363637), ('Clothing', 1750, 63.63636363636363)]

**Explanation**: Demonstrates using a window function to calculate each product's sales percentage within its category, showcasing DuckDB's analytical window function capabilities by partitioning and computing percentage contribution.
