from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# Agora o backend NÃO SABE onde está o banco.
# As informações vêm de variáveis de ambiente.
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

@app.get("/orders")
def list_orders():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM orders")
        return cur.fetchall()

@app.post("/orders")
def create_order(order: dict):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO orders (product, quantity, status) VALUES (%s, %s, 'NEW')",
            (order["product"], order["quantity"])
        )
        conn.commit()

    return {"message": "Pedido criado"}