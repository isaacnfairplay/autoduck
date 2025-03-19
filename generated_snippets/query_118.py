# Generated: 2025-03-19 08:40:17.652680
# Result: [('Charlie', 'West', 2, Decimal('55000.90'), 1), ('Charlie', 'West', 1, Decimal('52000.75'), 2), ('Alice', 'West', 2, Decimal('48000.60'), 3), ('Alice', 'West', 1, Decimal('45000.50'), 4), ('Bob', 'East', 2, Decimal('41000.30'), 1), ('Bob', 'East', 1, Decimal('38000.25'), 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate sales representative performance table
conn.execute('CREATE TABLE sales_reps (rep_name TEXT, region TEXT, sales_amount DECIMAL(10,2), quarter INT)')
conn.executemany('INSERT INTO sales_reps VALUES (?, ?, ?, ?)', [
    ('Alice', 'West', 45000.50, 1),
    ('Bob', 'East', 38000.25, 1),
    ('Charlie', 'West', 52000.75, 1),
    ('Alice', 'West', 48000.60, 2),
    ('Bob', 'East', 41000.30, 2),
    ('Charlie', 'West', 55000.90, 2)
])

# Calculate sales representative performance ranking within region
result = conn.execute('''
    SELECT 
        rep_name, 
        region, 
        quarter, 
        sales_amount,
        DENSE_RANK() OVER (PARTITION BY region ORDER BY sales_amount DESC) as performance_rank
    FROM sales_reps
''').fetchall()

for row in result:
    print(f"Rep: {row[0]}, Region: {row[1]}, Quarter: {row[2]}, Sales: ${row[3]}, Rank: {row[4]}")