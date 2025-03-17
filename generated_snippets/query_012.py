# Generated: 2025-03-16 22:09:27.387087
# Result: [('Laptop', Decimal('999.99')), ('Phone', Decimal('599.50'))]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE people (id INT, name VARCHAR)')
con.execute("INSERT INTO people VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")

rel = con.query('SELECT * FROM people')
name_proj = rel.project('name')
print('Projected Names:', [row[0] for row in name_proj.execute().fetchall()])