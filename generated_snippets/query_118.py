# Generated: 2025-03-19 18:00:50.981996
# Result: [('B', 200, 200), ('A', 100, 100), ('A', 150, 250), ('C', 300, 300)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate series and compute running totals with window function
conn.execute('CREATE TABLE sales (product STRING, amount INTEGER)')
conn.execute("INSERT INTO sales VALUES ('A', 100), ('B', 200), ('A', 150), ('C', 300)")

result = conn.execute("""
    SELECT 
        product, 
        amount, 
        SUM(amount) OVER (PARTITION BY product ORDER BY amount) as running_total
    FROM sales
""").fetchall()

print(result)