class Teste:
    def __init__(self, id, entrada, modelo):
        self.id = id
        self.entrada = entrada
        self.modelo = modelo
        

    def getId(self):
        return self.id

    def getEntrada(self):
        return self.entrada
        
    def getMoedelo(self):
        return self.modelo

    def setId(self, id:str) :
        self.id = id
        

    def setEntrada(self, entrada):
        self.entrada = entrada

    def setModelo(self, modelo):
        self.modelo = modelo