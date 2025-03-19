# Generated: 2025-03-19 09:11:26.828488
# Result: [(1, datetime.datetime(2023, 7, 15, 10, 0), Decimal('100.50'), Decimal('100.50'), 225.41666666666666), (1, datetime.datetime(2023, 7, 15, 11, 30), Decimal('250.75'), Decimal('351.25'), 225.41666666666666), (1, datetime.datetime(2023, 7, 15, 13, 45), Decimal('325.00'), Decimal('676.25'), 225.41666666666666), (2, datetime.datetime(2023, 7, 15, 12, 15), Decimal('75.25'), Decimal('75.25'), 75.25)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create time series transaction data
conn.execute('CREATE TABLE transactions (user_id INT, amount DECIMAL(10,2), timestamp TIMESTAMP)')

conn.executemany('INSERT INTO transactions VALUES (?, ?, ?)', [
    (1, 100.50, '2023-07-15 10:00:00'),
    (1, 250.75, '2023-07-15 11:30:00'),
    (2, 75.25, '2023-07-15 12:15:00'),
    (1, 325.00, '2023-07-15 13:45:00')
])

# Calculate user-level cumulative transaction metrics
result = conn.execute('''SELECT
    user_id,
    timestamp,
    amount,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY timestamp) as cumulative_amount,
    AVG(amount) OVER (PARTITION BY user_id) as avg_transaction
FROM transactions
''').fetchall()

for row in result:
    print(f"User ID: {row[0]}, Time: {row[1]}, Amount: ${row[2]}, Cumulative: ${row[3]}, Avg Transaction: ${row[4]:.2f}")