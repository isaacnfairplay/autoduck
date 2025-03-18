# Generated: 2025-03-18 11:49:12.815398
# Result: [('Engineering', 75000.0, 1), ('Sales', 57500.0, 2)]
# Valid: True
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

# Create an in-memory connection
con = duckdb.connect(':memory:')

# Create a sample table with employee data
con.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    );
''')

# Insert sample data
con.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', [
    (1, 'Alice', 'Sales', 55000.00),
    (2, 'Bob', 'Engineering', 75000.00),
    (3, 'Charlie', 'Sales', 60000.00)
])

# Perform a query with aggregation and filtering
result = con.execute('''
    SELECT department, 
           AVG(salary) as avg_salary, 
           COUNT(*) as employee_count
    FROM employees
    WHERE salary > 50000
    GROUP BY department
''').fetchall()

print(result)