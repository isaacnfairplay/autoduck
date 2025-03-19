# Generated: 2025-03-19 13:55:28.731279
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE994530>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')
conn.execute('CREATE TABLE products (id INTEGER, name VARCHAR, price DECIMAL(10,2))')
conn.execute("INSERT INTO products VALUES (1, 'Laptop', 999.99), (2, 'Tablet', 499.50)")
rel = conn.table('products').filter('price > 500').project('name, price')
print(rel.execute().fetchall())