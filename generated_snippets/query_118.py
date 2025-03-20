# Generated: 2025-03-19 21:41:00.228527
# Result: [('New York', 8400000, 'Northeast'), ('Los Angeles', 3900000, 'West')]
# Valid: True
# Variable city: Type: tuple
# Attributes/Methods: count, index
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.execute("""
CREATE TABLE cities (
    city_name VARCHAR,
    population INTEGER,
    region VARCHAR,
    latitude DOUBLE,
    longitude DOUBLE
)""")

# Insert sample data about global cities
conn.execute("""
INSERT INTO cities VALUES
    ('New York', 8400000, 'Northeast', 40.7128, -74.0060),
    ('Los Angeles', 3900000, 'West', 34.0522, -118.2437),
    ('Chicago', 2700000, 'Midwest', 41.8781, -87.6298)
""")

# Query to find cities with population over 3 million
result = conn.execute("""
SELECT city_name, population, region
FROM cities
WHERE population > 3000000
ORDER BY population DESC
""").fetchall()

for city in result:
    print(f"{city[0]}: {city[1]} people in {city[2]}")