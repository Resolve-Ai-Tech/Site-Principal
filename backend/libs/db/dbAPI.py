import sqlite3 as sql
from ..funcs.systemCripto import encrypt_message, decrypt_message

class GerenData():
    def __init__(self) -> None:
        self.database = "backend/libs/db/database.db"
        self.connection = None
        self.cursor = None
    
    def conectar(self) -> None:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()

    def desconectar(self) -> None:
        self.connection.close()
        
    def criarTabela(self) -> None:
        self.conectar()
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS projetos (
            nome TEXT PRIMARY KEY,
            tipo TEXT NOT NULL,
            versao TEXT NOT NULL,
            descricao TEXT NOT NULL
            );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
            );""")
        
        self.connection.commit()
        
        self.desconectar()
        
    def salvarProjeto(self, nome: str, tipo: str, versao: str, descricao: str) -> None:
        pass
    
    def listarProjetos(self) -> None:
        pass
    
    def getProjeto(self, nome: str) -> None:
        pass
    
    def salvarUsuario(self, nome: str, email: str, senha: str) -> None:
        pass
    
    def listarUsuarios(self) -> None:
        pass
    
    def getUsuario(self, email: str) -> None:
        pass

if __name__ == "__main__":
    pass