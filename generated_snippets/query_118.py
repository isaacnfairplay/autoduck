# Generated: 2025-03-19 14:12:13.599585
# Result: [('Chicago', datetime.date(2023, 7, 2), Decimal('30.20')), ('Chicago', datetime.date(2023, 7, 1), Decimal('29.40')), ('New York', datetime.date(2023, 7, 2), Decimal('33.10')), ('New York', datetime.date(2023, 7, 1), Decimal('32.50'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table with temperature readings and use QUALIFY to get top 2 hottest days per city
conn.execute('CREATE TABLE weather (city TEXT, date DATE, temperature DECIMAL(5,2))')
conn.execute("""INSERT INTO weather VALUES
    ('New York', '2023-07-01', 32.5),
    ('New York', '2023-07-02', 33.1),
    ('New York', '2023-07-03', 31.8),
    ('Chicago', '2023-07-01', 29.4),
    ('Chicago', '2023-07-02', 30.2),
    ('Chicago', '2023-07-03', 28.9)
""")

result = conn.execute('''
    SELECT city, date, temperature
    FROM (
        SELECT city, date, temperature,
               ROW_NUMBER() OVER (PARTITION BY city ORDER BY temperature DESC) as temp_rank
        FROM weather
    ) ranked
    WHERE temp_rank <= 2
''').fetchall()

for row in result:
    print(f"City: {row[0]}, Date: {row[1]}, Temperature: {row[2]}°C")