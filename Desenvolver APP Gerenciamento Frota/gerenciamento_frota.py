import sqlite3
from datetime import datetime

conn = sqlite3.connect('frota.db')
c = conn.cursor()

# Cria a tabela Veículo
c.execute('''CREATE TABLE IF NOT EXISTS veiculo
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              modelo TEXT NOT NULL,
              ano INTEGER NOT NULL,
              quilometragem INTEGER NOT NULL)''')

# Cria a tabela Motorista
c.execute('''CREATE TABLE IF NOT EXISTS motorista
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT NOT NULL,
              cnh TEXT NOT NULL,
              telefone TEXT)''')

# Cria a tabela Manutenção
c.execute('''CREATE TABLE IF NOT EXISTS manutencao
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              veiculo_id INTEGER NOT NULL,
              data TEXT NOT NULL,
               descricao TEXT NOT NULL,
               FOREIGN KEY(veiculo_id) REFERENCES veiculo(id))''')

# Define a classe Veiculo
class Veiculo:
    def __init__(self, modelo, ano, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def save(self):
        c.execute('INSERT INTO veiculo (modelo, ano, quilometragem) VALUES (?, ?, ?)',
        (self.modelo, self.ano, self.quilometragem))
        conn.commit()

@staticmethod
def list():
    c.execute('SELECT * FROM veiculo')
    return c.fetchall()

# Define a classe Motorista
class Motorista:
    def __init__(self, nome, cnh, telefone=None):
        self.nome = nome
        self.cnh = cnh
        self.telefone = telefone

    def save(self):
        c.execute('INSERT INTO motorista (nome, cnh, telefone) VALUES(?, ?, ?)',
                  (self.nome, self.cnh, self.telefone))
        conn.commit()

    @staticmethod
    def list():
        c.execute('SELECT * FROM motorista')
        return c.fetchall()
    
# Define a classe Manutencao
class Manutencao:
    def __init__(self, veiculo_id, descricao) -> None:
        self.veiculo_id = veiculo_id
        self.descricao = descricao
        self.data = datetime.no().strftime('%Y-%m-%d')

    def save(self):
        c.execute('INSERT INTO manutencao (veiculo_id, data, descricao) VALUES (?, ?, ?)',
                  (self.veiculo_id, self.data, self.descricao))
        conn.commit()

    @staticmethod
    def list():
        c.execute('SELECT * FROM manutencao')
        return c.fetchall()


conn.close()


          
    
