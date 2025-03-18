# Generated: 2025-03-17 20:08:09.994251
# Result: [(4, 'David', 'Engineering', 1, 4.0), (2, 'Bob', 'Marketing', 1, 2.0), (1, 'Alice', 'Sales', 1, 2.0), (3, 'Charlie', 'Sales', 2, 2.0)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables for customers and orders
con.execute('''
    CREATE TABLE customers (
        customer_id INT PRIMARY KEY,
        name VARCHAR,
        city VARCHAR
    );

    CREATE TABLE orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        product_name VARCHAR,
        order_date DATE,
        total_amount DECIMAL(10,2),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );

    INSERT INTO customers VALUES
        (1, 'Alice', 'New York'),
        (2, 'Bob', 'Chicago'),
        (3, 'Charlie', 'San Francisco');

    INSERT INTO orders VALUES
        (101, 1, 'Laptop', '2023-01-15', 1200.50),
        (102, 1, 'Smartphone', '2023-02-20', 800.25),
        (103, 2, 'Tablet', '2023-03-10', 500.75),
        (104, 3, 'Monitor', '2023-04-05', 350.00);
''')