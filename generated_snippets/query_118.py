# Generated: 2025-03-19 09:30:24.385687
# Result: [('Electronics', 750, 1), ('Electronics', 500, 2), ('Books', 600, 1), ('Books', 200, 2), ('Clothing', 450, 1), ('Clothing', 300, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sales dataset
conn.sql("""
CREATE TABLE sales AS
SELECT * FROM (
    VALUES
    ('Electronics', 500),
    ('Electronics', 750),
    ('Clothing', 300),
    ('Clothing', 450),
    ('Books', 200),
    ('Books', 600)
) t(category, amount)
""")

# Rank sales within each category by amount
result = conn.sql("""
SELECT
    category,
    amount,
    RANK() OVER (PARTITION BY category ORDER BY amount DESC) as sales_rank
FROM sales
""").fetchall()

print(result)