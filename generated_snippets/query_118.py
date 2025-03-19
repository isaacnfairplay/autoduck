# Generated: 2025-03-19 19:20:22.479016
# Result: [([2, 4, 6, 8, 10],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and transform numeric array using array_transform
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4, 5], x -> x * 2) as doubled_array
''').fetchall()

print(result[0][0])  # Output: [2, 4, 6, 8, 10]