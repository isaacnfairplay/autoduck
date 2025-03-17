# Generated: 2025-03-16 22:09:18.346598
# Result: [('Laptop', Decimal('999.99')), ('Phone', Decimal('599.50'))]
# Valid: True
# Variable product: Type: tuple
# Attributes/Methods: count, index
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE products (id INT, name VARCHAR, price DECIMAL(10,2))')
con.execute("INSERT INTO products VALUES (1, 'Laptop', 999.99), (2, 'Phone', 599.50), (3, 'Tablet', 349.75)")

result = con.execute('SELECT name, price FROM products WHERE price > 500').fetchall()
for product in result:
    print(f'{product[0]}: ${product[1]}')