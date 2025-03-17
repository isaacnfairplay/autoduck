# Generated: 2025-03-16 22:49:08.885933
# Result: [(2,)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
con = duckdb.connect(':memory:')

# Execute a simple query
result = con.execute('SELECT 1 + 1 AS calculation').fetchall()
print(result)