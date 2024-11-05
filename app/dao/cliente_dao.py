from ..models.modelo import Cliente

SQL_CRIA_CLIENTE = 'INSERT into cliente (nome, email, telefone, chave) values (%s, %s, %s, %s)'
BUSCA_SQL = 'SELECT id, nome, email, telefone, chave from cliente where email = %s and chave = %s'
NOME_SQL = 'SELECT nome from cliente where email = %s'
CHAVE_SQL = 'SELECT * from cliente where chave = %s'

class ClienteDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_CLIENTE, (cliente.nome, cliente.email, cliente.telefone, cliente.codigo))
        self.__db.connection.commit()
        return cliente

    def buscar_registro(self, email, chave):
        cursor = self.__db.connection.cursor()
        cursor.execute(BUSCA_SQL, (email ,chave))
        busca = cursor.fetchone()
        if busca:
            cliente = traduz_cliente(busca)
            return cliente
        else:
            return None

    def buscar_nome(self, email):
        cursor = self.__db.connection.cursor()
        cursor.execute(NOME_SQL, (email,))
        nome_db = cursor.fetchone()
        if nome_db:
            return nome_db[0]
        else:
            return None

    def buscar_chave(self,chave):
        cursor = self.__db.connection.cursor()
        cursor.execute(CHAVE_SQL, (chave,))
        chave_db = cursor.fetchone()
        if chave_db:
            return True
        else:
            return False

def traduz_cliente(cliente):
    print(cliente)
    return Cliente(cliente[1], cliente[2], cliente[3], cliente[4], cliente[0])
