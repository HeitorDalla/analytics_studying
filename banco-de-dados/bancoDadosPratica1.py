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

# Inserção de dados na tabela emprestimos
cursor.execute('select count(*) from emprestimos')

if cursor.fetchone()[0] == 0:
    emprestimos_inserir = [
        (1, '2025-05-01', 1),
        (2, '2025-05-05', 0),
        (3, '2025-04-20', 1),
        (4, '2025-05-10', 0),
        (5, '2025-05-15', 1),
        (6, '2025-05-18', 0),
        (7, '2025-05-12', 1),
        (8, '2025-05-21', 0),
        (9, '2025-05-25', 1),
        (10, '2025-05-27', 0)
    ]

    cursor.executemany('insert into emprestimos (livro_id, data_emprestimo, devolvido) values (?, ?, ?)', emprestimos_inserir)

    conn.commit()

# Streamlit

# Título principal
st.title('Prática com SQLite, Python e Streamlit')


# Todos os livros com nome do livro, autor e da categoria
st.subheader("Todos os livros com nome do livro, autor e da categoria", divider='grey')
st.write('\n')

df = pd.read_sql_query('''
    select
        l.titulo as `Nome do livro`,
        a.nome as `Nome do autor`,
        c.nome as `Nome da categorias`
    from livros l
    inner join categorias c on l.categoria_id = c.id
    inner join autores a on l.autor_id = a.id
''', conn)
st.dataframe(df)
st.write('\n')


# Filtro de livros por ano de publicação
st.subheader("Filtro de livros por ano de publicação", divider='grey')
st.write("\n")

# Buscar anos únicos de publicação
df_anos = pd.read_sql_query('''
    select
        distinct l.ano as `Ano de publicação`
    from livros l
    order by `Ano de publicação`
''', conn)

# Opções de escolha para o usuário
anosEscolha = st.selectbox('Ano de publicaçao', df_anos['Ano de publicação'])

# Buscar todos os livros filtrado pelo ano de publicação escolhido
livroAno = pd.read_sql_query('''
    select
        l.titulo as `Nome do livro`
    from livros l
    where l.ano = ?
    order by l.ano
''', conn, params=(anosEscolha,))

st.dataframe(livroAno)
st.write('\n')


# Quantidade total de livros, de empréstimos e devolvidos
st.subheader("Quantidade total de livros, de empréstimos e devolvidos", divider='grey')
st.write("\n")

cursor.execute('select count(*) from emprestimos')
totalLivros = cursor.fetchone()[0]

cursor.execute('select count(*) from emprestimos where devolvido = 0')
qtdDevolvido = cursor.fetchone()[0]

cursor.execute('select count(*) from emprestimos where devolvido = 1')
qtdNaoDevolvido = cursor.fetchone()[0]

st.write("O total de livros é: {}" .format(totalLivros))
st.write("O total de livros devolvidos é: {}" .format(qtdDevolvido))
st.write("O total de livros não devolvidos é: {}" .format(qtdNaoDevolvido))

st.write('\n')