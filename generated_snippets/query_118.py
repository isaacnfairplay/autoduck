# Generated: 2025-03-19 19:16:59.195069
# Result: [11, 12, 13, 14]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a product reviews table with sentiment analysis
conn.sql("""
CREATE TABLE reviews (
    product_id INTEGER,
    review_text VARCHAR,
    rating DECIMAL(2,1)
);

INSERT INTO reviews VALUES
(1, 'Great product!', 4.5),
(1, 'Amazing quality', 5.0),
(2, 'Not impressed', 2.0);

-- Calculate average rating and count of reviews per product
SELECT 
    product_id, 
    ROUND(AVG(rating), 1) AS avg_rating,
    COUNT(*) AS review_count,
    LIST(review_text) AS review_texts
FROM reviews
GROUP BY product_id
HAVING review_count > 1;
""").show()