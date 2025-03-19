# Generated: 2025-03-19 14:26:50.566038
# Result: [([0.0, 0.49999999999999994, 0.7071067811865476, 0.8660254037844386, 1.0],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform array elements using trigonometric functions
result = conn.execute('''
    SELECT array_transform([0, 30, 45, 60, 90], x -> SIN(RADIANS(x))) AS sin_array
''').fetchall()

print(result[0][0])  # Output: [0.0, 0.5, 0.7071067811865475, 0.8660254037844386, 1.0]