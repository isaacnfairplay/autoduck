# Task: For a focused DuckDB example, I recommend exploring the QUALIFY clause with a window function to filter top products by sales. Here's a concise demonstration:

```python
import duckdb

con = duckdb.connect()

# Create product sales data
con.execute('''
CREATE TABLE product_sales AS
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Tablet', 500),
    ('Clothing', 'Shirt', 50),
    ('Clothing', 'Pants', 100)
) AS t(category, product, amount)
''')

# Use QUALIFY to filter top 2 products per category
rel = con.query('''
SELECT *
FROM product_sales
QUALIFY ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) <= 2
''')

print(rel.execute().fetchall())
```

This example showcases DuckDB's QUALIFY clause for filtering results using a window function ranking.

## Step 1: For a focused DuckDB example, I recommend exploring the QUALIFY clause with a window function to filter top products by sales. Here's a concise demonstration:

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample product sales data
conn.execute('''
CREATE TABLE product_sales AS
SELECT 'Laptop' as product, 5000 as sales
UNION ALL
SELECT 'Phone', 7500
UNION ALL
SELECT 'Tablet', 3200
UNION ALL
SELECT 'Smartwatch', 2800
''')

# Use QUALIFY to get top 2 products by sales with window function
result = conn.execute('''
SELECT product, sales,
       RANK() OVER (ORDER BY sales DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)
```

**Result**: [('Phone', 7500, 1), ('Laptop', 5000, 2)]

**Explanation**: Demonstrates QUALIFY clause filtering top products using window function ranking, showing DuckDB's advanced analytical query capabilities
## Step 2: ```python

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample employee data with departments
conn.execute('''
CREATE TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL(10,2)
);

INSERT INTO employees VALUES
(1, 'Alice', 'Sales', 55000),
(2, 'Bob', 'Marketing', 60000),
(3, 'Charlie', 'Sales', 52000),
(4, 'David', 'Engineering', 75000),
(5, 'Eve', 'Marketing', 58000);
''')

# Use window function to calculate department salary rankings
result = conn.execute('''
SELECT 
    name, 
    department, 
    salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_salary_rank
FROM employees
''').fetchall()

print(result)
```

**Result**: [('Alice', 'Sales', Decimal('55000.00'), 1), ('Charlie', 'Sales', Decimal('52000.00'), 2), ('David', 'Engineering', Decimal('75000.00'), 1), ('Bob', 'Marketing', Decimal('60000.00'), 1), ('Eve', 'Marketing', Decimal('58000.00'), 2)]

**Explanation**: Demonstrates window function with DENSE_RANK() partitioned by department, showing relative salary rankings within each department
## Step 3: import duckdb

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create time series sales data
conn.execute('''
CREATE TABLE daily_sales AS
SELECT '2023-01-01' as sales_date, 1200.50 as revenue
UNION ALL SELECT '2023-01-02', 1350.75
UNION ALL SELECT '2023-01-03', 1100.25
''')

# Calculate 3-day moving average of revenue
result = conn.execute('''
SELECT 
    sales_date, 
    revenue,
    AVG(revenue) OVER (ORDER BY sales_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
FROM daily_sales
''').fetchall()

print(result)
```

**Result**: [('2023-01-01', Decimal('1200.50'), 1200.5), ('2023-01-02', Decimal('1350.75'), 1275.625), ('2023-01-03', Decimal('1100.25'), 1217.1666666666667)]

**Explanation**: Demonstrates DuckDB's window function for calculating a 3-day moving average of sales revenue, showing time series analysis capabilities with sliding window computation.
## Step 4: con = duckdb.connect()

Failed after 3 attempts: Parser Error: syntax error at or near "#"
## Step 5: # Create product sales data

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_inventory (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    stock_quantity INT,
    unit_price DECIMAL(10,2)
);

INSERT INTO product_inventory VALUES
(1, 'Wireless Headphones', 'Electronics', 150, 79.99),
(2, 'Smart Speaker', 'Electronics', 200, 129.50),
(3, 'Running Shoes', 'Sports', 100, 89.99),
(4, 'Yoga Mat', 'Sports', 75, 39.99),
(5, 'Bluetooth Earbuds', 'Electronics', 180, 59.99);
''')

