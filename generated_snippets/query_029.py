# Generated: 2025-03-16 22:18:01.628172
# Result: [(1, 'Alice', 'Sales', 50000)]
# Valid: True
import duckdb

con = duckdb.connect(':memory:')

con.sql('''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    department VARCHAR,
    salary INTEGER
);

INSERT INTO employees VALUES
    (1, 'Alice', 'Sales', 50000);
''')

result = con.sql('SELECT * FROM employees').fetchall()
print(result)