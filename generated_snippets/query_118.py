# Generated: 2025-03-19 09:05:27.956355
# Result: [(102, 4.55, 60, 1), (101, 4.15, 40, 2), (102, 4.55, 60, 3), (101, 4.15, 40, 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a complex data tracking table for product reviews
conn.execute('''CREATE TABLE product_reviews (
    product_id INT,
    reviewer_id INT,
    rating DECIMAL(3,2),
    review_date DATE,
    helpful_votes INT
)''')

# Insert sample review data
conn.executemany('INSERT INTO product_reviews VALUES (?, ?, ?, ?, ?)', [
    (101, 1, 4.5, '2023-07-01', 25),
    (101, 2, 3.8, '2023-07-02', 15),
    (102, 3, 4.9, '2023-07-03', 40),
    (102, 4, 4.2, '2023-07-04', 20)
])

# Analyze reviews using window functions and aggregations
result = conn.execute('''SELECT
    product_id,
    ROUND(AVG(rating) OVER (PARTITION BY product_id), 2) as avg_product_rating,
    SUM(helpful_votes) OVER (PARTITION BY product_id) as total_helpful_votes,
    RANK() OVER (ORDER BY rating DESC) as rating_rank
FROM product_reviews
''').fetchall()

for row in result:
    print(f"Product ID: {row[0]}, Avg Rating: {row[1]}, Total Helpful Votes: {row[2]}, Rating Rank: {row[3]}")