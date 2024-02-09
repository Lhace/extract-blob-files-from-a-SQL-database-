import sqlite3
import os

def extract_blob_data_from_database(database_path, table_name, blob_column, output_folder):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Fetch data from the specified table and column
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for row in rows:
        # Extract blob data
        blob_data = row[blob_column]

        # Decode and write the blob data to a file
        file_name = f"{row['id']}.bin"  # Assuming 'id' is a unique identifier in your table
        file_path = os.path.join(output_folder, file_name)

        with open(file_path, 'wb') as file:
            file.write(blob_data)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    # Specify your database details
    database_path = 'your_database.db'
    table_name = 'your_table'
    blob_column = 'your_blob_column'
    output_folder = 'output_files'

    # Execute the extraction function
    extract_blob_data_from_database(database_path, table_name, blob_column, output_folder)
