# Generated: 2025-03-19 21:24:20.759549
# Result: [('"Alice"', '["Python","SQL"]', 2), ('"Bob"', '["Java","C++"]', 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Demonstrate JSON extraction and manipulation
conn.execute('CREATE TABLE json_data (data JSON)')
conn.execute("""INSERT INTO json_data VALUES
    ('{"name":"Alice", "age":30, "skills":["Python","SQL"]}'),
    ('{"name":"Bob", "age":35, "skills":["Java","C++"]}')""")

result = conn.execute("""
    SELECT 
        json_extract(data, '$.name') as name,
        json_extract(data, '$.skills') as skills,
        json_array_length(json_extract(data, '$.skills')) as skill_count
    FROM json_data
""").fetchall()

print(result)