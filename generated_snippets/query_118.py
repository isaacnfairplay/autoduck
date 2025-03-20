# Generated: 2025-03-19 20:23:30.058396
# Result: [('Triangle', 3, Decimal('10.500'), 1), ('Square', 4, Decimal('25.000'), 2), ('Pentagon', 5, Decimal('15.750'), 3), ('Hexagon', 6, Decimal('20.250'), 4)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of geometric shapes
conn.execute('CREATE TABLE shapes (shape VARCHAR, sides INTEGER, area DECIMAL)')
conn.execute("""INSERT INTO shapes VALUES
    ('Triangle', 3, 10.5),
    ('Square', 4, 25.0),
    ('Pentagon', 5, 15.75),
    ('Hexagon', 6, 20.25)
""")

# Use window functions to rank shapes by side count
result = conn.execute('''
    SELECT 
        shape, 
        sides, 
        area,
        RANK() OVER (ORDER BY sides) as side_rank
    FROM shapes
''').fetchall()

for row in result:
    print(f"Shape: {row[0]}, Sides: {row[1]}, Area: {row[2]}, Side Rank: {row[3]}")