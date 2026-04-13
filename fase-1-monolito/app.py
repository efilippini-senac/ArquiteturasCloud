# Importa o framework FastAPI
from fastapi import FastAPI

# Importa suporte para retornar HTML
from fastapi.responses import HTMLResponse

# Importa a biblioteca de conexão com PostgreSQL
import psycopg2

# Cria a aplicação web
app = FastAPI()

# Conexão com o banco de dados
# Neste caso, o banco roda NA MESMA VM
conn = psycopg2.connect(
    host="localhost",
    database="orders",
    user="orders",
    password="orders"
)

# Página inicial (frontend)
@app.get("/", response_class=HTMLResponse)
def home():
    return open("templates/index.html").read()

# Endpoint para listar pedidos
@app.get("/orders")
def list_orders():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM orders")
        return cur.fetchall()

# Endpoint para criar pedido
@app.post("/orders")
def create_order(order: dict):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO orders (product, quantity, status) VALUES (%s, %s, 'NEW')",
            (order["product"], order["quantity"])
        )
        conn.commit()

    return {"message": "Pedido criado"}