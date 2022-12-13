# Neural Net Class
# A class to create a net of Neurons

from perceptron import Perceptron
from neuron import Neuron


class NeuralNet:
    def __init__(self, num_of_neurons, training_set):
        self.num_of_neurons = num_of_neurons
        self.training_set = training_set
        self.neuron_list = []

    def run(self, inputs):
        recognized_characters = []
        for n in self.neuron_list:
            if n.calculate_output(inputs) == 1:
                recognized_characters.append(self.neuron_list.index(n))

        return recognized_characters

    def train_net(self):
        perceptron = Perceptron()
        for i in range(self.num_of_neurons):
            perceptron.update_parameters(self.training_set[i],
                                         0,  # w_bias
                                         0,  # theta
                                         1)  # alpha

            weights = perceptron.train()
            self.neuron_list.append(Neuron(weights, perceptron.w_bias, 0))