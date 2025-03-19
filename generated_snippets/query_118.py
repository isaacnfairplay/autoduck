# Generated: 2025-03-19 19:12:41.536950
# Result: [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.sql("""
CREATE TABLE cities (
    city_name VARCHAR,
    population INTEGER,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

INSERT INTO cities VALUES
('New York', 8400000, 40.7128, -74.0060),
('Los Angeles', 3900000, 34.0522, -118.2437),
('Chicago', 2700000, 41.8781, -87.6298);

-- Find cities within a bounding box using spatial predicate
SELECT city_name, population
FROM cities
WHERE latitude BETWEEN 30 AND 45
  AND longitude BETWEEN -120 AND -70;
""").show()
