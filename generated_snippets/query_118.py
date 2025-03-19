# Generated: 2025-03-19 14:32:58.027124
# Result: ('"Alice"', '30', '"New York"')
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a nested JSON data structure and extract nested values
conn.execute("CREATE TABLE user_profiles AS SELECT * FROM (VALUES ('{\"name\": \"Alice\", \"details\": {\"age\": 30, \"city\": \"New York\"}}')) AS t(profile)")

result = conn.execute("""
    SELECT 
        json_extract(profile, '$.name') AS name,
        json_extract(profile, '$.details.age') AS age,
        json_extract(profile, '$.details.city') AS city
    FROM user_profiles
""").fetchone()

print(f"Name: {result[0]}, Age: {result[1]}, City: {result[2]}")