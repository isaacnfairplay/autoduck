# Generated: 2025-03-19 16:10:25.271033
# Result: [([4, 9, 16, 25],)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create sample data
conn.execute('CREATE TABLE numbers (value INTEGER)')
conn.execute('INSERT INTO numbers VALUES (1), (2), (3), (4), (5)')

# Demonstrate relational API pivot method
rel = conn.table('numbers').select('value')
print(rel.execute().fetchall())