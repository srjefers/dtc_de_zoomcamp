import os
import argparse
import pandas as pd
import pyarrow.parquet as pq
from time import time
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    output_file = f"{table_name}.parquet"

    # Dowload data file
    os.system(f'wget {url} -O {output_file}')

    # DB connection
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    t_start = time()

    parquet_file = pq.ParquetFile(output_file)
    for indx, batch in enumerate(parquet_file.iter_batches(batch_size=10000)):
        batch_df = batch.to_pandas()
        batch_df.tpep_pickup_datetime = pd.to_datetime(batch_df.tpep_pickup_datetime)
        batch_df.tpep_dropoff_datetime = pd.to_datetime(batch_df.tpep_dropoff_datetime)
        
        if indx == 0:
            batch_df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
            batch_df.to_sql(name=table_name, con=engine, if_exists='append')
        else:
            batch_df.to_sql(name=table_name, con=engine, if_exists='append')
        
    t_end = time()
    print('Sussecfully inserted, took %.3f' % (t_end - t_start))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest data to Postgres.')

    # user
    # password 
    # host
    # port 
    # database name 
    # table name
    # url of the csv

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the postgres table')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    main(args)


