# Generated: 2025-03-19 08:32:17.325788
# Result: [(2, 'Electronics', Decimal('750.50'), Decimal('1250.50'), 1), (1, 'Electronics', Decimal('500.00'), Decimal('500.00'), 2), (4, 'Clothing', Decimal('300.25'), Decimal('551.00'), 1), (3, 'Clothing', Decimal('250.75'), Decimal('250.75'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales table with product categories
conn.execute("""
    CREATE TABLE sales (
        product_id INT,
        category TEXT,
        sale_amount DECIMAL(10,2)
    );

    INSERT INTO sales VALUES
    (1, 'Electronics', 500.00),
    (2, 'Electronics', 750.50),
    (3, 'Clothing', 250.75),
    (4, 'Clothing', 300.25);
""")

# Window function: cumulative sales per category with ranking
result = conn.execute("""
    SELECT 
        product_id, 
        category, 
        sale_amount,
        SUM(sale_amount) OVER (PARTITION BY category ORDER BY product_id) as cumulative_sales,
        RANK() OVER (PARTITION BY category ORDER BY sale_amount DESC) as sales_rank
    FROM sales
""").fetchall()

for row in result:
    print(row)