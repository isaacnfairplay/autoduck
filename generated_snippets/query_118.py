# Generated: 2025-03-19 09:36:33.254048
# Result: [('Engineering', 'Bob', Decimal('160000.00'), 80000.0), ('Sales', 'Charlie', Decimal('65000.00'), 65000.0), ('Marketing', 'David', Decimal('70000.00'), 70000.0), ('Engineering', 'Alice', Decimal('160000.00'), 80000.0)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

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