# Calculate total inventory value by category
result = conn.execute('''
SELECT 
    category, 
    SUM(stock_quantity * unit_price) as total_inventory_value,
    AVG(unit_price) as average_price
FROM product_inventory
GROUP BY category
ORDER BY total_inventory_value DESC
''').fetchall()

print(result)
```

**Result**: [('Electronics', Decimal('48696.70'), 89.82666666666667), ('Sports', Decimal('11998.25'), 64.99)]

**Explanation**: This example demonstrates creating a product inventory table with detailed product information, then using SQL aggregation to calculate total inventory value and average price per category, showcasing DuckDB's ability to perform complex analytical queries efficiently.
## Step 6: con.execute('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a self-referencing recursive CTE to generate numeric sequences
result = conn.execute('''
WITH RECURSIVE number_sequence(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM number_sequence WHERE n < 10
)
SELECT * FROM number_sequence
''').fetchall()

print(result)
```

**Result**: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]

**Explanation**: Demonstrates a recursive Common Table Expression (CTE) for generating a numeric sequence from 1 to 10, showcasing DuckDB's ability to handle recursive queries with a self-referencing table expression.
## Step 7: CREATE TABLE product_sales AS

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with hierarchical sales data
conn.execute('''
CREATE TABLE product_sales (
    product_id INT,
    product_name VARCHAR,
    category VARCHAR,
    sales_amount DECIMAL(10,2),
    sales_year INT
);

INSERT INTO product_sales VALUES
(1, 'Laptop', 'Electronics', 150000.50, 2022),
(2, 'Smartphone', 'Electronics', 220000.75, 2022),
(3, 'Tablet', 'Electronics', 80000.25, 2022),
(4, 'Wireless Headphones', 'Electronics', 45000.00, 2022),
(5, 'Laptop', 'Electronics', 175000.00, 2023),
(6, 'Smartphone', 'Electronics', 250000.50, 2023),
(7, 'Tablet', 'Electronics', 95000.75, 2023);
'''
)
```

**Result**: [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)]

**Explanation**: Creates a product sales table with comprehensive sales data across multiple years, enabling complex analytical queries and comparisons.
## Step 8: SELECT * FROM (VALUES

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Use VALUES to create inline table with multiple data types
result = conn.execute("""
SELECT * FROM (VALUES
    (1, 'Alice', 25.5),
    (2, 'Bob', 30.2),
    (3, 'Charlie', 35.7)
) AS people(id, name, score)
""").fetchall()

print(result)
```

**Result**: [(1, 'Alice', Decimal('25.5')), (2, 'Bob', Decimal('30.2')), (3, 'Charlie', Decimal('35.7'))]

**Explanation**: Demonstrates DuckDB's VALUES clause to create an inline table with multiple columns and data types, useful for quick data generation or testing without creating a permanent table.
## Step 9: ('Electronics', 'Laptop', 1200),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900);
''')

# Calculate total sales by category
result = conn.execute('''
SELECT category, 
       SUM(sales_amount) as total_category_sales
FROM product_sales
GROUP BY category
''').fetchall()

print(result)
```

**Result**: [('Electronics', Decimal('3600.00'))]

**Explanation**: Demonstrates DuckDB's capability to create an in-memory table, insert data, and perform a grouped aggregation to calculate total sales by category.
## Step 10: ('Electronics', 'Phone', 800),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Electronics', 'Phone', 800);
''')

