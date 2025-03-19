# Generated: 2025-03-19 10:40:57.923623
# Result: (datetime.date(2023, 1, 1),)
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
result = conn.execute("SELECT DATE '2023-01-01'").fetchone()
print(result[0])