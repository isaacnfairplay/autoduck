# Generated: 2025-03-19 14:57:54.141758
# Result: [0.0, 0.5, 0.7071, 0.866, 1.0]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Apply sine function to numeric array
result = conn.execute('''
    SELECT array_transform([0, 30, 45, 60, 90], x -> ROUND(SIN(RADIANS(x)), 4)) AS sine_values
''').fetchone()[0]

print(result)  # Outputs: [0.0, 0.5, 0.7071, 0.866, 1.0]