import sqlite3
from collections import Counter
from collections import defaultdict
from datetime import date, time, datetime, timedelta, tzinfo, timezone
import pandas as pd
import streamlit as st

conn = sqlite3.connect('banco-de-dados/ecommerce.db') # Criando a conexão com banco de dados
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


# 1 - Todos os livros com nome do livro, autor e da categoria
st.subheader("Todos os livros com nome do livro, autor e da categoria", divider='grey')
st.write('\n')

df_filtroLivro = pd.read_sql_query('''
    select
        l.titulo as `Nome do livro`,
        a.nome as `Nome do autor`,
        c.nome as `Nome da categorias`
    from livros l
    inner join categorias c on l.categoria_id = c.id
    inner join autores a on l.autor_id = a.id
''', conn)
st.dataframe(df_filtroLivro)
st.write('\n')


# 2 - Filtro de livros por ano de publicação
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


# 3 - Quantidade total de livros, de empréstimos e devolvidos
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


# 4 - Número de livros por categoria (agrupado)
st.subheader("Número de livros por categoria (agrupado)")
st.write("\n")

# Buscar todas as categorias existentes
df_categorias = pd.read_sql_query('''
    select
        distinct c.nome as `Categoria Livro`
    from categorias c
    group by c.nome
    order by c.nome
''', conn)

categoriaEscolha = st.selectbox('Nome da categoria', df_categorias['Categoria Livro'])

# Buscar a quantidade de livros na categoria especificada
df_quantidadeLivros = pd.read_sql_query('''
    select
        count(*) as `Quantidade de livros`
    from livros l
    inner join categorias c on l.categoria_id = c.id
    where c.nome = ?
''', conn, params=(categoriaEscolha,))

st.dataframe(df_quantidadeLivros)
st.write("\n")


# 5 - Formulário para registrar um novo livro
st.subheader("Inserção de um novo Livro", divider='grey')

# Carrega os autores e categorias existentes (dataframe)
df_autores = pd.read_sql_query('select id, nome from autores order by nome', conn)
df_categorias = pd.read_sql_query('select id, nome from categorias order by nome', conn)

with st.form("form inserir livro", clear_on_submit=True):
    titulo = st.text_input("Nome do livro")
    autor = st.selectbox("Nome do autor", df_autores['nome'])
    categoria = st.selectbox("Categorias", df_categorias['nome'])
    ano = st.text_input("Ano de publicação[AAAA]")
    quantidadeDisponivel = st.number_input("Quantidade disponível", min_value=0.0, step=1.0)

    enviar = st.form_submit_button("Inserir")

    anoAtual = datetime.now().year

    if enviar:
        if titulo and autor and categoria and ano and quantidadeDisponivel is not None:
            try:
                anoInteiro = int(ano)

                if 1000 <= anoInteiro <= anoAtual:
                    # Recuperar os ids correspondentes ao nome
                    autor_id = int(df_autores[df_autores['nome'] == autor]['id'].values[0])
                    categoria_id = int(df_categorias[df_categorias['nome'] == categoria]['id'].values[0])

                    cursor.execute('''
                        insert into livros
                        (titulo, autor_id, categoria_id, ano, quantidade_disponivel)
                        values (?, ?, ?, ?, ?)
                    ''', (titulo, autor_id, categoria_id, ano, int(quantidadeDisponivel)))

                    conn.commit()
                    st.success("Livro inserido com sucesso!")
                else:
                    st.error("Livro com ano de lançamento acima do esperado!")
            except ValueError:
                st.error("O ano deve ser numérico!")
        else:
            st.error("Preencha todos os campos corretamente!")


# 6 - Formulário para editar um autor (alterar o nome)
st.subheader("Editar um autor", divider='grey')

with st.form("form alterar autor", clear_on_submit=True):
    autorMudar = st.selectbox("Autores", df_autores['nome'])
    novoAutor = st.text_input("Nome do Autor")

    enviar = st.form_submit_button("Editar")

    if enviar:
        if novoAutor.strip():
            # Recupear o id do autor
            autor_id = int(df_autores[df_autores['nome'] == autorMudar]['id'].values[0])
            
            cursor.execute('''
                update autores
                set nome = ?
                where id = ?
            ''', (novoAutor, autor_id))

            conn.commit()
            st.success("Nome do autor alterado!")
        else:
            st.error("Preencha todos os campos corretamente!")


# 7 - Formulário para editar um livro (alterar titulo, categoria, quantidade disponivel
st.subheader("Editar todas as informações de um livro")

df_livroAlterar = pd.read_sql_query("select * from livros order by id", conn)
df_categorias = pd.read_sql_query("select * from categorias order by nome", conn)

with st.form("Editar informações do livro", clear_on_submit=True):
    livros = st.selectbox("Livros", df_livroAlterar['titulo'])
    tituloMudar = st.text_input("Título")
    categoriaMudar = st.selectbox("Categorias", df_categorias['nome'])
    quantidadeMudar = st.number_input("Quantidade disponível", min_value=1, step=1)

    enviar = st.form_submit_button("Editar")

    if enviar:
        if livros and tituloMudar and quantidadeMudar is not None:
            indiceLivroMudar = int(df_livroAlterar[df_livroAlterar['titulo'] == livros]['id'].values[0])
            indiceCategoriaMudar = int(df_categorias[df_categorias['nome'] == categoriaMudar]['id'].values[0])

            cursor.execute('''
                update livros
                set titulo = ?, categoria_id = ?, quantidade_disponivel = ?
                where id = ?
            ''', (tituloMudar, indiceCategoriaMudar, quantidadeMudar, indiceLivroMudar))

            conn.commit()
            st.success("Informações do livro alterado!")
        else:
            st.write("Erro ao validar campos!")