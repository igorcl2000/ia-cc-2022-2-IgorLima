class Perceptron:
    def __init__(self):
        pass
    def __init__(self, entradas_p, alpha_p, theta_p):
        self.conjunto_treinamento = entradas_p
        self.alpha = alpha_p
        self.theta = theta_p
    def passo_zero(self):
        self.pesos = []
        for i in range(len(self.conjunto_treinamento[0][0])):
            self.pesos.append(0)
    def passo_n(self):
        print("\t\t\t\tAplicação do Perceptron\n")
        print("Entradas\t\t\tSaida\t\tPesos\n")
        epoca = 0
        while (True):
            for ct in self.conjunto_treinamento:
                entrada = list(ct[0])
                saida = ct[1]
                saida_y = 0

                for j in range(len(self.pesos)):
                    saida_y += entrada[j] * self.pesos[j]
                saida_y = self.f_saida(saida_y, self.theta)

                p_old = list(self.pesos)
                if(saida_y != saida):
                    for i in range(len(self.pesos)):
                        self.pesos[i] = self.pesos[i] + entrada[i] * self.alpha * saida
                print('({: d} {: d} {: d} )\t\t\t{: d}\t\t\t({: d} {: d} {: d} )'.format(ct[0][0], ct[0][1], ct[0][2], ct[1],self.pesos[0], self.pesos[1], self.pesos[2]))
            epoca += 1
            print()
            if (p_old == self.pesos and epoca != 1):
                break
        print("Epocas:",epoca)
    def f_saida(self, saida_y, theta):
        if (saida_y > theta):
            return 1
        elif (saida_y > -theta and saida_y < theta):
            return 0
        elif (saida_y < -theta):
            return -1
if __name__ == "__main__":
    #([1, 1, 1], 1) -> ([x1 , x2, b]. saida)
    perceptron = Perceptron([([1, 1, 1], 1),
                ([1, -1, 1], -1),
                ([-1, 1, 1], -1),
                ([-1, -1, 1], -1)], -1, 0)
    perceptron.passo_zero()
    perceptron.passo_n()