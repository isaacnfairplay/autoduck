# Generated: 2025-03-19 08:08:26.743964
# Result: [('UK', 9000000, 1), ('Japan', 14000000, 1), ('USA', 8400000, 1)]
# Valid: True
import duckdb

# Create in-memory connection
conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.execute('''
CREATE TABLE cities (
    city VARCHAR,
    country VARCHAR,
    population INTEGER
);

INSERT INTO cities VALUES
    ('New York', 'USA', 8400000),
    ('London', 'UK', 9000000),
    ('Tokyo', 'Japan', 14000000);
''')

# Perform aggregation and filtering
result = conn.execute('''
SELECT 
    country, 
    MAX(population) as max_population,
    COUNT(*) as city_count
FROM cities
GROUP BY country
HAVING MAX(population) > 5000000
''').fetchall()

for row in result:
    print(row)