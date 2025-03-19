# Generated: 2025-03-19 18:19:38.445980
# Result: [2, 4, 6, 8]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a temporary table and apply a window function
conn.execute("""
CREATE TABLE sales (
    product TEXT,
    region TEXT,
    amount DECIMAL
);

INSERT INTO sales VALUES
    ('Widget', 'North', 1000),
    ('Gadget', 'North', 1500),
    ('Widget', 'South', 800),
    ('Gadget', 'South', 1200);

SELECT 
    product, 
    region, 
    amount,
    RANK() OVER (PARTITION BY region ORDER BY amount DESC) as sales_rank
FROM sales;
""")

# Fetch and print results
results = conn.fetchall()
for row in results:
    print(row)