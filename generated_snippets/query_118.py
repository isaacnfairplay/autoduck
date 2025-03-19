# Generated: 2025-03-19 16:04:33.706004
# Result: [(2, 'Electronics', Decimal('1500.000'), 1), (4, 'Clothing', Decimal('1200.000'), 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with geographic data and perform spatial query
conn.execute("""
CREATE TABLE cities (
    name VARCHAR,
    latitude DOUBLE,
    longitude DOUBLE
);

INSERT INTO cities VALUES
    ('New York', 40.7128, -74.0060),
    ('Los Angeles', 34.0522, -118.2437),
    ('Chicago', 41.8781, -87.6298);

-- Calculate distances between cities using Haversine formula
SELECT 
    name, 
    ROUND(6371 * 2 * ASIN(
        SQRT(POWER(SIN((latitude - 40.7128) * PI() / 360), 2) + 
             COS(latitude * PI() / 180) * COS(40.7128 * PI() / 180) * 
             POWER(SIN((longitude - (-74.0060)) * PI() / 360), 2)
        )
    ), 2) AS distance_km
FROM cities
""").fetchall()
