# Running postgres Database
sudo docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="toor" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network1 \
  --name pg-database \
  postgres:13

# sudo docker start /pg-database

# Running pgcli
pgcli -h localhost -p 5432 -u root -d ny_taxi

# Running pgadmin
sudo docker run -it \
  -e PGADMIN_DEFAULT_EMAIL='admin@admin.com' \
  -e PGADMIN_DEFAULT_PASSWORD='root' \
  -p 8080:80 \
  --network=pg-network1 \
  --name pgadmin \
  dpage/pgadmin4

# sudo docker start /pgadmin

# Building docker network
docker network create pg-network1

# Cast jupyter notebook to script
jupyter nbconvert --to=script upload-data.ipynb

# executing script
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

python3 ingest_data.py \
  --user=root \
  --password=toor \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}

#
sudo docker build -t taxi_ingest:v001 .

sudo docker run -it \
  --network=pg-network1 \
  taxi_ingest:v001 \
    --user=root \
    --password=toor \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}