# Generated: 2025-03-19 16:56:23.845911
# Result: [(3, ['reading', 'music']), (1, ['reading', 'coding'])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with array column
conn.sql("CREATE TABLE users (id INT, interests STRING[])")

# Insert data with array literals
conn.sql("INSERT INTO users VALUES "
         "(1, ['reading', 'coding']), "
         "(2, ['travel', 'photography']), "
         "(3, ['reading', 'music'])")

# Use array_contains to filter rows
result = conn.sql("SELECT * FROM users WHERE 'reading' = ANY(interests)").fetchall()
print(result)