# Generated: 2025-03-19 14:40:33.632184
# Result: [1, 8, 27, 64, 125]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Generate an array of numbers and cube each element using array_transform
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * x * x) AS cubed_values
''').fetchone()[0]

print(result)  # Outputs: [1, 8, 27, 64, 125]