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

# Building docker network
docker network create pg-network1