import pandas as pd
import sqlite3
import os

# ============================
# CONFIGURAÇÕES
# ============================

EXCEL_PATH = "/mnt/data/db_plano_corte.xlsx"   # caminho do arquivo
SQLITE_DB_PATH = "plano_corte.db"              # nome do banco
TABLE_NAME = "plano_corte"                     # nome da tabela

# ============================
# 1. LER EXCEL
# ============================

df = pd.read_excel(EXCEL_PATH)

print("Arquivo Excel carregado.")
print(df.head())

# ============================
# 2. CONECTAR AO SQLITE
# ============================

conn = sqlite3.connect(SQLITE_DB_PATH)
cursor = conn.cursor()

# ============================
# 3. APAGAR TABELA SE EXISTIR
# ============================

cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
conn.commit()

print(f"Tabela '{TABLE_NAME}' removida (se existia).")

# ============================
# 4. CRIAR TABELA NOVA
# ============================
# Criação automática via pandas
df.to_sql(TABLE_NAME, conn, index=False)

print(f"Tabela '{TABLE_NAME}' criada novamente.")

# ============================
# 5. FECHAR CONEXÃO
# ============================

conn.close()

print("Banco SQLite atualizado com sucesso.")