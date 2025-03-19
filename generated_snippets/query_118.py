# Generated: 2025-03-19 13:51:13.113752
# Result: [(102, 'Books', datetime.datetime(2023, 6, 15, 9, 15), 2, 'Books'), (102, 'Electronics', datetime.datetime(2023, 6, 15, 12, 20), 2, 'Books'), (101, 'Electronics', datetime.datetime(2023, 6, 15, 10, 30), 2, 'Electronics'), (101, 'Clothing', datetime.datetime(2023, 6, 15, 11, 45), 2, 'Electronics')]
# Valid: True
import duckdb

# Connect to in-memory database
conn = duckdb.connect(':memory:')

# Create table with user interaction data
conn.execute('''CREATE TABLE user_clicks (
    user_id INTEGER,
    page_category VARCHAR,
    click_timestamp TIMESTAMP
)''')

# Insert sample click data
conn.execute('''INSERT INTO user_clicks VALUES
    (101, 'Electronics', '2023-06-15 10:30:00'),
    (101, 'Clothing', '2023-06-15 11:45:00'),
    (102, 'Books', '2023-06-15 09:15:00'),
    (102, 'Electronics', '2023-06-15 12:20:00')''')

# Analyze user click patterns using window function
result = conn.execute('''
SELECT 
    user_id, 
    page_category, 
    click_timestamp,
    COUNT(*) OVER (PARTITION BY user_id) as total_page_views,
    FIRST_VALUE(page_category) OVER (PARTITION BY user_id ORDER BY click_timestamp) as first_category
FROM user_clicks
''').fetchall()

print(result)