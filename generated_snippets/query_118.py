# Generated: 2025-03-19 14:25:07.778997
# Result: [(1, '"Alice"', '"blue"'), (2, '"Bob"', '"red"')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate JSON extraction and nested querying
conn.execute('CREATE TABLE users (id INTEGER, data JSON)')
conn.execute("""INSERT INTO users VALUES
    (1, '{"name": "Alice", "preferences": {"color": "blue", "size": "large"}}'),
    (2, '{"name": "Bob", "preferences": {"color": "red", "size": "medium"}}')""")

result = conn.execute('''
    SELECT 
        id, 
        json_extract(data, '$.name') as name,
        json_extract(data, '$.preferences.color') as color
    FROM users
''').fetchall()

for row in result:
    print(row)