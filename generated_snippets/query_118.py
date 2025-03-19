# Generated: 2025-03-19 11:54:51.598122
# Result: [('Haruki Murakami', 'Kafka on the Shore', 2002)]
# Valid: True
import duckdb

# Create an in-memory database
conn = duckdb.connect(':memory:')

# Create authors table
conn.execute('CREATE TABLE authors (author_id INT PRIMARY KEY, name TEXT, country TEXT)')
conn.executemany('INSERT INTO authors VALUES (?, ?, ?)', [
    (1, 'Haruki Murakami', 'Japan'),
    (2, 'Chimamanda Ngozi Adichie', 'Nigeria'),
    (3, 'Kazuo Ishiguro', 'United Kingdom')
])

# Create books table with foreign key relationship
conn.execute('CREATE TABLE books (book_id INT PRIMARY KEY, title TEXT, author_id INT, publication_year INT, FOREIGN KEY(author_id) REFERENCES authors(author_id))')
conn.executemany('INSERT INTO books VALUES (?, ?, ?, ?)', [
    (101, 'Kafka on the Shore', 1, 2002),
    (102, 'Norwegian Wood', 1, 1987),
    (103, 'Americanah', 2, 2013),
    (104, 'Never Let Me Go', 3, 2005)
])

# Demonstrate join and filtering
result = conn.execute('''
    SELECT a.name, b.title, b.publication_year
    FROM authors a JOIN books b ON a.author_id = b.author_id
    WHERE a.country = 'Japan' AND b.publication_year > 1990
''').fetchall()

print(result)