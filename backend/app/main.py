from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI(title="IronKing")

# Configuração de diretórios
BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_DIR = BASE_DIR / "frontend" / "static"
TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"

# Configuração de arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="/app/frontend/static"), name="static")
templates = Jinja2Templates(directory="/app/frontend/templates")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "postgres"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database=os.getenv("POSTGRES_DB", "ironking"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres")
        )
        return conn
    except Exception as e:
        return None

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "IronKing"}
    )

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/db-status")
async def db_status():
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()[0]
                return {
                    "status": "connected",
                    "message": "Conexão com o banco de dados estabelecida com sucesso!",
                    "version": version
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erro ao verificar o banco de dados: {str(e)}"
            }
        finally:
            conn.close()
    else:
        return {
            "status": "disconnected",
            "message": "Não foi possível conectar ao banco de dados"
        }