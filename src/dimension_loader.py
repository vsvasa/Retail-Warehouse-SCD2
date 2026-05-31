import pandas as pd
from utils import setup_logger

logger = setup_logger()
def load_dimension(df, table_name, connection):

    cur = None

    try:
        cur = connection.cursor()

        columns = ",".join(df.columns)
        placeholders = ",".join(["%s"] * len(df.columns))

        insert_query = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({placeholders})
        """

        logger.info(df.dtypes)
        logger.info(df.isna().sum())
        logger.info(df.head())

        data = list(df.itertuples(index=False, name=None))
        batch_size = 10000

        for i in range(0, len(data), batch_size):

            batch = data[i:i+batch_size]

            cur.executemany(insert_query, batch)

            connection.commit()

            logger.info(
                f"Inserted rows {i} to {min(i+batch_size,len(data))}"
            )
        logger.info(f"Loading into {table_name}")
        logger.info(f"Columns: {df.columns.tolist()}")

        connection.commit()

        logger.info(f"Loaded {len(df)} records into {table_name}")

    except Exception as e:
        logger.error(f"Error loading {table_name}: {str(e)}")

        if connection:
            connection.rollback()

    finally:
        if cur is not None:
            cur.close()