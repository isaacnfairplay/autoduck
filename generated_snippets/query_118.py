# Generated: 2025-03-19 17:26:36.644647
# Result: [('Simone Biles', 'USA', 'Gymnastics', 3, 1), ('Katie Ledecky', 'USA', 'Swimming', 3, 1), ('Michael Phelps', 'USA', 'Swimming', 3, 1)]
# Valid: True
# Variable con: Type: DuckDBPyConnection
# Attributes/Methods: _pybind11_conduit_v1_(), append(), array_type(), arrow(), begin(), checkpoint(), close(), commit(), create_function(), cursor(), decimal_type(), description, df(), dtype(), duplicate(), enum_type(), execute(), executemany(), extract_statements(), fetch_arrow_table(), fetch_df(), fetch_df_chunk(), fetch_record_batch(), fetchall(), fetchdf(), fetchmany(), fetchnumpy(), fetchone(), filesystem_is_registered(), from_arrow(), from_csv_auto(), from_df(), from_parquet(), from_query(), get_table_names(), install_extension(), interrupt(), list_filesystems(), list_type(), load_extension(), map_type(), pl(), query(), read_csv(), read_json(), read_parquet(), register(), register_filesystem(), remove_function(), rollback(), row_type(), rowcount, sql(), sqltype(), string_type(), struct_type(), table(), table_function(), tf(), torch(), type(), union_type(), unregister(), unregister_filesystem(), values(), view()
import duckdb

con = duckdb.connect(':memory:')

# Create and populate a table with Olympic medal data
con.execute('''CREATE TABLE olympic_medals (
    athlete TEXT,
    country TEXT,
    sport TEXT,
    medal_type TEXT
)''')

con.execute('''INSERT INTO olympic_medals VALUES
    ('Simone Biles', 'USA', 'Gymnastics', 'Gold'),
    ('Katie Ledecky', 'USA', 'Swimming', 'Gold'),
    ('Michael Phelps', 'USA', 'Swimming', 'Gold')''')

# Use window function to rank athletes by medal count
result = con.execute('''SELECT 
    athlete, 
    country, 
    sport, 
    COUNT(*) OVER (PARTITION BY country) as country_medals,
    RANK() OVER (ORDER BY medal_type DESC) as medal_rank
FROM olympic_medals''').fetchall()

for row in result:
    print(row)