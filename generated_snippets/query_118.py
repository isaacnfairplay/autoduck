# Generated: 2025-03-19 18:07:28.037667
# Result: [('Electronics', [[1, 2, 3], [6, 7]]), ('Clothing', [[4, 5]])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table and demonstrate array aggregation
conn.execute('CREATE TABLE products (category STRING, tags INTEGER[])')
conn.execute("INSERT INTO products VALUES ('Electronics', [1, 2, 3]), ('Clothing', [4, 5]), ('Electronics', [6, 7])")

result = conn.execute("SELECT category, array_agg(tags) AS all_tags FROM products GROUP BY category").fetchall()

print(result)