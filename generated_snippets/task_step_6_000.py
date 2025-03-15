# Generated: 2025-03-15 17:01:07.369270
# Result: [('Marketing', 60000.0, 1), ('HR', 58000.0, 1), ('Sales', 53500.0, 2)]
# Valid: True
# Variable row: Type: tuple
# Attributes/Methods: count, index
# Variable conn: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Connect to an in-memory database
conn = duckdb.connect(':memory:')

# Create a table
conn.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10,2)
    )
""")

# Insert sample data
conn.executemany("""
    INSERT INTO employees VALUES (?, ?, ?, ?)
""", [
    (1, 'Alice', 'Sales', 55000.00),
    (2, 'Bob', 'Marketing', 60000.00),
    (3, 'Charlie', 'Sales', 52000.00),
    (4, 'David', 'HR', 58000.00)
])

# Perform a simple query
result = conn.execute("""
    SELECT department, 
           AVG(salary) as avg_salary, 
           COUNT(*) as employee_count
    FROM employees
    GROUP BY department
    ORDER BY avg_salary DESC
""").fetchall()

# Print the results
print("Department Salary Summary:")
for row in result:
    print(f"Department: {row[0]}, Avg Salary: ${row[1]:.2f}, Employees: {row[2]}")

# Close the connection
conn.close()