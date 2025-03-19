# Generated: 2025-03-19 15:44:57.092366
# Result: [4, 9, 16, 25]
# Valid: True
# Variable table: Type: NoneType
import duckdb

conn = duckdb.connect(':memory:')
table = conn.sql('CREATE TABLE products (id INT, name VARCHAR, price DECIMAL)')
rel = conn.table('products').filter('price > 10').project('name, price')
print(rel.execute().fetchall())