# Generated: 2025-03-19 15:15:10.142838
# Result: [(1, ['python', 'data', 'analytics'], 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with complex nested data and query using list/array functions
conn.execute("CREATE TABLE complex_data (id INT, tags VARCHAR[])")
conn.execute("INSERT INTO complex_data VALUES (1, ['python', 'data', 'analytics']), (2, ['sql', 'database'])")

# Find rows where tags contains specific elements using array_contains
result = conn.execute("""
    SELECT id, tags, array_length(tags) as tag_count
    FROM complex_data
    WHERE array_contains(tags, 'python')
""").fetchall()

print(result)  # Shows rows matching 'python' tag