from disco import Disco

class Config:

    def __init__(self):
        self._numero_discos = int(input("\nInforme a quantidade de discos: "))

    def adiciona_discos(self, torre_inicial):
        discos = self.add_disco()
        for ix in range(self._numero_discos):
            torre_inicial.empilha(discos[ix])

    def add_disco(self):
        discos = []
        arquivo = open('disco.txt', 'r')

        for linha in arquivo:
            discos.append(Disco(int(linha)))

        return discos
    
    def numero_discos(self):
        return self._numero_discos


    def status_torres(self, torres):
        print('\nNumero de discos: ' + str(self._numero_discos))

        for torre in torres:
            torre.to_string()
