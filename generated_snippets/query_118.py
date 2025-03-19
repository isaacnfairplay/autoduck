# Generated: 2025-03-19 08:59:13.038240
# Result: [('GOOGL', 100.5), ('MSFT', 280.75), ('AAPL', 150.25)]
# Valid: True
# Variable avg_price: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
# Variable symbol: Type: str
# Attributes/Methods: capitalize, casefold, center, count, encode, endswith, expandtabs, find, format, format_map, index, isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
import duckdb

conn = duckdb.connect(':memory:')

# Create a table of stock prices
conn.execute('CREATE TABLE stock_prices (symbol TEXT, price DECIMAL(10,2), date DATE)')

# Insert sample stock data
conn.executemany('INSERT INTO stock_prices VALUES (?, ?, ?)', [
    ('AAPL', 150.25, '2023-07-01'),
    ('GOOGL', 100.50, '2023-07-01'),
    ('MSFT', 280.75, '2023-07-01')
])

# Calculate average price for each stock symbol
result = conn.execute('SELECT symbol, AVG(price) as avg_price FROM stock_prices GROUP BY symbol').fetchall()

for symbol, avg_price in result:
    print(f'{symbol}: ${avg_price:.2f}')