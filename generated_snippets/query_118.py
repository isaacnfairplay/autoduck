# Generated: 2025-03-19 18:28:52.374411
# Result: [('"Alice"', '30')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# JSON parsing and transformation example
query = '''
SELECT
    json_extract(json_str, '$.name') as person_name,
    json_extract_string(json_str, '$.age') as person_age
FROM (
    SELECT '{
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }' as json_str
);
'''

result = conn.execute(query).fetchall()
for row in result:
    print(f'Name: {row[0]}, Age: {row[1]}')