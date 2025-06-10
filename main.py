from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello from FastAPI on GKE!"}

@app.get("/api/dbcheck")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname = "postgres",
            user = "postgres",
            password = "secretpassword",
            host=os.getenv("DB_HOST", "my-postgres-postgresql.my-app.svc.cluster.local"),
             port=5432
        )
        return{"db": "connected"}
    except Exception as e:
        return {"db": "error", "details": str(e)}