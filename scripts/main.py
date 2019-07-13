import os
import psycopg2


def lambda_handler(event, context):
    params = dict(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cur:
            cur.execute("select * from users")
            for user in cur.fetchall():
                print(user)
