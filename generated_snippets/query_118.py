# Generated: 2025-03-19 17:58:11.130182
# Result: [([2, 3, 4, 5],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create array and use array_transform to increment each element
result = conn.execute('''
    SELECT array_transform([1, 2, 3, 4], x -> x + 1) AS incremented_array
''').fetchall()

print(result[0][0])  # Outputs: [2, 3, 4, 5]