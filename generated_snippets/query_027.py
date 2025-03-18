# Generated: 2025-03-16 22:17:30.724422
# Result: [('Alice', 'New York', Decimal('1200.75'), Decimal('1701.25'), 1), ('Bob', 'San Francisco', Decimal('750.25'), Decimal('750.25'), 2), ('Alice', 'New York', Decimal('500.50'), Decimal('1701.25'), 3)]
# Valid: True
import duckdb

# Create in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Create sales and customer relations
con.sql('''
CREATE TABLE sales (
    sale_id INTEGER,
    customer_id INTEGER,
    amount DECIMAL(10,2)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    city VARCHAR
);

INSERT INTO customers VALUES
    (1, 'Alice', 'New York'),
    (2, 'Bob', 'San Francisco');

INSERT INTO sales VALUES
    (101, 1, 500.50),
    (102, 2, 750.25),
    (103, 1, 1200.75);
''')

# Advanced analytical query with joins and window functions
result = con.sql('''
SELECT
    c.name,
    c.city,
    s.amount,
    SUM(s.amount) OVER (PARTITION BY c.city) AS city_total_sales,
    RANK() OVER (ORDER BY s.amount DESC) AS sales_rank
FROM sales s
JOIN customers c ON s.customer_id = c.id
''').fetchall()

for row in result:
    print(row)