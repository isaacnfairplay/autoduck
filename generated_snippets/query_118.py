# Generated: 2025-03-19 21:10:29.235579
# Result: [(datetime.date(2023, 1, 1), Decimal('100.00'), 100.0), (datetime.date(2023, 1, 2), Decimal('102.50'), 101.25), (datetime.date(2023, 1, 3), Decimal('101.75'), 101.41666666666667), (datetime.date(2023, 1, 4), Decimal('103.25'), 102.5), (datetime.date(2023, 1, 5), Decimal('105.00'), 103.33333333333333)]
# Valid: True
import duckdb

conn = duckdb.connect(':memory:')

# Create table with numeric array
conn.sql("""
CREATE TABLE numeric_arrays (
    id INTEGER,
    values INTEGER[]
);

INSERT INTO numeric_arrays VALUES
    (1, [1, 2, 3]),
    (2, [4, 5, 6]);

SELECT
    id,
    array_transform(values, x -> x + 10) AS transformed_values
FROM numeric_arrays;
""").show()