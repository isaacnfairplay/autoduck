# Generated: 2025-03-19 10:50:13.016966
# Result: [(1, 4.5, 2), (2, 3.5, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table for product reviews
conn.execute('''
CREATE TABLE reviews (
    product_id INTEGER,
    rating INTEGER,
    review_date DATE
);
''')

conn.executemany('INSERT INTO reviews VALUES (?, ?, ?)', [
    (1, 4, '2023-01-15'),
    (1, 5, '2023-02-20'),
    (2, 3, '2023-03-10'),
    (2, 4, '2023-04-05')
])

# Calculate average rating per product with minimum review count
result = conn.execute('''
SELECT 
    product_id, 
    AVG(rating) as avg_rating,
    COUNT(*) as review_count
FROM reviews
GROUP BY product_id
HAVING COUNT(*) >= 2
''').fetchall()

for row in result:
    print(f'Product {row[0]}: Avg Rating = {row[1]}, Reviews = {row[2]}')