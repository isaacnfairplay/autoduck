# Generated: 2025-03-19 17:11:48.747890
# Result: [(1, datetime.date(2023, 1, 15), 5, 5), (1, datetime.date(2023, 2, 20), 3, 8), (2, datetime.date(2023, 1, 15), 2, 2), (2, datetime.date(2023, 3, 10), 4, 6)]
# Valid: True
import duckdb

# Create an in-memory database with sales data
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
        (1, '2023-01-15', 5, 100.50),
        (1, '2023-02-20', 3, 100.50),
        (2, '2023-01-15', 2, 250.00),
        (2, '2023-03-10', 4, 250.00);
""")

# Window function: Calculate cumulative sales per product
result = conn.sql("""
    SELECT 
        product_id, 
        sale_date, 
        quantity,
        SUM(quantity) OVER (PARTITION BY product_id ORDER BY sale_date) as cumulative_quantity
    FROM sales
    ORDER BY product_id, sale_date
""").fetchall()

for row in result:
    print(row)