# Demonstrate grouped aggregation with multiple conditions
result = conn.execute('''
SELECT 
    category, 
    product_name, 
    SUM(sales_amount) as total_product_sales
FROM product_sales
GROUP BY category, product_name
HAVING total_product_sales > 1000
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Phone', Decimal('2300.00')), ('Electronics', 'Laptop', Decimal('1200.00'))]

**Explanation**: This example demonstrates DuckDB's ability to perform grouped aggregation with multiple conditions, showing how to calculate total sales per product within a category and filter results based on total sales amount.
## Step 11: ('Electronics', 'Tablet', 500),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create recursive CTE to simulate factorial calculation
result = conn.execute('''
WITH RECURSIVE factorial(n, fact) AS (
    SELECT 1, 1
    UNION ALL
    SELECT n + 1, (n + 1) * fact FROM factorial WHERE n < 5
)
SELECT * FROM factorial
''').fetchall()

print(result)
```

**Result**: [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]

**Explanation**: This code demonstrates a recursive CTE (Common Table Expression) in DuckDB to calculate factorials for numbers 1 through 5, showing how recursive queries can simulate iterative computations using SQL.
## Step 12: ('Clothing', 'Shirt', 50),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with clothing category
conn.execute('''
CREATE TABLE clothing_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_quantity INT
);

INSERT INTO clothing_sales VALUES
('Clothing', 'Shirt', 50),
('Clothing', 'Pants', 30),
('Clothing', 'Shirt', 25);
'''
)

# Group and aggregate sales by clothing type
result = conn.execute('''
SELECT 
    product_name, 
    SUM(sales_quantity) as total_sales
FROM clothing_sales
WHERE category = 'Clothing'
GROUP BY product_name
''').fetchall()

print(result)
```

**Result**: [('Shirt', 75), ('Pants', 30)]

**Explanation**: Demonstrates creating an in-memory DuckDB table with clothing sales data and using SQL to aggregate sales quantities for each clothing product type, filtering specifically for the 'Clothing' category.
## Step 13: ('Clothing', 'Pants', 100)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create clothing sales table with complex data
conn.execute('''
CREATE TABLE clothing_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_quantity INT,
    sales_region VARCHAR
);

INSERT INTO clothing_sales VALUES
('Clothing', 'Shirt', 50, 'North'),
('Clothing', 'Pants', 30, 'North'),
('Clothing', 'Shirt', 25, 'South'),
('Clothing', 'Pants', 70, 'South');
''')

# Compute total sales quantity by clothing type and region
result = conn.execute('''
SELECT 
    product_name, 
    sales_region,
    SUM(sales_quantity) as total_sales
FROM clothing_sales
WHERE category = 'Clothing'
GROUP BY product_name, sales_region
ORDER BY total_sales DESC
''').fetchall()

print(result)
```

**Result**: [('Pants', 'South', 70), ('Shirt', 'North', 50), ('Pants', 'North', 30), ('Shirt', 'South', 25)]

**Explanation**: This example demonstrates advanced DuckDB SQL with complex grouping across multiple dimensions (product and region), filtering by category, and sorting aggregated results.
## Step 14: ) AS t(category, product, amount)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create inline table with categorical aggregation
result = conn.execute('''
WITH sales_data(category, product, amount) AS (
    VALUES
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 1500),
    ('Clothing', 'Shirt', 800),
    ('Clothing', 'Pants', 950)
)
SELECT 
    category, 
    SUM(amount) as total_category_sales,
    COUNT(DISTINCT product) as unique_products
FROM sales_data
GROUP BY category
ORDER BY total_category_sales DESC
''').fetchall()

print(result)
```

**Result**: [('Electronics', 2700, 2), ('Clothing', 1750, 2)]

**Explanation**: Demonstrates an inline table (VALUES clause) with multi-column categorical aggregation, showing total sales and unique product count per category using a Common Table Expression (CTE)
## Step 15: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product price history table
conn.execute('''
CREATE TABLE product_prices (
    product_name VARCHAR,
    price DECIMAL(10,2),
    price_date DATE
);

INSERT INTO product_prices VALUES
('Laptop', 999.99, '2023-01-01'),
('Laptop', 1099.99, '2023-02-01'),
('Laptop', 949.99, '2023-03-01');
''')

# Calculate price changes with window functions
result = conn.execute('''
SELECT 
    product_name, 
    price, 
    price_date,
    price - LAG(price) OVER (PARTITION BY product_name ORDER BY price_date) as price_change
