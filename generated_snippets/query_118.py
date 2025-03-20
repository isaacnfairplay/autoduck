# Generated: 2025-03-19 20:06:29.079318
# Result: [('Apple', datetime.date(2023, 1, 15), Decimal('100.50'), Decimal('100.50'), 100.5), ('Apple', datetime.date(2023, 1, 17), Decimal('125.75'), Decimal('226.25'), 113.125), ('Banana', datetime.date(2023, 1, 16), Decimal('75.25'), Decimal('75.25'), 75.25), ('Banana', datetime.date(2023, 1, 18), Decimal('90.00'), Decimal('165.25'), 82.625)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create and populate graph-like relationship table
conn.execute('''
    CREATE TABLE social_network (
        person_id INTEGER,
        friend_id INTEGER
    );
    INSERT INTO social_network VALUES
        (1, 2), (1, 3), (2, 4),
        (3, 4), (4, 5), (5, 1);

    -- Recursive query to find network connections
    WITH RECURSIVE network_paths(start_id, end_id, path, depth) AS (
        SELECT person_id, friend_id, 
               CAST(person_id || '->' || friend_id AS VARCHAR) AS path, 
               1 AS depth
        FROM social_network
        UNION ALL
        SELECT np.start_id, sn.friend_id, 
               np.path || '->' || sn.friend_id, 
               np.depth + 1
        FROM network_paths np
        JOIN social_network sn ON np.end_id = sn.person_id
        WHERE np.depth < 3
    )
    SELECT DISTINCT start_id, end_id, path, depth
    FROM network_paths
    ORDER BY depth;
''').fetchall()