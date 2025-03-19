# Generated: 2025-03-19 16:33:00.539201
# Result: [(3,), (5,), (7,), (9,), (11,), (13,), (15,), (17,), (19,)]
# Valid: True
# Variable prime: Type: tuple
# Attributes/Methods: count, index
import duckdb

conn = duckdb.connect(':memory:')

# Generate unique sequence of prime numbers using recursive CTE
result = conn.execute('''
WITH RECURSIVE primes(n, candidate) AS (
    SELECT 2, 3
    UNION ALL
    SELECT n + 1, candidate + 2
    FROM primes
    WHERE NOT EXISTS (
        SELECT 1 FROM primes p2 
        WHERE p2.n < primes.n AND candidate % p2.candidate = 0
    ) AND n < 10
)
SELECT candidate FROM primes
''').fetchall()

for prime in result:
    print(prime[0])