class ContaBancaria:

    def __init(self):
        self.__numero_conta = 0
        self.__saldo = 0.0
        self.__titular = ""

    def get_numero_conta(self):
        return self.__numero_conta

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def set_numero_conta(self, numero_conta):
        self.__numero_conta = numero_conta

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_titular(self, titular):
        self.__titular = titular

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        if self.get_saldo() >= valor:
            self.__saldo -= valor

class ContaCorrente(ContaBancaria):

    def __init__(self):
        ContaBancaria.__init__(self)
        self.__taxa_manutencao = 0.0

    def get_taxa_manutencao(self):
        return self.__taxa_manutencao

    def set_taxa_manutencao(self, taxa_manutencao):
        self.__taxa_manutencao = taxa_manutencao

    def depositar(self, valor):
         self.set_saldo(self.get_saldo() + valor - self.__taxa_manutencao)

class ContaPoupanca(ContaCorrente):

    def __init__(self):
        ContaCorrente.__init__(self)
