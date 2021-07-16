import time

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        data = time.ctime()
        print("\n\n O saldo do(a) titular {} é de R${}. \n {} \n Banco Karoliny do Sul \n".format(self.__titular,
        self.__saldo, data))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar): #metodo privado
        return valor_a_sacar <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} informado, excede o seu limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @staticmethod #eh da propria classe, portanto podemos utilizar quando queremos criar algo sem declarar o objeto no metodo construtor mas tem tudo haver com a classe, sendo uma exceção somente da classe.
    #Métodos estáticos tem um cheiro de linguagem procedural já que independe de um objeto para ser chamado e não manipula informações/atributos de objetos. Deve ser usado com bastante cautela!
    def codigo_banco():
        return "001"
    
    def get_saldo(self): #forma de como fzr get 
        return self.__saldo
    
    @property #forma de fzr o get tbm, só que mais limpo no codigo e chamar sem o "()" parenteses, utilizando propriedade
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    def set_limite(self, limite): #forma de fzr o set
        self.__limite = limite
    
    @limite.setter #mesmo proposito do get, agora com o set, utilizando o nome do metodo com a palavra reservada do python "setter", ou seja alterando com propriedade
    def limite(self, limite):
        self.__limite = limite

    