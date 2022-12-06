class Neuron:
    def __init__(self):
        pass

    def p_saida(self, inputs, theta):
        net = 0.0
        for j in range(len(self.weights)):
            net += inputs[j] * self.weights[j]
        # net += self.w_bias

        if (net > theta):
            return 1
        elif (net > -theta and net < theta):
            return 0
        elif (net < -theta):
            return -1

        #.