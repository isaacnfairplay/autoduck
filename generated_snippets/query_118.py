# Generated: 2025-03-19 14:56:09.026064
# Result: [('Alice', 28, 'Middle-aged'), ('Diana', 22, 'Young')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and query a people table with complex age-based filtering
conn.execute('''CREATE TABLE people (name VARCHAR, age INTEGER, city VARCHAR)''')
conn.execute('''INSERT INTO people VALUES 
    ('Alice', 28, 'New York'), 
    ('Bob', 35, 'San Francisco'), 
    ('Charlie', 42, 'Chicago'), 
    ('Diana', 22, 'Boston')''')

result = conn.execute('''
    SELECT name, age, 
           CASE 
               WHEN age < 25 THEN 'Young' 
               WHEN age BETWEEN 25 AND 40 THEN 'Middle-aged' 
               ELSE 'Senior' 
           END as age_group
    FROM people
    WHERE city IN ('New York', 'Boston') AND age > 20
    ORDER BY age DESC
''').fetchall()

print(result)