import abc


class TesteInterface(abc.ABC):
    @abc.abstractmethod
    def perfilarModelo(sefl, modelo):
        pass

    def calcularMetricas(self, entrada, modelo):
        pass

    def treinarDl(self, entrada, modelo):
        pass

    def gerarRelatorio(self, entrada, modelo):
        pass
