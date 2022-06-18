class Cliente:
    def __init__(self, nome, email, telefone, chave, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.codigo = chave

    # def __str__(self):
    #     return f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nChave: {self.chave}Data: {self.data}"
