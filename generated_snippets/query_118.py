# Generated: 2025-03-19 17:59:02.226164
# Result: [(1, 'Alice', 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with JSON data and extract nested values
conn.execute("CREATE TABLE users (id INTEGER, details JSON)")
conn.execute("INSERT INTO users VALUES (1, '{\"name\": \"Alice\", \"skills\": [\"Python\", \"SQL\"]}')")

result = conn.execute("""
    SELECT 
        id, 
        details->>'name' AS name,
        json_array_length(details->'skills') AS skill_count
    FROM users
""").fetchall()

print(result)  # Demonstrates JSON extraction and array length computation