import duckdb
conn = duckdb.connect(':memory:')
result = conn.execute("SELECT 42").fetchall()