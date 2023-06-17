import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("DELETE FROM table WHERE search_condition ORDER BY criteria LIMIT row_count OFFSET offset;")
#“LIMIT 4 OFFSET 4” will ignore the first 4 rows, and returned 4 rows starting from the fifth rows, so you will get rows 5,6,7, and 8.
print("Row deleted")
#DROP TABLE [IF EXISTS] [schema_name.]table_name;

conn.close()
