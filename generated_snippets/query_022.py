# Generated: 2025-03-16 22:16:17.602614
# Result: [('Laptop', 'Electronics', datetime.date(2023, 1, 15), 5, Decimal('999.99'), Decimal('4999.95'), 1), ('Smartphone', 'Electronics', datetime.date(2023, 2, 20), 3, Decimal('599.50'), Decimal('6798.45'), 2), ('Tablet', 'Electronics', datetime.date(2023, 3, 10), 2, Decimal('399.75'), Decimal('7597.95'), 3)]
# Valid: True
# Variable row: Type: tuple
# Attributes/Methods: count, index
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
# Variable result: Type: list
# Attributes/Methods: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
import duckdb

# Establish in-memory database connection
con = duckdb.connect(':memory:')

# Create sample tables for complex analysis
con.sql('''
    CREATE TABLE sales (
        product_id INTEGER,
        sale_date DATE,
        quantity INTEGER,
        price DECIMAL(10,2)
    );

    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        category VARCHAR
    );
''');

# Insert sample data
con.sql('''
    INSERT INTO products VALUES
        (1, 'Laptop', 'Electronics'),
        (2, 'Smartphone', 'Electronics'),
        (3, 'Tablet', 'Electronics');

    INSERT INTO sales VALUES
        (1, '2023-01-15', 5, 999.99),
        (2, '2023-02-20', 3, 599.50),
        (3, '2023-03-10', 2, 399.75);
''');

# Complex analytical query with window functions and joins
result = con.sql('''
    SELECT 
        p.name AS product_name,
        p.category,
        s.sale_date,
        s.quantity,
        s.price,
        SUM(s.quantity * s.price) OVER (PARTITION BY p.category ORDER BY s.sale_date) AS cumulative_category_revenue,
        RANK() OVER (PARTITION BY p.category ORDER BY s.quantity DESC) AS sales_rank
    FROM sales s
    JOIN products p ON s.product_id = p.id
''').fetchall()

for row in result:
    print(row)