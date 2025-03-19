# Generated: 2025-03-19 13:52:04.190829
# Result: [([4.0, 6.0, 7.0, 8.0, 10.0],)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create table with numeric lists
conn.execute('CREATE TABLE number_arrays (values_list INTEGER[])')
conn.execute('INSERT INTO number_arrays VALUES ([10, 20, 30, 40, 50])')

# Apply complex mathematical transformation (exponential & floor)
result = conn.execute('SELECT array_transform(values_list, x -> floor(sqrt(x * 2))) as transformed_values FROM number_arrays').fetchall()

print(result)