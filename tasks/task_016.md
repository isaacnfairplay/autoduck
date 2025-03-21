# Task: Here's a concise DuckDB window function example using the relational API:

```python
import duckdb

con = duckdb.connect()

# Create sales data
con.execute('''
CREATE TABLE sales AS 
SELECT * FROM (VALUES 
    ('Electronics', 'Laptop', 1200),
    ('Electronics', 'Phone', 800),
    ('Electronics', 'Tablet', 500)
) AS t(category, product, amount)
''')

# Calculate running total per category
rel = con.query('''
SELECT 
    category, 
    product, 
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY amount) as running_total
FROM sales
''')

print(rel.execute().fetchall())
```

This example demonstrates window functions by computing running total within product categories using the DuckDB relational API.

## Step 1: Here's a concise DuckDB window function example using the relational API:

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('CREATE TABLE sales (product TEXT, month INT, revenue DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Widget', 1, 1000.50), ('Gadget', 1, 1500.75),
    ('Widget', 2, 1200.25), ('Gadget', 2, 1750.60)
])

# Calculate cumulative revenue per product using window function
result = conn.execute('''
    SELECT 
        product, 
        month, 
        revenue,
        SUM(revenue) OVER (PARTITION BY product ORDER BY month) as cumulative_revenue
    FROM sales
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Month: {row[1]}, Revenue: {row[2]}, Cumulative: {row[3]})")
```

**Result**: [('Widget', 1, Decimal('1000.50'), Decimal('1000.50')), ('Widget', 2, Decimal('1200.25'), Decimal('2200.75')), ('Gadget', 1, Decimal('1500.75'), Decimal('1500.75')), ('Gadget', 2, Decimal('1750.60'), Decimal('3251.35'))]

**Explanation**: Demonstrates a window function calculating cumulative revenue per product across months using partitioning and ordered summation
## Step 2: ```python

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate product inventory table
conn.execute('CREATE TABLE inventory (product TEXT, quantity INT, warehouse TEXT)')
conn.executemany('INSERT INTO inventory VALUES (?, ?, ?)', [
    ('Laptop', 50, 'East'), ('Phone', 75, 'West'), 
    ('Tablet', 30, 'East'), ('Desktop', 40, 'West')
])

# Use window function to rank products by quantity per warehouse
result = conn.execute('''
    SELECT 
        product, 
        warehouse, 
        quantity,
        RANK() OVER (PARTITION BY warehouse ORDER BY quantity DESC) as rank
    FROM inventory
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Warehouse: {row[1]}, Quantity: {row[2]}, Rank: {row[3]}")
```

**Result**: [('Phone', 'West', 75, 1), ('Desktop', 'West', 40, 2), ('Laptop', 'East', 50, 1), ('Tablet', 'East', 30, 2)]

**Explanation**: Demonstrates DuckDB window function (RANK) to rank products by quantity within each warehouse, showing complex analytical querying capabilities
## Step 3: import duckdb

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table with geographic sales data
conn.execute('CREATE TABLE sales (region TEXT, product TEXT, revenue DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('North', 'Laptop', 5000.50), 
    ('South', 'Tablet', 3200.75),
    ('North', 'Desktop', 4500.25),
    ('South', 'Laptop', 4800.60)
])

# Perform multi-dimensional aggregation with GROUPING SETS
result = conn.execute('''
    SELECT 
        region, 
        product, 
        SUM(revenue) as total_revenue,
        GROUPING(region) as region_grouping,
        GROUPING(product) as product_grouping
    FROM sales
    GROUP BY GROUPING SETS ((region, product), (region), (product), ())
''').fetchall()

for row in result:
    print(f"Region: {row[0]}, Product: {row[1]}, Revenue: {row[2]}, Region Grouping: {row[3]}, Product Grouping: {row[4]}")
```

**Result**: [('South', 'Laptop', Decimal('4800.60'), 0, 0), ('North', None, Decimal('9500.75'), 0, 1), ('South', None, Decimal('8001.35'), 0, 1), ('North', 'Laptop', Decimal('5000.50'), 0, 0), ('North', 'Desktop', Decimal('4500.25'), 0, 0), ('South', 'Tablet', Decimal('3200.75'), 0, 0), (None, 'Laptop', Decimal('9801.10'), 1, 0), (None, 'Desktop', Decimal('4500.25'), 1, 0), (None, None, Decimal('17502.10'), 1, 1), (None, 'Tablet', Decimal('3200.75'), 1, 0)]

**Explanation**: Demonstrates DuckDB's advanced GROUPING SETS for multi-dimensional aggregation, allowing complex summarization of sales data across different grouping levels
## Step 4: con = duckdb.connect()

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate time series data
conn.execute('CREATE TABLE stock_prices (symbol TEXT, date DATE, price DECIMAL(10,2))')
conn.executemany('INSERT INTO stock_prices VALUES (?, ?, ?)', [
    ('AAPL', '2023-01-01', 150.25),
    ('AAPL', '2023-01-02', 152.40),
    ('AAPL', '2023-01-03', 149.75),
    ('GOOGL', '2023-01-01', 90.50),
    ('GOOGL', '2023-01-02', 92.10),
    ('GOOGL', '2023-01-03', 91.80)
])

# Calculate moving average using window function
result = conn.execute('''
    SELECT 
        symbol, 
        date, 
        price,
        AVG(price) OVER (PARTITION BY symbol ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg
    FROM stock_prices
''').fetchall()

for row in result:
    print(f"Symbol: {row[0]}, Date: {row[1]}, Price: {row[2]}, Moving Avg: {row[3]:.2f}")
```

**Result**: [('GOOGL', datetime.date(2023, 1, 1), Decimal('90.50'), 90.5), ('GOOGL', datetime.date(2023, 1, 2), Decimal('92.10'), 91.3), ('GOOGL', datetime.date(2023, 1, 3), Decimal('91.80'), 91.46666666666667), ('AAPL', datetime.date(2023, 1, 1), Decimal('150.25'), 150.25), ('AAPL', datetime.date(2023, 1, 2), Decimal('152.40'), 151.325), ('AAPL', datetime.date(2023, 1, 3), Decimal('149.75'), 150.8)]

**Explanation**: Demonstrates time series analysis using DuckDB's window function to calculate a 3-day moving average for stock prices, partitioned by stock symbol
## Step 5: # Create sales data

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales representative performance table
conn.execute('CREATE TABLE sales_reps (rep_name TEXT, region TEXT, sales_amount DECIMAL(10,2), quarter INT)')
conn.executemany('INSERT INTO sales_reps VALUES (?, ?, ?, ?)', [
    ('Alice', 'West', 45000.50, 1),
    ('Bob', 'East', 38000.25, 1),
    ('Charlie', 'West', 52000.75, 1),
    ('Alice', 'West', 48000.60, 2),
    ('Bob', 'East', 41000.30, 2),
    ('Charlie', 'West', 55000.90, 2)
])

# Calculate sales representative performance ranking within region
result = conn.execute('''
    SELECT 
        rep_name, 
        region, 
        quarter, 
        sales_amount,
        DENSE_RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as performance_rank
    FROM sales_reps
''').fetchall()

for row in result:
    print(f"Rep: {row[0]}, Region: {row[1]}, Quarter: {row[2]}, Sales: ${row[3]}, Rank: {row[4]}")
```

**Result**: [('Charlie', 'West', 2, Decimal('55000.90'), 1), ('Charlie', 'West', 1, Decimal('52000.75'), 2), ('Alice', 'West', 2, Decimal('48000.60'), 3), ('Alice', 'West', 1, Decimal('45000.50'), 4), ('Bob', 'East', 2, Decimal('41000.30'), 1), ('Bob', 'East', 1, Decimal('38000.25'), 2)]

**Explanation**: Demonstrates a window function to rank sales representatives by performance within their region across quarters, showcasing DuckDB's ability to perform advanced analytical queries on categorical data
## Step 6: con.execute('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for tournament rankings
conn.execute('CREATE TABLE tournament_results (player TEXT, game TEXT, score INT, round INT)')
conn.executemany('INSERT INTO tournament_results VALUES (?, ?, ?, ?)', [
    ('Alice', 'Chess', 95, 1),
    ('Bob', 'Chess', 88, 1),
    ('Alice', 'Chess', 92, 2),
    ('Bob', 'Chess', 90, 2),
    ('Charlie', 'Chess', 85, 1),
    ('Charlie', 'Chess', 87, 2)
])

# Calculate player's performance improvement using LAG window function
result = conn.execute('''
    SELECT 
        player, 
        game, 
        round, 
        score,
        LAG(score) OVER (PARTITION BY player ORDER BY round) as previous_score,
        score - LAG(score) OVER (PARTITION BY player ORDER BY round) as score_improvement
    FROM tournament_results
''').fetchall()

for row in result:
    print(f"Player: {row[0]}, Game: {row[1]}, Round: {row[2]}, Score: {row[3]}, Previous Score: {row[4]}, Improvement: {row[5]})")
```

**Result**: [('Bob', 'Chess', 1, 88, None, None), ('Bob', 'Chess', 2, 90, 88, 2), ('Alice', 'Chess', 1, 95, None, None), ('Alice', 'Chess', 2, 92, 95, -3), ('Charlie', 'Chess', 1, 85, None, None), ('Charlie', 'Chess', 2, 87, 85, 2)]

**Explanation**: Demonstrates DuckDB's window function LAG() to calculate score improvement across tournament rounds for each player
## Step 7: CREATE TABLE sales AS

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with comprehensive columns
conn.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    sale_date DATE,
    customer_id INTEGER,
    region VARCHAR
);
'''
)

# Optional: Insert sample data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 2, 1200.50, 2401.00, '2023-06-15', 101, 'North'),
    (2, 'Tablet', 'Electronics', 1, 350.75, 350.75, '2023-06-16', 102, 'South')
])
```

**Result**: [('Bob', 'Chess', 1, 88, None, None), ('Bob', 'Chess', 2, 90, 88, 2), ('Alice', 'Chess', 1, 95, None, None), ('Alice', 'Chess', 2, 92, 95, -3), ('Charlie', 'Chess', 1, 85, None, None), ('Charlie', 'Chess', 2, 87, 85, 2)]

**Explanation**: Creates a comprehensive sales table with multiple columns representing typical sales transaction data, including primary key, product details, pricing, date, customer, and regional information
## Step 8: SELECT * FROM (VALUES

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table using VALUES clause
result = conn.execute("""
SELECT * FROM (VALUES
    ('Apple', 5, 1.50),
    ('Banana', 3, 0.75),
    ('Orange', 7, 1.25)
) AS fruits(name, quantity, price)
""").fetchall()

for row in result:
    print(f"Fruit: {row[0]}, Quantity: {row[1]}, Price: ${row[2]}")
```

**Result**: [('Apple', 5, Decimal('1.50')), ('Banana', 3, Decimal('0.75')), ('Orange', 7, Decimal('1.25'))]

**Explanation**: Demonstrates DuckDB's powerful VALUES clause for inline table creation, allowing direct data specification without separate INSERT statements. Shows how to name columns and create a temporary table-like structure within a SELECT query.
## Step 9: ('Electronics', 'Laptop', 1200),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('CREATE TABLE electronics_sales (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert specific sales data
conn.execute("INSERT INTO electronics_sales VALUES ('Electronics', 'Laptop', 1200)")

# Query and demonstrate result processing
result = conn.execute('SELECT * FROM electronics_sales WHERE category = ?', ['Electronics']).fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Price: ${row[2]}")
```

**Result**: [('Electronics', 'Laptop', Decimal('1200.00'))]

**Explanation**: Creates an in-memory DuckDB table for electronics sales, inserts a specific Laptop record, and queries/prints the result using parameterized SQL and fetchall() method
## Step 10: ('Electronics', 'Phone', 800),

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('CREATE TABLE electronics_sales (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert specific sales data
conn.execute("INSERT INTO electronics_sales VALUES ('Electronics', 'Laptop', 1200), ('Electronics', 'Phone', 800)")

# Query and demonstrate result processing
result = conn.execute('SELECT * FROM electronics_sales WHERE category = ?', ['Electronics']).fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Price: ${row[2]}")
```

**Result**: [('Electronics', 'Laptop', Decimal('1200.00')), ('Electronics', 'Phone', Decimal('800.00'))]

**Explanation**: This code creates an in-memory DuckDB table for electronics sales, inserts two products (Laptop and Phone), and then queries and prints all electronics category items.
## Step 11: ('Electronics', 'Tablet', 500)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create electronics sales table
conn.execute('CREATE TABLE electronics_sales (category TEXT, product TEXT, price DECIMAL(10,2))')

# Insert electronics sales including Tablet
conn.execute("INSERT INTO electronics_sales VALUES ('Electronics', 'Laptop', 1200), ('Electronics', 'Phone', 800), ('Electronics', 'Tablet', 500)")

# Query and demonstrate result processing
result = conn.execute('SELECT * FROM electronics_sales WHERE category = ?', ['Electronics']).fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Price: ${row[2]}")
```

**Result**: [('Electronics', 'Laptop', Decimal('1200.00')), ('Electronics', 'Phone', Decimal('800.00')), ('Electronics', 'Tablet', Decimal('500.00'))]

**Explanation**: Extends the previous electronics sales example by adding a Tablet product and demonstrating multiple record insertion and flexible querying in DuckDB
## Step 12: ) AS t(category, product, amount)

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table and insert multiple rows using VALUES clause
result = conn.execute("""
SELECT * FROM (VALUES
    ('Electronics', 'Laptop', 1200.50),
    ('Electronics', 'Phone', 800.25),
    ('Electronics', 'Tablet', 500.75)
) AS t(category, product, amount)
""").fetchall()

for row in result:
    print(f"Category: {row[0]}, Product: {row[1]}, Amount: ${row[2]:.2f}")
```

**Result**: [('Electronics', 'Laptop', Decimal('1200.50')), ('Electronics', 'Phone', Decimal('800.25')), ('Electronics', 'Tablet', Decimal('500.75'))]

**Explanation**: Demonstrates creating an inline table using DuckDB's VALUES clause, showing a flexible way to generate temporary data for querying without creating a permanent table. Useful for quick data exploration or testing scenarios.
## Step 13: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate employee performance table
conn.execute('CREATE TABLE employee_performance (employee TEXT, department TEXT, performance_score DECIMAL(5,2), bonus DECIMAL(10,2))')
conn.executemany('INSERT INTO employee_performance VALUES (?, ?, ?, ?)', [
    ('Alice', 'Sales', 92.5, 5000.00),
    ('Bob', 'Marketing', 88.3, 4200.50),
    ('Charlie', 'Sales', 95.7, 5500.25),
    ('David', 'Marketing', 90.1, 4500.75)
])

# Calculate department performance ranking using PERCENT_RANK
result = conn.execute('''
    SELECT 
        employee, 
        department, 
        performance_score,
        PERCENT_RANK() OVER (PARTITION BY department ORDER BY performance_score DESC) as performance_percentile
    FROM employee_performance
''').fetchall()

for row in result:
    print(f"Employee: {row[0]}, Department: {row[1]}, Score: {row[2]}, Percentile: {row[3]:.2%}")
```

**Result**: [('Charlie', 'Sales', Decimal('95.70'), 0.0), ('Alice', 'Sales', Decimal('92.50'), 1.0), ('David', 'Marketing', Decimal('90.10'), 0.0), ('Bob', 'Marketing', Decimal('88.30'), 1.0)]

**Explanation**: Demonstrates a DuckDB window function (PERCENT_RANK) to calculate relative performance percentiles within each department, showing how employees rank compared to their peers using a percentile approach.
## Step 14: # Calculate running total per category

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table
conn.execute('CREATE TABLE category_sales (category TEXT, sale_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25),
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate running total per category using window function
result = conn.execute('''
    SELECT 
        category, 
        sale_amount, 
        SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as running_total
    FROM category_sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Sale Amount: ${row[1]}, Running Total: ${row[2]:.2f}")
```

**Result**: [('Electronics', Decimal('500.25'), Decimal('500.25')), ('Electronics', Decimal('1000.50'), Decimal('1500.75')), ('Clothing', Decimal('600.30'), Decimal('600.30')), ('Clothing', Decimal('750.75'), Decimal('1351.05'))]

**Explanation**: Demonstrates calculating a running total for sales within each product category using a window function with PARTITION BY and ORDER BY clauses in DuckDB.
## Step 15: rel = con.query('''

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for multi-warehouse inventory tracking
conn.execute('CREATE TABLE warehouse_inventory (product TEXT, warehouse TEXT, quantity INT, price DECIMAL(10,2))')
conn.executemany('INSERT INTO warehouse_inventory VALUES (?, ?, ?, ?)', [
    ('Laptop', 'East', 50, 1200.50),
    ('Phone', 'West', 75, 800.25),
    ('Tablet', 'East', 30, 500.75),
    ('Desktop', 'West', 40, 1000.00)
])

# Demonstrate complex window function with multiple window specifications
result = conn.execute('''
    SELECT 
        product, 
        warehouse, 
        quantity,
        RANK() OVER (PARTITION BY warehouse ORDER BY quantity DESC) as quantity_rank,
        DENSE_RANK() OVER (ORDER BY price DESC) as price_dense_rank
    FROM warehouse_inventory
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Warehouse: {row[1]}, Quantity: {row[2]}, Quantity Rank: {row[3]}, Price Dense Rank: {row[4]}")
```

**Result**: [('Laptop', 'East', 50, 1, 1), ('Desktop', 'West', 40, 2, 2), ('Phone', 'West', 75, 1, 3), ('Tablet', 'East', 30, 2, 4)]

**Explanation**: This example demonstrates advanced window function usage in DuckDB by creating an inventory tracking table and applying multiple window specifications simultaneously, showing rank calculations across different dimensions.
## Step 16: SELECT

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table with product sales data
conn.execute('CREATE TABLE products (id INT, name TEXT, price DECIMAL(10,2), category TEXT)')
conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?)', [
    (1, 'Laptop', 1200.50, 'Electronics'),
    (2, 'Phone', 800.25, 'Electronics'),
    (3, 'Book', 25.99, 'Literature')
])

# Perform SELECT with multiple conditions and ordering
result = conn.execute('''
    SELECT name, price, category 
    FROM products 
    WHERE category = 'Electronics' AND price > 700 
    ORDER BY price DESC
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Price: ${row[1]}, Category: {row[2]}')
```

**Result**: [('Laptop', Decimal('1200.50'), 'Electronics'), ('Phone', Decimal('800.25'), 'Electronics')]

**Explanation**: Demonstrates a SELECT query using DuckDB with multiple filtering conditions (category and price) and result ordering, showcasing basic querying capabilities with in-memory database.
## Step 17: category,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate category sales table
conn.execute('CREATE TABLE category_sales (category TEXT, sale_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25),
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate total sales and percentage contribution per category
result = conn.execute('''
    SELECT 
        category, 
        SUM(sale_amount) as total_sales,
        SUM(sale_amount) / (SELECT SUM(sale_amount) FROM category_sales) * 100 as sales_percentage
    FROM category_sales
    GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Sales: ${row[1]:.2f}, Sales Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', Decimal('1500.75'), 52.62465811066694), ('Clothing', Decimal('1351.05'), 47.37534188933305)]

**Explanation**: Demonstrates calculating total sales and percentage contribution for each product category using a subquery and aggregation functions.
## Step 18: product,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create product table with sales tracking
conn.execute('CREATE TABLE products (id INT PRIMARY KEY, name TEXT, category TEXT, price DECIMAL(10,2), stock INT)')

# Insert sample product data
conn.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 1200.50, 50),
    (2, 'Phone', 'Electronics', 800.25, 75),
    (3, 'Tablet', 'Electronics', 500.75, 30)
])

# Analyze products with window function to rank by price within category
result = conn.execute('''
    SELECT 
        name, 
        category, 
        price,
        RANK() OVER (PARTITION BY category ORDER BY price DESC) as price_rank
    FROM products
''').fetchall()

for row in result:
    print(f'Product: {row[0]}, Category: {row[1]}, Price: ${row[2]}, Price Rank: {row[3]}')
```

**Result**: [('Laptop', 'Electronics', Decimal('1200.50'), 1), ('Phone', 'Electronics', Decimal('800.25'), 2), ('Tablet', 'Electronics', Decimal('500.75'), 3)]

**Explanation**: Demonstrates DuckDB's window function capabilities by creating a product table and ranking products by price within their category, highlighting the API's ability to perform complex analytical queries in-memory.
## Step 19: amount,

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for calculating sales percentages
conn.execute('CREATE TABLE sales (product TEXT, category TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO sales VALUES (?, ?, ?)', [
    ('Laptop', 'Electronics', 1200.50),
    ('Phone', 'Electronics', 800.25),
    ('Book', 'Literature', 50.75)
])

# Calculate total sales and percentage contribution per category
result = conn.execute('''
    SELECT 
        category, 
        SUM(amount) as total_sales,
        SUM(amount) / (SELECT SUM(amount) FROM sales) * 100 as sales_percentage
    FROM sales
    GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Sales: ${row[1]:.2f}, Sales Percentage: {row[2]:.2f}%")
```

**Result**: [('Electronics', Decimal('2000.75'), 97.52620034121374), ('Literature', Decimal('50.75'), 2.4737996587862536)]

**Explanation**: Demonstrates calculating sales percentages across different product categories using DuckDB's window and aggregation functions, showing how to compute relative contributions to total sales.
## Step 20: SUM(amount) OVER (PARTITION BY category ORDER BY amount) as running_total

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales table
conn.execute('CREATE TABLE category_sales (category TEXT, amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25), 
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate running total per category using window function
result = conn.execute('''
    SELECT 
        category, 
        amount, 
        SUM(amount) OVER (PARTITION BY category ORDER BY amount) as running_total
    FROM category_sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Amount: ${row[1]}, Running Total: ${row[2]:.2f}")
```

**Result**: [('Electronics', Decimal('500.25'), Decimal('500.25')), ('Electronics', Decimal('1000.50'), Decimal('1500.75')), ('Clothing', Decimal('600.30'), Decimal('600.30')), ('Clothing', Decimal('750.75'), Decimal('1351.05'))]

**Explanation**: Demonstrates a cumulative total calculation within each category using a window function, showing progressive sum of amounts while preserving category partitioning
## Step 21: FROM sales

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with comprehensive columns
conn.execute('''
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product_name VARCHAR,
    category VARCHAR,
    quantity INTEGER,
    unit_price DECIMAL(10,2),
    total_price DECIMAL(10,2),
    sale_date DATE,
    customer_id INTEGER,
    region VARCHAR
);
''')

# Insert sample sales data
conn.executemany('INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [
    (1, 'Laptop', 'Electronics', 2, 1200.50, 2401.00, '2023-06-15', 101, 'North'),
    (2, 'Tablet', 'Electronics', 1, 350.75, 350.75, '2023-06-16', 102, 'South')
])

# Query to demonstrate flexible table exploration
result = conn.execute('''
SELECT 
    category, 
    SUM(total_price) as total_revenue, 
    AVG(unit_price) as avg_unit_price,
    COUNT(*) as num_sales
FROM sales
GROUP BY category
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Total Revenue: ${row[1]:.2f}, Avg Unit Price: ${row[2]:.2f}, Sales Count: {row[3]}")
```

**Result**: [('Electronics', Decimal('2751.75'), 775.625, 2)]

**Explanation**: This example creates a comprehensive sales table with multiple columns, inserts sample data, and demonstrates a flexible analytical query using aggregation functions to extract insights about sales by category.
## Step 22: ''')

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create table for tracking product orders
conn.execute('CREATE TABLE product_orders (product TEXT, order_date DATE, quantity INT, price DECIMAL(10,2))')

# Insert sample order data
conn.executemany('INSERT INTO product_orders VALUES (?, ?, ?, ?)', [
    ('Laptop', '2023-07-01', 5, 1200.50),
    ('Phone', '2023-07-02', 3, 800.25),
    ('Tablet', '2023-07-03', 2, 500.75)
])

# Calculate cumulative quantity and total value using window functions
result = conn.execute('''  
    SELECT 
        product, 
        order_date, 
        quantity,
        SUM(quantity) OVER (ORDER BY order_date) as cumulative_quantity,
        SUM(quantity * price) OVER (ORDER BY order_date) as cumulative_value
    FROM product_orders
''').fetchall()

for row in result:
    print(f"Product: {row[0]}, Date: {row[1]}, Quantity: {row[2]}, Cumulative Qty: {row[3]}, Cumulative Value: ${row[4]:.2f}")
```

**Result**: [('Laptop', datetime.date(2023, 7, 1), 5, 5, Decimal('6002.50')), ('Phone', datetime.date(2023, 7, 2), 3, 8, Decimal('8403.25')), ('Tablet', datetime.date(2023, 7, 3), 2, 10, Decimal('9404.75'))]

**Explanation**: Demonstrates window functions in DuckDB by tracking cumulative product orders and calculating running totals of quantity and order value over time
## Step 23: print(rel.execute().fetchall())

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create example data
conn.execute('CREATE TABLE numbers (value INT)')
conn.executemany('INSERT INTO numbers VALUES (?)', [(x,) for x in range(1, 6)])

# Execute and print results
result = conn.execute('SELECT value * 2 as doubled FROM numbers').fetchall()
print(result)
```

**Result**: [(2,), (4,), (6,), (8,), (10,)]

**Explanation**: Demonstrates a simple DuckDB query that multiplies each number by 2, showcasing basic table creation, data insertion, and result retrieval
## Step 24: ```

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of stock prices
conn.execute('CREATE TABLE stock_prices (symbol TEXT, price DECIMAL(10,2), date DATE)')

# Insert sample stock data
conn.executemany('INSERT INTO stock_prices VALUES (?, ?, ?)', [
    ('AAPL', 150.25, '2023-07-01'),
    ('GOOGL', 100.50, '2023-07-01'),
    ('MSFT', 280.75, '2023-07-01')
])

# Calculate average price for each stock symbol
result = conn.execute('SELECT symbol, AVG(price) as avg_price FROM stock_prices GROUP BY symbol').fetchall()

for symbol, avg_price in result:
    print(f'{symbol}: ${avg_price:.2f}')
```

**Result**: [('GOOGL', 100.5), ('MSFT', 280.75), ('AAPL', 150.25)]

**Explanation**: Demonstrates DuckDB's basic data insertion, aggregation, and querying capabilities by creating an in-memory stock price table and calculating average prices per symbol.
## Step 25: This example demonstrates window functions by computing running total within product categories using the DuckDB relational API.

**Generated by**: Anthropic

```python
import duckdb

conn = duckdb.connect(':memory:')

# Create category sales table
conn.execute('CREATE TABLE category_sales (category TEXT, sale_amount DECIMAL(10,2))')
conn.executemany('INSERT INTO category_sales VALUES (?, ?)', [
    ('Electronics', 1000.50),
    ('Electronics', 500.25),
    ('Clothing', 750.75),
    ('Clothing', 600.30)
])

# Calculate running total per category using window function
result = conn.execute('''
    SELECT 
        category, 
        sale_amount, 
        SUM(sale_amount) OVER (PARTITION BY category ORDER BY sale_amount) as running_total
    FROM category_sales
''').fetchall()

for row in result:
    print(f"Category: {row[0]}, Sale Amount: ${row[1]}, Running Total: ${row[2]:.2f}")
```

**Result**: [('Electronics', Decimal('500.25'), Decimal('500.25')), ('Electronics', Decimal('1000.50'), Decimal('1500.75')), ('Clothing', Decimal('600.30'), Decimal('600.30')), ('Clothing', Decimal('750.75'), Decimal('1351.05'))]

**Explanation**: Demonstrates a window function that calculates a running total of sales within each product category, showing cumulative sales amounts ordered by individual sale amounts.
