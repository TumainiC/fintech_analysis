import os
import duckdb
import logging 

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CSV → DuckDB tables (transactions, customers, cards)


def ingest_csv_to_duckdb(csv_file_path, duckdb_connection):
    try:
        logger.info(f"Ingesting CSV files from {csv_file_path} into DuckDB...Please be patient, this may take a moment.")
        duckdb_connection.execute(f"""
            CREATE TABLE IF NOT EXISTS transactions AS 
            SELECT * FROM read_csv_auto('{csv_file_path}/transactions.csv');
        """)
        logger.info("Transactions table created.")
        duckdb_connection.execute(f"""
            CREATE TABLE IF NOT EXISTS customers AS 
            SELECT * FROM read_csv_auto('{csv_file_path}/customers.csv');
        """)
        logger.info("Customers table created.")
        duckdb_connection.execute(f"""
            CREATE TABLE IF NOT EXISTS cards AS 
            SELECT * FROM read_csv_auto('{csv_file_path}/cards.csv');
        """)
        logger.info("Cards table created.")
        logger.info("CSV files ingested successfully into DuckDB.")

    except Exception as e:
        logger.error(f"Error ingesting CSV files: {e}")

tables = ['transactions', 'customers', 'cards']
def testing_tables(duckdb_connection):
    try:
        logger.info("Testing the ingested tables...")
        for table in tables:
            duckdb_connection.table(table).show()
        logger.info("Tables tested successfully.")
    except Exception as e:
        logger.error(f"Error testing tables: {e}")

if __name__ == "__main__":
    
    # Delete if db exists    
    if os.path.exists('./data/db/fintech.db'):
        os.remove('./data/db/fintech.db')

    con = duckdb.connect('./data/db/fintech.db')  # file database
    logging.info("Connected to DuckDB database 'fintech.db'.")
    ingest_csv_to_duckdb("./data/raw", con)
    testing_tables(con)

