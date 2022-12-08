import abc


class UsuarioInterface(abc.ABC):
    @abc.abstractmethod
    def login(self, nome: str, senha: str, email: str):
        pass

    def carregarDados(self, entrada):
        pass

    def carregarModelo(self, modelo):
        pass

    def testarDl(self, entrada, modelo):
        pass
