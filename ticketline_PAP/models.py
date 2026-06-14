from peewee import *
from database import db

class BaseModel(Model):
    """Classe base que define a base de dados a usar em todos os modelos"""
    class Meta:
        database = db

class Utilizador(BaseModel):
    nome = CharField()
    email = CharField(unique=True)
    password_hash = CharField()
    tipo = CharField(choices=[('cliente', 'Cliente'), ('helpdesk', 'Helpdesk')])
    
class Ticket(BaseModel):
    titulo = CharField()
    descricao = TextField()
    estado = CharField(choices=[('aberto', 'Aberto'), ('em_progresso', 'Em Progresso'), ('fechado', 'Fechado')], default='aberto')
    # O cliente que criou o ticket
    criado_por = ForeignKeyField(Utilizador, backref='meus_tickets')
    # O agente do helpdesk que está a tratar do ticket
    atribuido_a = ForeignKeyField(Utilizador, backref='tickets_atribuidos', null=True)
