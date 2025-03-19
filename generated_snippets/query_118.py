# Generated: 2025-03-19 17:27:26.930878
# Result: [('Simone Biles', 'USA', 'Gymnastics', 3, 1), ('Katie Ledecky', 'USA', 'Swimming', 3, 1), ('Michael Phelps', 'USA', 'Swimming', 3, 1)]
# Valid: True
# Variable squared: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable square_array: Type: function
# Variable original: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

conn = duckdb.connect(':memory:')

def square_array(numbers):
    result = conn.execute("SELECT array_transform(?, x -> x * x) AS squared_numbers", [numbers]).fetchone()[0]
    return result

original = [1, 2, 3, 4, 5]
squared = square_array(original)
print(f"Original: {original}")
print(f"Squared: {squared}")