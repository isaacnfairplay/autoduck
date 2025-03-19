# Generated: 2025-03-19 10:39:12.391921
# Result: [('Science Fiction', 4.75, 1), ('Dystopian', 4.6, 1)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a books table with complex schema
conn.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        author VARCHAR,
        publication_year INTEGER,
        genre VARCHAR,
        rating DECIMAL(3,2)
    );
''')

# Insert sample book data
conn.executemany('INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)', [
    (1, 'Dune', 'Frank Herbert', 1965, 'Science Fiction', 4.75),
    (2, '1984', 'George Orwell', 1949, 'Dystopian', 4.60),
    (3, 'The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 4.80)
])

# Demonstrate grouping and filtering with complex conditions
result = conn.execute('''
    SELECT 
        genre, 
        AVG(rating) as avg_rating,
        COUNT(*) as book_count
    FROM books
    WHERE publication_year > 1940
    GROUP BY genre
    HAVING AVG(rating) > 4.5
    ORDER BY avg_rating DESC
''').fetchall()

for row in result:
    print(row)