# Generated: 2025-03-19 08:17:54.685803
# Result: [(2, 'Bob', '45', 'Chicago')]
# Valid: True
import duckdb

# Create in-memory database
conn = duckdb.connect(':memory:')

# Create JSON processing table
conn.execute('''
CREATE TABLE customer_data (
    id INTEGER,
    details JSON
);

INSERT INTO customer_data VALUES
    (1, '{ "name": "Alice", "age": 30, "city": "New York" }'),
    (2, '{ "name": "Bob", "age": 45, "city": "Chicago" }');
''')  

# Extract and query JSON data
result = conn.execute('''
SELECT 
    id, 
    details->>'name' as name,
    details->>'age' as age,
    details->>'city' as city
FROM customer_data
WHERE (details->>'age')::INTEGER > 35
''').fetchall()

for row in result:
    print(row)