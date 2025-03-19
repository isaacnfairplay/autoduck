# Generated: 2025-03-19 14:47:37.491514
# Result: [(datetime.date(2023, 1, 1), Decimal('100.50'), 100.5), (datetime.date(2023, 1, 2), Decimal('200.75'), 150.625), (datetime.date(2023, 1, 3), Decimal('150.25'), 175.5)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Compute rolling average of sales with window function
conn.execute('CREATE TABLE sales (date DATE, amount DECIMAL(10,2))')
conn.execute("INSERT INTO sales VALUES ('2023-01-01', 100.50), ('2023-01-02', 200.75), ('2023-01-03', 150.25)")

result = conn.execute("""
    SELECT 
        date, 
        amount, 
        AVG(amount) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as rolling_avg
    FROM sales
""").fetchall()

for row in result:
    print(f"Date: {row[0]}, Amount: ${row[1]}, Rolling Avg: ${row[2]:.2f}")