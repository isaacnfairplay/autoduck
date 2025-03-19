# Generated: 2025-03-19 14:04:25.094928
# Result: [('London', datetime.date(2023, 6, 1), Decimal('22.10'), 22.75), ('London', datetime.date(2023, 6, 2), Decimal('23.40'), 22.466666666666665), ('London', datetime.date(2023, 6, 3), Decimal('21.90'), 22.65), ('New York', datetime.date(2023, 6, 1), Decimal('28.50'), 29.35), ('New York', datetime.date(2023, 6, 2), Decimal('30.20'), 29.466666666666665), ('New York', datetime.date(2023, 6, 3), Decimal('29.70'), 29.95)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a time series table with daily temperature data
conn.execute('''
CREATE TABLE temperatures (
    date DATE,
    city TEXT,
    temp_celsius DECIMAL(5,2)
);

INSERT INTO temperatures VALUES
    ('2023-06-01', 'New York', 28.5),
    ('2023-06-02', 'New York', 30.2),
    ('2023-06-03', 'New York', 29.7),
    ('2023-06-01', 'London', 22.1),
    ('2023-06-02', 'London', 23.4),
    ('2023-06-03', 'London', 21.9);
''')

# Perform moving average calculation using window function
result = conn.execute('''
SELECT 
    city, 
    date, 
    temp_celsius,
    AVG(temp_celsius) OVER (PARTITION BY city ORDER BY date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as moving_avg
FROM temperatures
ORDER BY city, date
''').fetchall()

for row in result:
    print(row)