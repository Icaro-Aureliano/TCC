class Cliente:
    def __init__(self, nome, email, telefone, chave, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.codigo = chave
