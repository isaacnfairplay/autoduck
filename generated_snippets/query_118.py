# Generated: 2025-03-19 20:59:03.040755
# Result: [('Hello World', 'HELLO WORLD', 11, 'Hell0 W0rld'), ('DuckDB Rocks', 'DUCKDB ROCKS', 12, 'DuckDB R0cks'), ('SQL Processing', 'SQL PROCESSING', 14, 'SQL Pr0cessing')]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with string manipulation target
conn.sql('''
CREATE TABLE text_data (
    text_content VARCHAR
);

INSERT INTO text_data VALUES
('Hello World'),
('DuckDB Rocks'),
('SQL Processing');
''')

# Demonstrate advanced string processing
result = conn.sql('''
SELECT 
    text_content, 
    UPPER(text_content) as uppercase_text,
    LENGTH(text_content) as text_length,
    REPLACE(text_content, 'o', '0') as text_substitution
FROM text_data
''').fetchall()

print(result)