# Generated: 2025-03-19 14:19:01.345385
# Result: [Decimal('90.0'), Decimal('180.0'), Decimal('270.0')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Transform fruit prices by applying percentage discount
result = conn.execute('''
    SELECT array_transform([100, 200, 300], x -> x * 0.9) AS discounted_prices
''').fetchone()[0]

print(result)  # Output: [90.0, 180.0, 270.0]