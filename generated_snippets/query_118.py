# Generated: 2025-03-19 18:18:46.490303
# Result: [2, 4, 6, 8]
# Valid: True
# Variable query: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
import duckdb

conn = duckdb.connect(':memory:')

# Transform list elements using array_transform
query = '''
SELECT array_transform([1, 2, 3, 4], x -> x * 2) AS doubled_list;
'''

result = conn.execute(query).fetchone()[0]
print(result)  # Output: [2, 4, 6, 8]