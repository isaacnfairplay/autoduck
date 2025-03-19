# Generated: 2025-03-19 14:18:11.601487
# Result: [('Alice', ['Python', 'SQL', 'Machine Learning']), ('Charlie', ['Python', 'Data Analysis'])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with employee skills and use array_contains for filtering
conn.execute('CREATE TABLE employees (name TEXT, skills TEXT[])')
conn.execute("""INSERT INTO employees VALUES
    ('Alice', ['Python', 'SQL', 'Machine Learning']),
    ('Bob', ['Java', 'DevOps']),
    ('Charlie', ['Python', 'Data Analysis'])
""")

result = conn.execute('''
    SELECT name, skills
    FROM employees
    WHERE array_contains(skills, 'Python')
''').fetchall()

for row in result:
    print(f"Name: {row[0]}, Skills: {row[1]})")