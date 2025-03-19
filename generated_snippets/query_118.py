# Generated: 2025-03-19 10:37:29.391883
# Result: [('USA', 2020, 113, 1), ('China', 2020, 88, 2), ('Japan', 2020, 58, 3)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table of Olympic medal counts
conn.execute('''
    CREATE TABLE olympic_medals (
        country TEXT,
        year INTEGER,
        gold INTEGER,
        silver INTEGER,
        bronze INTEGER
    );
''')

# Insert sample data
conn.executemany('INSERT INTO olympic_medals VALUES (?, ?, ?, ?, ?)', [
    ('USA', 2020, 39, 41, 33),
    ('China', 2020, 38, 32, 18),
    ('Japan', 2020, 27, 14, 17)
])

# Compute total medal counts with window function
result = conn.execute('''
    SELECT 
        country, 
        year, 
        gold + silver + bronze AS total_medals,
        RANK() OVER (ORDER BY gold DESC) as gold_rank
    FROM olympic_medals
''').fetchall()

for row in result:
    print(row)