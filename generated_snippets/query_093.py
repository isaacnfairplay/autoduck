# Generated: 2025-03-16 23:54:14.763037
# Result: [(1, 'Alice', 30), (3, 'Charlie', 35)]
# Valid: True
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create a sample table
con.execute('''
    CREATE TABLE users (
        id INT,
        name VARCHAR,
        age INT
    );
    INSERT INTO users VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35);
''')

# Query the table
result = con.execute('SELECT * FROM users WHERE age > 25').fetchall()
for row in result:
    print(row)