# Generated: 2025-03-19 14:43:09.228551
# Result: []
# Valid: True
import duckdb

# Complex nested array transformation and filtering
conn = duckdb.connect(':memory:')

result = conn.execute("""
    SELECT 
        array_filter(
            array_transform(
                [[1, 2], [3, 4], [5, 6]], 
                x -> [x[0] * 2, x[1] * 3]
            ), 
            x -> x[0] > 5
        ) AS transformed_arrays
""").fetchone()[0]

print(result)  # Expected: [[6, 9], [10, 18]]