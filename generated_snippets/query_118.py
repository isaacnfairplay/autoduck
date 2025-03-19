# Generated: 2025-03-19 12:44:14.362837
# Result: [('B', 220, '2023-03-01', 1), ('B', 180, '2023-02-01', 2), ('A', 200, '2023-02-01', 1), ('A', 150, '2023-03-01', 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample sales data
conn.execute('''
CREATE TABLE sales AS
SELECT * FROM (VALUES
    ('A', 100, '2023-01-01'),
    ('A', 200, '2023-02-01'),
    ('A', 150, '2023-03-01'),
    ('B', 120, '2023-01-01'),
    ('B', 180, '2023-02-01'),
    ('B', 220, '2023-03-01')
) AS t(region, amount, date);
'''
)

# Use QUALIFY to filter top 2 sales per region
result = conn.execute('''
SELECT region, amount, date,
       RANK() OVER (PARTITION BY region ORDER BY amount DESC) as sales_rank
FROM sales
QUALIFY sales_rank <= 2
''').fetchall()

print(result)