# Generated: 2025-03-19 17:39:18.336074
# Result: [([1, 4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array and transform via array_transform
result = conn.sql("""
SELECT array_transform([1, 2, 3, 4, 5], x -> x * x) AS squared_values
""").fetchall()

print(result)  # Outputs squared list