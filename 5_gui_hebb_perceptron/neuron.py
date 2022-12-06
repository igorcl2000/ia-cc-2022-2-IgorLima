class Neuron:
    def __init__(self):
        pass
    def p_output(self, l_values, teta):
        output = 0.0
        for j in range(len(self.l_values)):
            output += l_values[j] * self.l_values[j]
        if (output > teta):
            return 1
        elif (output > -teta and output < teta):
            return 0
        elif (output < -teta):
            return -1
    def h_output(self, l_values):
        output = 0.0
        for j in range(len(self.l_values)):
            output += l_values[j] * self.l_values[j]
        if (output > 0):
            return 1
        elif (output < 0):
            return -1
