# Generated: 2025-03-19 17:46:48.384139
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create geographic sales data with geospatial indexing
conn.sql("""
CREATE TABLE sales_regions (
    region_id INTEGER,
    region_name VARCHAR,
    geohash VARCHAR
);

INSERT INTO sales_regions VALUES
(1, 'North', 'abc123'),
(2, 'South', 'def456'),
(3, 'East', 'ghi789');

-- Query regions using geospatial proximity
SELECT region_name
FROM sales_regions
WHERE geohash LIKE 'abc%'
""").show()