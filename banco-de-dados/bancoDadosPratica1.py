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

conn.commit()

# Inserção dos dados da tabela autores
cursor.execute('select count(*) from autores')

if cursor.fetchone()[0] == 0:
    autores_inserir = [
        ('Alice Monteiro',),
        ('Bruno Cardoso',),
        ('Camila Figueiredo',),
        ('Daniel Vasques',),
        ('Elisa Moura',),
        ('Felipe Andrade',),
        ('Gabriela Tavares',),
        ('Henrique Silveira',),
        ('Isabela Nunes',),
        ('João Pedro Ribeiro',)
    ]

    cursor.executemany('insert into autores (nome) values (?)', autores_inserir)

    conn.commit()

# Inserção de dados na tabela categorias
cursor.execute('select count(*) from categorias')

if cursor.fetchone()[0] == 0:
    categorias_inserir = [
        ('Romance',),
        ('Ficção Científica',),
        ('Biografia',),
        ('História',),
        ('Autoajuda',),
        ('Tecnologia',),
        ('Fantasia',),
        ('Suspense',),
        ('Psicologia',),
        ('Negócios',)
    ]

    cursor.executemany('insert into categorias (nome) values (?)', categorias_inserir)

    conn.commit()

# Inserção de dados na tabela livros
cursor.execute('select count(*) from livros')

if cursor.fetchone()[0] == 0:
    livros_inserir = [
        ('O Amor em Tempos Modernos', 1, 1, '2018', 5),
        ('Além das Estrelas', 2, 2, '2020', 3),
        ('A Vida de Einstein', 3, 3, '2016', 2),
        ('Brasil Colonial', 4, 4, '2014', 4),
        ('Desperte o Gigante Interior', 5, 5, '2010', 6),
        ('Inteligência Artificial Hoje', 6, 6, '2023', 7),
        ('Reinos Esquecidos', 7, 7, '2019', 2),
        ('O Mistério da Noite', 8, 8, '2022', 5),
        ('Mente e Emoção', 9, 9, '2017', 4),
        ('Empreender com Propósito', 10, 10, '2021', 8)
    ]

    cursor.executemany('insert into livros (titulo, autor_id, categoria_id, ano, quantidade_disponivel) values (?, ?, ?, ?, ?)', livros_inserir)

    conn.commit()

