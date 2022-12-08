class Usuario:
    def __init__(self, nome, senha, email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def getNome(self):
        return self.nome

    def getSenha(self):
        return self.senha

    def getEmail(self):
        return self.email

    def setNome(self, nome: str):
        self.nome = nome

    def setSenha(self, senha: str):
        self.senha = senha

    def setEmail(self, email):
        self.email = email
