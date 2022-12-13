# Neuron Class
# Class to run a neural network from weights,
# calculated by Perceptron learning rule


class Neuron:
    def __init__(self, weights, w_bias, theta):
        self.w_bias = w_bias
        self.theta = theta
        self.weights = weights

    def calculate_net(self, inputs):
        net = 0.0

        # net = bias + xi * wi
        for i in range(len(inputs)):
            net += inputs[i] * self.weights[i]
        net += self.w_bias

        return net

    def calculate_output(self, inputs):
        net = self.calculate_net(inputs)
        if net > self.theta:
            return 1
        elif net < -self.theta:
            return -1
        else:
            return 0