# Generated: 2025-03-19 14:58:48.137410
# Result: <duckdb.duckdb.DuckDBPyConnection object at 0x00000147DE947E30>
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data
conn.execute('''CREATE TABLE cities (
    city_id INTEGER,
    city_name VARCHAR,
    country VARCHAR,
    population INTEGER,
    latitude FLOAT,
    longitude FLOAT
)''')

# Insert sample data
conn.execute('''INSERT INTO cities VALUES
    (1, 'New York', 'USA', 8400000, 40.7128, -74.0060),
    (2, 'London', 'UK', 9000000, 51.5074, -0.1278),
    (3, 'Tokyo', 'Japan', 14000000, 35.6762, 139.6503),
    (4, 'Sydney', 'Australia', 5300000, -33.8688, 151.2093)''')

# Query to find cities in Northern/Southern Hemispheres
result = conn.execute('''SELECT 
    city_name, 
    country, 
    population,
    CASE 
        WHEN latitude > 0 THEN 'Northern Hemisphere'
        ELSE 'Southern Hemisphere'
    END as hemisphere
FROM cities
ORDER BY population DESC''')

print(result.fetchall())