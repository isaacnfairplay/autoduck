# Generated: 2025-03-19 08:41:10.567439
# Result: [('Bob', 'Chess', 1, 88, None, None), ('Bob', 'Chess', 2, 90, 88, 2), ('Alice', 'Chess', 1, 95, None, None), ('Alice', 'Chess', 2, 92, 95, -3), ('Charlie', 'Chess', 1, 85, None, None), ('Charlie', 'Chess', 2, 87, 85, 2)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate table for tournament rankings
conn.execute('CREATE TABLE tournament_results (player TEXT, game TEXT, score INT, round INT)')
conn.executemany('INSERT INTO tournament_results VALUES (?, ?, ?, ?)', [
    ('Alice', 'Chess', 95, 1),
    ('Bob', 'Chess', 88, 1),
    ('Alice', 'Chess', 92, 2),
    ('Bob', 'Chess', 90, 2),
    ('Charlie', 'Chess', 85, 1),
    ('Charlie', 'Chess', 87, 2)
])

# Calculate player's performance improvement using LAG window function
result = conn.execute('''
    SELECT 
        player, 
        game, 
        round, 
        score,
        LAG(score) OVER (PARTITION BY player ORDER BY round) as previous_score,
        score - LAG(score) OVER (PARTITION BY player ORDER BY round) as score_improvement
    FROM tournament_results
''').fetchall()

for row in result:
    print(f"Player: {row[0]}, Game: {row[1]}, Round: {row[2]}, Score: {row[3]}, Previous Score: {row[4]}, Improvement: {row[5]})")