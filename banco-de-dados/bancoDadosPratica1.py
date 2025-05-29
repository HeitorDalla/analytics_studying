import sqlite3
from collections import Counter
from collections import defaultdict
from datetime import date, time, datetime, timedelta, tzinfo, timezone
import pandas as pd
import streamlit as st

conn = sqlite3.connect('ecommerce.db') # Criando a conexão com banco de dados
cursor = conn.cursor() # Executor de comandos

# Criando tabela de emprestimos
cursos.execute('''
create table if not exists emprestimos(
    id integer primary key autoincrement,
    data_emprestimo test not null,
    devolvido integer not null
)
''')
