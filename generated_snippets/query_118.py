# Generated: 2025-03-19 15:03:03.770673
# Result: []
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and query temporal data using date functions
conn.execute('''CREATE TABLE events (
    event_name VARCHAR,
    event_date DATE
)''')

conn.execute('''INSERT INTO events VALUES
    ('Conference', '2023-07-15'),
    ('Workshop', '2023-08-20'),
    ('Seminar', '2024-01-10')''')

result = conn.execute('''SELECT 
    event_name, 
    event_date, 
    DATE_TRUNC('month', event_date) as month_start,
    DATEDIFF('day', CURRENT_DATE, event_date) as days_until_event
FROM events
WHERE event_date > CURRENT_DATE
ORDER BY days_until_event''').fetchall()

print(result)