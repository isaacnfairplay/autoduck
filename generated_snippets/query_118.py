# Generated: 2025-03-19 21:35:36.333311
# Result: [('C', 'D', Decimal('0.40'), Decimal('0.40')), ('B', 'D', Decimal('0.85'), Decimal('0.85')), ('A', 'B', Decimal('0.75'), Decimal('0.75')), ('A', 'C', Decimal('0.60'), Decimal('0.75')), ('D', 'E', Decimal('0.95'), Decimal('0.95'))]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a graph-like table of connections
conn.execute('''
CREATE TABLE network_connections (
    source_node VARCHAR,
    destination_node VARCHAR,
    connection_weight DECIMAL(5,2)
)''')

# Insert network topology data
conn.executemany('INSERT INTO network_connections VALUES (?, ?, ?)', [
    ('A', 'B', 0.75),
    ('A', 'C', 0.60),
    ('B', 'D', 0.85),
    ('C', 'D', 0.40),
    ('D', 'E', 0.95)
])

# Use window functions to find max connection weight per source node
result = conn.sql('''
SELECT 
    source_node,
    destination_node,
    connection_weight,
    MAX(connection_weight) OVER (PARTITION BY source_node) as max_node_weight
FROM network_connections
''').fetchall()

print(result)