# Generated: 2025-03-17 19:58:37.950189
# Result: [('David', 'Engineering', Decimal('75000.000'), 75000.0, Decimal('500000.000'), 1), ('Bob', 'Marketing', Decimal('60000.000'), 60000.0, Decimal('200000.000'), 2), ('Charlie', 'Sales', Decimal('55000.000'), 52500.0, Decimal('250000.000'), 3), ('Alice', 'Sales', Decimal('50000.000'), 52500.0, Decimal('250000.000'), 4)]
# Valid: True
import duckdb

# Create an in-memory DuckDB connection
conn = duckdb.connect(':memory:')

# Create table with sample tuple mapping
conn.execute('CREATE TABLE example_mapping (id INT, name VARCHAR, mapping_value INT)')

# Insert data matching the specific tuple
conn.execute("INSERT INTO example_mapping VALUES (1, 'Alice', 1)")

# Query and display results
results = conn.execute('SELECT * FROM example_mapping').fetchall()
for row in results:
    print(row)

conn.close()