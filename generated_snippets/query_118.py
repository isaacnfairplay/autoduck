# Generated: 2025-03-19 15:53:30.570334
# Result: [('Bob', 35, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and query a people table with nested JSON data
conn.sql('''
    CREATE TABLE people AS 
    SELECT * FROM (
        VALUES 
        ('Alice', {'age': 30, 'skills': ['Python', 'SQL']}),
        ('Bob', {'age': 35, 'skills': ['Java', 'C++', 'DuckDB']})
    ) AS t(name, details)
''')

# Extract nested JSON fields and filter
result = conn.sql('''
    SELECT 
        name, 
        details['age'] as age, 
        ARRAY_LENGTH(details['skills']) as skill_count
    FROM people
    WHERE 35 = details['age']
''').fetchall()

print(result)