# Generated: 2025-03-19 11:17:51.153500
# Result: [('Phone', 'South', Decimal('3200.75'), Decimal('3200.75')), ('Laptop', 'West', Decimal('4500.60'), Decimal('4500.60')), ('Laptop', 'North', Decimal('5000.50'), Decimal('5000.50')), ('Tablet', 'East', Decimal('2100.25'), Decimal('2100.25'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table and insert sample data
conn.sql('''
CREATE TABLE temperatures (
    city VARCHAR,
    date DATE,
    temp_celsius FLOAT
);

INSERT INTO temperatures VALUES
    ('New York', '2023-07-01', 28.5),
    ('New York', '2023-07-02', 29.1),
    ('Chicago', '2023-07-01', 25.3),
    ('Chicago', '2023-07-02', 26.7);
''')

# Complex windowing with inter-city temperature comparisons
rel = conn.sql('''
SELECT 
    city, 
    date, 
    temp_celsius,
    AVG(temp_celsius) OVER (PARTITION BY city ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as moving_avg,
    temp_celsius - AVG(temp_celsius) OVER (PARTITION BY city) as deviation_from_mean
FROM temperatures
''')

print(rel.execute().fetchall())