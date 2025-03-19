# Generated: 2025-03-19 11:36:17.974154
# Result: [('Paris', 'France', 2140000, 1), ('Tokyo', 'Japan', 13900000, 1), ('London', 'UK', 9000000, 1), ('New York', 'USA', 8400000, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with geographic data
conn.execute('''
CREATE TABLE cities (
    city VARCHAR,
    country VARCHAR,
    population INTEGER
);

INSERT INTO cities VALUES
('New York', 'USA', 8400000),
('London', 'UK', 9000000),
('Tokyo', 'Japan', 13900000),
('Paris', 'France', 2140000);
''')

# Rank cities by population within their country
result = conn.execute('''
SELECT
    city,
    country,
    population,
    DENSE_RANK() OVER (PARTITION BY country ORDER BY population DESC) as population_rank
FROM cities
ORDER BY country, population_rank
''').fetchall()

for row in result:
    print(f"{row[0]} ({row[1]}): {row[2]} people - Rank: {row[3]}")