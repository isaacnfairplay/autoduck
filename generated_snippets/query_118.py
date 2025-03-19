# Generated: 2025-03-19 14:00:56.810202
# Result: [('Python', 2, 27500.0, 1), ('C++', 1, 7500.0, 2)]
# Valid: True
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a temporary table of GitHub repositories
conn.execute("""
CREATE TABLE repositories (
    name TEXT,
    stars INTEGER,
    language TEXT,
    created_date DATE
);

INSERT INTO repositories VALUES
    ('duckdb', 7500, 'C++', '2019-01-01'),
    ('pandas', 33000, 'Python', '2012-01-15'),
    ('numpy', 22000, 'Python', '2005-11-03');
"""
)

# Complex query using window functions and aggregations
result = conn.execute("""
SELECT 
    language, 
    COUNT(*) as repo_count,
    AVG(stars) as avg_stars,
    RANK() OVER (ORDER BY AVG(stars) DESC) as star_rank
FROM repositories
GROUP BY language
ORDER BY avg_stars DESC
""").fetchall()

for row in result:
    print(row)