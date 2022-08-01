## Modificaciones
Se modifica el puerto a 80 para no generar problemas con otros conetenedores como el de PgAdmin
``` yaml
airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - 80:8080
```