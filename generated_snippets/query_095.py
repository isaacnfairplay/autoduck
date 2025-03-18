# Generated: 2025-03-16 23:55:40.509123
# Result: [(1, 'Alice', 30), (3, 'Charlie', 35)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample relation with id and name
rel = con.sql('SELECT * FROM (VALUES (1, \'Alice\'), (2, \'Bob\'), (3, \'Charlie\')) AS t(id, name)')

# Apply filter to select rows where id > 1
filtered_rel = rel.filter('id > 1')

# Execute and fetch filtered results
results = filtered_rel.execute().fetchall()
print(results)  # Output will be [(2, 'Bob'), (3, 'Charlie')]