# Generated: 2025-03-19 14:33:48.298473
# Result: [1.0, 2.0, 3.0, 4.0, 5.0]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Apply square root to array elements using array_transform
result = conn.execute('''
    SELECT array_transform([1, 4, 9, 16, 25], x -> SQRT(x)) AS root_values
''').fetchone()[0]

print(result)  # Outputs: [1.0, 2.0, 3.0, 4.0, 5.0]