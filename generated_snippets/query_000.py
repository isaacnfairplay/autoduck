# Generated: 2025-03-16 22:06:16.444357
# Result: [('Bob', 'Marketing', Decimal('60000.00'), 'San Francisco', 60000.0, 1), ('Charlie', 'Sales', Decimal('55000.00'), 'New York', 52500.0, 2), ('Alice', 'Sales', Decimal('50000.00'), 'New York', 52500.0, 3), ('David', 'HR', Decimal('45000.00'), 'Chicago', 45000.0, 4)]
# Valid: True
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable row: Type: tuple
# Attributes/Methods: count, index
import duckdb

# Create an in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables for demonstrating advanced queries
con.execute('''
    CREATE TABLE employees (
        employee_id INT, 
        name VARCHAR, 
        department VARCHAR, 
        salary DECIMAL(10,2)
    );

    CREATE TABLE departments (
        dept_id VARCHAR, 
        dept_name VARCHAR, 
        location VARCHAR
    );

    INSERT INTO employees VALUES
        (1, 'Alice', 'Sales', 50000),
        (2, 'Bob', 'Marketing', 60000),
        (3, 'Charlie', 'Sales', 55000),
        (4, 'David', 'HR', 45000);

    INSERT INTO departments VALUES
        ('Sales', 'Sales Department', 'New York'),
        ('Marketing', 'Marketing Department', 'San Francisco'),
        ('HR', 'Human Resources', 'Chicago');
''')

# Complex multi-table JOIN with window functions
result = con.execute('''
    SELECT 
        e.name, 
        e.department, 
        e.salary,
        d.location,
        AVG(e.salary) OVER (PARTITION BY e.department) as dept_avg_salary,
        RANK() OVER (ORDER BY e.salary DESC) as salary_rank
    FROM employees e
    JOIN departments d ON e.department = d.dept_id
    ORDER BY salary_rank
''').fetchall()

for row in result:
    print(row)
