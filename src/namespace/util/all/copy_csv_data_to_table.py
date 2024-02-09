from psycopg2 import sql


def copy_csv_data_to_table(conn, csv_file, table_name):
    with conn.cursor() as cursor:
        with open(csv_file, "r") as f:
            # Reset the cursor's position to the beginning of the file
            f.seek(0)
            
            # Construct the COPY command
            copy_command = sql.SQL("COPY {} FROM STDIN WITH (FORMAT csv, HEADER true);").format(sql.Identifier(table_name))

            # Use copy_expert to copy the file to the table
            cursor.copy_expert(copy_command, f)