# Generated: 2025-03-19 16:09:35.196484
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Pivot table to transform rows into columns
conn.execute("""
CREATE TABLE sales (
    product VARCHAR,
    region VARCHAR,
    amount DECIMAL
);

INSERT INTO sales VALUES
    ('Laptop', 'North', 1000),
    ('Laptop', 'South', 1500),
    ('Phone', 'North', 800),
    ('Phone', 'South', 1200);

SELECT * FROM sales
PIVOT (SUM(amount) FOR region IN ('North', 'South'))
""").fetchall()