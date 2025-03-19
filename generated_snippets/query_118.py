# Generated: 2025-03-19 18:37:30.834872
# Result: [11, 12, 13, 14, 15]
# Valid: True
# Variable array_data: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create array to transform
array_data = [1, 2, 3, 4, 5]

# Use DuckDB array transformation
result = conn.execute('SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) as transformed_array').fetchone()[0]

print(result)  # Should output: [11, 12, 13, 14, 15]