FROM product_prices
''').fetchall()

print(result)
```

**Result**: [('Laptop', Decimal('999.99'), datetime.date(2023, 1, 1), None), ('Laptop', Decimal('1099.99'), datetime.date(2023, 2, 1), Decimal('100.00')), ('Laptop', Decimal('949.99'), datetime.date(2023, 3, 1), Decimal('-150.00'))]

**Explanation**: Demonstrates DuckDB's window function capabilities by tracking price changes for a product over time using LAG() to compare consecutive price entries
## Step 16: # Use QUALIFY to filter top 2 products per category

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

# Use QUALIFY to get top 2 products per category by sales
result = conn.execute('''
SELECT category, product_name, sales_amount,
       RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Phone', Decimal('1500.00'), 1), ('Electronics', 'Laptop', Decimal('1200.00'), 2), ('Clothing', 'Pants', Decimal('950.00'), 1), ('Clothing', 'Shirt', Decimal('800.00'), 2)]

**Explanation**: Demonstrates using QUALIFY with window functions to filter top 2 products within each sales category based on sales amount.
## Step 17: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking employee performance
conn.execute('''
CREATE TABLE employee_performance (
    employee_id INT,
    department VARCHAR,
    performance_score DECIMAL(5,2),
    bonus_eligible BOOLEAN
);

INSERT INTO employee_performance VALUES
(1, 'Sales', 87.5, TRUE),
(2, 'Marketing', 92.3, TRUE),
(3, 'Engineering', 95.1, TRUE),
(4, 'Sales', 78.6, FALSE),
(5, 'Marketing', 85.2, TRUE);
''')

# Calculate performance metrics using window functions
result = conn.execute('''
SELECT 
    department,
    AVG(performance_score) OVER (PARTITION BY department) as dept_avg_score,
    RANK() OVER (ORDER BY performance_score DESC) as performance_rank,
    bonus_eligible
FROM employee_performance
''').fetchall()

print(result)
```

**Result**: [('Engineering', 95.1, 1, True), ('Marketing', 88.75, 2, True), ('Sales', 83.05, 3, True), ('Marketing', 88.75, 4, True), ('Sales', 83.05, 5, False)]

**Explanation**: Demonstrates using window functions to calculate departmental performance averages and individual performance rankings, with conditional bonus eligibility tracking
## Step 18: SELECT *

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample table
conn.execute('''
CREATE TABLE customers (
    id INT,
    name VARCHAR,
    age INT
);

INSERT INTO customers VALUES
(1, 'Alice', 28),
(2, 'Bob', 35),
(3, 'Charlie', 42);
''')

# Simple SELECT * query
result = conn.execute('SELECT * FROM customers').fetchall()
print(result)
```

**Result**: [(1, 'Alice', 28), (2, 'Bob', 35), (3, 'Charlie', 42)]

**Explanation**: Demonstrates basic DuckDB SELECT * operation by creating an in-memory table and retrieving all rows and columns using a wildcard query.
## Step 19: FROM product_sales

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

# Calculate total sales by category and product
result = conn.execute('''
SELECT 
    category, 
    product_name,
    SUM(sales_amount) as total_product_sales
FROM product_sales
GROUP BY category, product_name
ORDER BY total_product_sales DESC
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Phone', Decimal('1500.00')), ('Electronics', 'Laptop', Decimal('1200.00')), ('Clothing', 'Pants', Decimal('950.00')), ('Electronics', 'Tablet', Decimal('900.00')), ('Clothing', 'Shirt', Decimal('800.00'))]

**Explanation**: Demonstrates creating a product sales table, using GROUP BY with multiple columns to calculate total sales per product within each category, and sorting results in descending order of total sales.
## Step 20: QUALIFY ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) <= 2

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE sales (
    category VARCHAR,
    product VARCHAR,
    amount DECIMAL(10,2)
);

INSERT INTO sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

result = conn.execute('''
SELECT category, product, amount,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) as rank
FROM sales
QUALIFY rank <= 2
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Phone', Decimal('1500.00'), 1), ('Electronics', 'Laptop', Decimal('1200.00'), 2), ('Clothing', 'Pants', Decimal('950.00'), 1), ('Clothing', 'Shirt', Decimal('800.00'), 2)]

