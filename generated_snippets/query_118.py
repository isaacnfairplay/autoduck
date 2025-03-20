# Generated: 2025-03-19 20:54:40.698883
# Result: [(101, datetime.datetime(2023, 6, 15, 8, 0), datetime.datetime(2023, 6, 15, 10, 30), datetime.timedelta(seconds=9000), datetime.datetime(2023, 6, 15, 8, 0)), (102, datetime.datetime(2023, 6, 15, 9, 15), datetime.datetime(2023, 6, 15, 11, 45), datetime.timedelta(seconds=9000), datetime.datetime(2023, 6, 15, 9, 0)), (103, datetime.datetime(2023, 6, 15, 10, 30), datetime.datetime(2023, 6, 15, 13, 0), datetime.timedelta(seconds=9000), datetime.datetime(2023, 6, 15, 10, 0))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create temporal dataset
conn.sql('''
CREATE TABLE flights (
    flight_id INTEGER,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    duration_minutes INTEGER
);

INSERT INTO flights VALUES
(101, '2023-06-15 08:00:00', '2023-06-15 10:30:00', 150),
(102, '2023-06-15 09:15:00', '2023-06-15 11:45:00', 150),
(103, '2023-06-15 10:30:00', '2023-06-15 13:00:00', 150);
'''
)

# Demonstrate timestamp function and interval calculation
result = conn.sql('''
SELECT 
    flight_id,
    departure_time,
    arrival_time,
    (arrival_time - departure_time) AS actual_duration,
    date_trunc('hour', departure_time) AS departure_hour
FROM flights
''').fetchall()

print(result)