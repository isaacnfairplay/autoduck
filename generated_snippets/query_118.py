# Generated: 2025-03-19 14:49:18.539866
# Result: [(1, 'Alice', [90, 95, 100])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with complex nested data
conn.execute('CREATE TABLE nested_data (id INTEGER, details STRUCT(name VARCHAR, scores INT[]))')
conn.execute("INSERT INTO nested_data VALUES (1, {'name': 'Alice', 'scores': [85, 90, 95]})")

# Extract and transform nested data using SQL
result = conn.execute("""
    SELECT 
        id, 
        details.name, 
        array_transform(details.scores, x -> x + 5) as boosted_scores
    FROM nested_data
""").fetchall()

for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}, Boosted Scores: {row[2]})")