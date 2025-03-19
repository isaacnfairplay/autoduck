# Generated: 2025-03-19 19:29:55.259678
# Result: [(datetime.datetime(2023, 1, 1, 10, 0), 2, ['login', 'purchase']), (datetime.datetime(2023, 1, 1, 11, 0), 1, ['logout']), (datetime.datetime(2023, 1, 2, 9, 0), 1, ['login']), (datetime.datetime(2023, 1, 2, 14, 0), 1, ['purchase'])]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create multi-range temporal histogram for event frequency
conn.execute('''CREATE TABLE event_log (
    event_time TIMESTAMP,
    event_type VARCHAR
)''')

conn.execute('''INSERT INTO event_log VALUES
    ('2023-01-01 10:15:00', 'login'),
    ('2023-01-01 10:20:00', 'purchase'),
    ('2023-01-01 11:05:00', 'logout'),
    ('2023-01-02 09:30:00', 'login'),
    ('2023-01-02 14:45:00', 'purchase')''')

# Compute hourly event frequency with time-based windowing
result = conn.execute('''SELECT 
    DATE_TRUNC('hour', event_time) as hour_bucket,
    COUNT(*) as event_count,
    LIST(event_type) as event_types
FROM event_log
GROUP BY hour_bucket
ORDER BY hour_bucket''').fetchall()

for row in result:
    print(f'Hour: {row[0]}, Events: {row[1]}, Types: {row[2]})')