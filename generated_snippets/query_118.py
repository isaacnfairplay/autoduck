# Generated: 2025-03-19 18:17:03.921803
# Result: ({'name': 'Alice', 'skills': ['Python', 'SQL']}, 'Alice', 'Python')
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create nested data and extract substructures
result = conn.execute("""
    SELECT 
        {'name': 'Alice', 'skills': ['Python', 'SQL']} as person,
        person['name'] as extracted_name,
        person['skills'][1] as second_skill
""").fetchone()

print(f"Full Person: {result[0]}")
print(f"Name: {result[1]}")
print(f"Second Skill: {result[2]}")