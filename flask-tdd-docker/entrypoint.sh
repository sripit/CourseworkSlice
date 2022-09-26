#because api depends on docker and postgres being up,, we r creating
#an entryway

echo "Waiting for postgres..."
#referenced the Postgres container using name of service (api-db)
while ! nc -z api-db 5432; do
  #loop continnues until "Connection to api-db port 5432 succeeded
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0