# Generated: 2025-03-19 18:15:22.913346
# Result: [('Brazil', 'South America', 212559417), ('China', 'Asia', 1439323776), ('USA', 'North America', 331000000)]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create and populate table with geographic data
conn.execute('''
    CREATE TABLE countries (
        name VARCHAR,
        continent VARCHAR,
        population INTEGER
    );

    INSERT INTO countries VALUES
        ('USA', 'North America', 331000000),
        ('China', 'Asia', 1439323776),
        ('Brazil', 'South America', 212559417),
        ('India', 'Asia', 1380004385);
''')

# Use QUALIFY window function to select top country by population per continent
result = conn.execute('''
    SELECT name, continent, population
    FROM (
        SELECT 
            name, 
            continent, 
            population,
            RANK() OVER (PARTITION BY continent ORDER BY population DESC) as pop_rank
        FROM countries
    ) ranked_countries
    WHERE pop_rank = 1
''').fetchall()

for row in result:
    print(row)