**Explanation**: Demonstrates using QUALIFY with ROW_NUMBER() to select top 2 products per category by sales amount, partitioning the window function by category and ordering by sales in descending order.
## Step 21: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product inventory and sales
conn.execute('''
CREATE TABLE product_tracking (
    product_id INT,
    product_name VARCHAR,
    inventory_quantity INT,
    sales_quantity INT,
    price DECIMAL(10,2)
);

INSERT INTO product_tracking VALUES
(1, 'Laptop', 100, 25, 999.99),
(2, 'Phone', 150, 40, 599.99),
(3, 'Tablet', 75, 15, 349.99);
'''
)

# Calculate inventory turnover ratio using window functions
result = conn.execute('''
SELECT 
    product_name,
    inventory_quantity,
    sales_quantity,
    sales_quantity * 1.0 / inventory_quantity as turnover_ratio,
    RANK() OVER (ORDER BY sales_quantity * 1.0 / inventory_quantity DESC) as turnover_rank
FROM product_tracking
''').fetchall()

print(result)
```

**Result**: [('Phone', 150, 40, 0.26666666666666666, 1), ('Laptop', 100, 25, 0.25, 2), ('Tablet', 75, 15, 0.2, 3)]

**Explanation**: Demonstrates DuckDB's window functions by calculating inventory turnover ratio, ranking products based on their sales-to-inventory performance, showcasing analytical querying capabilities
## Step 22: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('CREATE TABLE numbers (id INT, value INT)')
conn.execute('INSERT INTO numbers VALUES (1, 10), (2, 20), (3, 30)')

rel = conn.table('numbers').filter('value > 15')
print(rel.execute().fetchall())
```

**Result**: [('Phone', 150, 40, 0.26666666666666666, 1), ('Laptop', 100, 25, 0.25, 2), ('Tablet', 75, 15, 0.2, 3)]

**Explanation**: Demonstrates DuckDB relational API by creating an in-memory table, filtering rows using the table() and filter() methods, and executing the query to fetch results greater than 15.
## Step 23: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product sales table with multi-category hierarchical data
conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    subcategory VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Computers', 'Laptop', 1200),
('Electronics', 'Computers', 'Desktop', 900),
('Electronics', 'Mobile', 'Smartphone', 1500),
('Clothing', 'Outerwear', 'Jacket', 800),
('Clothing', 'Tops', 'Shirt', 600);
'''
)

# Demonstrate multi-level aggregation and window ranking
result = conn.execute('''
SELECT 
    category, 
    subcategory, 
    SUM(sales_amount) as total_subcategory_sales,
    RANK() OVER (PARTITION BY category ORDER BY SUM(sales_amount) DESC) as subcategory_rank
FROM product_sales
GROUP BY category, subcategory
QUALIFY subcategory_rank <= 2
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Computers', Decimal('2100.00'), 1), ('Clothing', 'Tops', Decimal('600.00'), 2), ('Clothing', 'Outerwear', Decimal('800.00'), 1), ('Electronics', 'Mobile', Decimal('1500.00'), 2)]

**Explanation**: Demonstrates multi-level aggregation using category, subcategory with window function to rank subcategories within each category, showcasing DuckDB's hierarchical data analysis capabilities
## Step 24: This example showcases DuckDB's QUALIFY clause for filtering results using a window function ranking.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

conn.execute('''
CREATE TABLE product_sales (
    category VARCHAR,
    product_name VARCHAR,
    sales_amount DECIMAL(10,2)
);

INSERT INTO product_sales VALUES
('Electronics', 'Laptop', 1200),
('Electronics', 'Phone', 1500),
('Electronics', 'Tablet', 900),
('Clothing', 'Shirt', 800),
('Clothing', 'Pants', 950);
''')

result = conn.execute('''
SELECT category, product_name, sales_amount,
       RANK() OVER (PARTITION BY category ORDER BY sales_amount DESC) as sales_rank
FROM product_sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)
```

**Result**: [('Electronics', 'Phone', Decimal('1500.00'), 1), ('Electronics', 'Laptop', Decimal('1200.00'), 2), ('Clothing', 'Pants', Decimal('950.00'), 1), ('Clothing', 'Shirt', Decimal('800.00'), 2)]

**Explanation**: Demonstrates using QUALIFY clause to select top 2 selling products within each category using window function ranking.
