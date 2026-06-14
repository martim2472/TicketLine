from peewee import SqliteDatabase
import os

# Define o caminho da base de dados (guarda na pasta do projeto)
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'ticketline.db')

db = SqliteDatabase(db_path)

def init_db():
    """Função para ligar à base de dados e criar as tabelas se não existirem."""
    from models import Utilizador, Ticket
    db.connect()
    db.create_tables([Utilizador, Ticket])
    db.close()
