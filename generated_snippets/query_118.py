# Generated: 2025-03-19 19:00:47.792272
# Result: [('Clothing', 2, 100, Decimal('79.50'), Decimal('7950.00')), ('Electronics', 1, 50, Decimal('499.99'), Decimal('47499.25')), ('Electronics', 3, 25, Decimal('899.99'), Decimal('47499.25')), ('Home', 4, 75, Decimal('149.99'), Decimal('11249.25'))]
# Valid: True
# Variable transformed_array: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

# Create numeric array and perform element-wise transformation
array_data = [1, 2, 3, 4, 5]
transformed_array = conn.sql('SELECT array_transform([1, 2, 3, 4, 5], x -> x + 10) AS result').fetchone()[0]

print(f'Original Array: {array_data}')
print(f'Transformed Array: {transformed_array}')