import sqlite3
from collections import Counter
from collections import defaultdict
from datetime import date, time, datetime, timedelta, tzinfo, timezone
import pandas as pd
import streamlit as st

conn = sqlite3.connect('ecommerce.db') # Criando a conexão com banco de dados
cursor = conn.cursor() # Executor de comandos

# Criando a tabela de autores
cursor.execute('''
create table if not exists autores (
    id integer primary key autoincrement,
    nome text not null
)
''')

# Criando a tabela de categorias
cursor.execute('''
create table if not exists categorias (
    id integer primary key autoincrement,
    nome text not null          
)
''')

# Criando a tabela de livros
cursor.execute('''
create table if not exists livros (
    id integer primary key autoincrement,
    titulo text not null,
    autor_id integer not null,
    categoria_id integer not null,
    ano text not null,
    quantidade_disponivel integer not null,
    foreign key (autor_id) references autores (id),
    foreign key (categoria_id) references categorias (id)
)
''')

# Criando a tabela de emprestimos
cursor.execute('''
create table if not exists emprestimos (
    id integer primary key autoincrement,
    livro_id integer not null,
    data_emprestimo text not null,
    devolvido integer not null check (devolvido in (0, 1)),
    foreign key (livro_id) references livros (id)
)
''')