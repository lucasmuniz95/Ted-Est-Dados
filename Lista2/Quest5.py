import numpy as np

class FilaAeroporto:
    def __init__(self, qtde_aeroporto):
        self.qtde_aeroporto = qtde_aeroporto
        self.numero_avioes = 0
        self.avioes = np.empty(self.qtde_aeroporto, dtype = int)
        self.ultima_posicao = self.qtde_aeroporto - 1

    def fila_vazia(self):
        return self.numero_avioes == 0

    def fila_cheia(self):
        return self.numero_avioes == self.qtde_aeroporto
      
    # Adicionar um avião à fila de espera 
    def enfileirarAvioes(self, aviao):
        if self.fila_cheia():
            print('A fila está cheia')
            return
        
        if self.numero_avioes == 0:
            self.avioes[self.numero_avioes] = aviao
            self.numero_avioes += 1
        else:
            x = self.numero_avioes - 1
            while x >= 0:
                if aviao > self.avioes[x]:
                    self.avioes[x + 1] = self.avioes[x]
                else:
                    break      
                x -= 1 

            self.avioes[x + 1] = aviao
            self.numero_avioes += 1

    # Autorizar a decolagem do primeiro avião da fila;
    def desenfileirarAvioes(self):
        if self.fila_vazia():
            print('A fila está vazia')
            return
        
        aviao = self.avioes[self.numero_avioes - 1]
        self.numero_avioes -= 1
        return aviao
            

    # Listar as características do primeiro avião da fila.
    def primeiroAviao(self):
        if self.fila_vazia():
            return -1
        else:
            return self.avioes[self.numero_avioes - 1]

    # Listar todos os aviões na fila de espera;
    def imprime(self):
        if self.fila_vazia() == 0:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i},  - {self.avioes[i]}' )     
