class Hebb:
    def __init__(self):
        pass
    def __init__(self, entradas_p):
        self.conjunto_treinamento = entradas_p
    def passo_zero(self):
        self.pesos = []
        for i in range(len(self.conjunto_treinamento[0][0])):
            self.pesos.append(0)
    def passo_n(self):
        print("\t\t\t\tAplicação da Regra de Hebb\n")
        print("Entradas\t\t\tSaida\t\tPesos\n")
        for ct in self.conjunto_treinamento:
            entrada = list(ct[0])
            saida = ct[1]
            for i in range(len(self.pesos)):
                self.pesos[i] = self.pesos[i] + entrada[i] * saida
            print('({: d} {: d} {: d} )\t\t\t{: d}\t\t\t({: d} {: d} {: d} )'.format(ct[0][0],ct[0][1],ct[0][2],ct[1],self.pesos[0],self.pesos[1],self.pesos[2]))
if __name__ == "__main__":
    # ([1, 1, 1], 1) -> ([x1 , x2, b]. saida)
    hebb = Hebb([([1, 1, 1], 1),
                ([1, -1, 1], -1),
                ([-1, 1, 1], -1),
                ([-1, -1, 1], -1)])
    hebb.passo_zero()
    hebb.passo_n()