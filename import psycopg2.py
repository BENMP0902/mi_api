import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres.atgxanqwsnttopfxzlwm",
        password="rA2_93#7tK2Meaj",
        host="aws-0-us-west-1.pooler.supabase.com",
        port="6543"
    )
    print("Conexión exitosa")
except psycopg2.OperationalError as e:
    print(f"Error al conectar: {e}")
