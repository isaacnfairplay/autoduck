# Generated: 2025-03-16 22:45:28.904714
# Result: [('North', 'B', Decimal('1500.000'), Decimal('2500.000'), 1), ('East', 'A', Decimal('1300.000'), Decimal('2400.000'), 2), ('South', 'B', Decimal('1200.000'), Decimal('2000.000'), 3), ('East', 'B', Decimal('1100.000'), Decimal('2400.000'), 4), ('North', 'A', Decimal('1000.000'), Decimal('2500.000'), 5), ('South', 'A', Decimal('800.000'), Decimal('2000.000'), 6)]
# Valid: True
# Variable start_time: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
# Variable result1: Type: tuple
# Attributes/Methods: count, index
# Variable benchmark_query: Type: function
# Variable time: Type: module
# Attributes/Methods: _STRUCT_TM_ITEMS, altzone, asctime, ctime, daylight, get_clock_info, gmtime, localtime, mktime, monotonic, monotonic_ns, perf_counter, perf_counter_ns, process_time, process_time_ns, sleep, strftime, strptime, struct_time, thread_time, thread_time_ns, time, time_ns, timezone, tzname
# Variable sql_time: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
# Variable result2: Type: tuple
# Attributes/Methods: count, index
# Variable rel_api_time: Type: float
# Attributes/Methods: as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
import duckdb
import time

# Performance Benchmarking of Query Approaches
con = duckdb.connect(':memory:')

# Create large sample dataset
con.execute('CREATE TABLE large_data AS SELECT range AS id, random() AS value FROM range(1000000)')

# Benchmark 1: Direct SQL Query
start_time = time.time()
result1 = con.execute('SELECT AVG(value) FROM large_data WHERE id > 500000').fetchone()
sql_time = time.time() - start_time

# Benchmark 2: Relational API
start_time = time.time()
result2 = (con.table('large_data')
    .filter('id > 500000')
    .aggregate('AVG(value)')
    .execute().fetchone())
rel_api_time = time.time() - start_time

print(f'SQL Query Time: {sql_time:.4f} seconds')
print(f'Relational API Time: {rel_api_time:.4f} seconds')
print(f'Results Match: {result1 == result2}')