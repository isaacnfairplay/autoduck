# Generated: 2025-03-16 22:49:29.043294
# Result: [(2, datetime.date(2023, 2, 25), 8, Decimal('110.00'), Decimal('1380.00'), 1), (1, datetime.date(2023, 2, 20), 15, Decimal('55.00'), Decimal('1325.00'), 2), (1, datetime.date(2023, 1, 15), 10, Decimal('50.00'), Decimal('500.00'), 3), (2, datetime.date(2023, 1, 10), 5, Decimal('100.00'), Decimal('500.00'), 3)]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')
con.execute('CREATE TABLE employees (id INT, name VARCHAR, department_id INT)')
con.execute("INSERT INTO employees VALUES (1, 'Alice', 101), (2, 'Bob', 102), (3, 'Charlie', 101)")