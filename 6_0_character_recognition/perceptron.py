# Perceptron Class
# Class to calculate weights using the Perceptron Rule


class Perceptron:
    def __init__(self):
        self.w_bias = 0.0
        self.theta = 0
        self.alpha = 1
        self.num_of_inputs = 0
        self.num_of_epochs = 0

        self.weights = []
        self.net = 0.0
        self.training_set = []

    def update_parameters(self, training_set, w_bias, theta, alpha):

        self.training_set = training_set
        self.w_bias = w_bias
        self.theta = theta
        self.alpha = alpha

        self.num_of_inputs = len(self.training_set[0][0])

        self.init_weights()

    def init_weights(self):
        self.weights = []
        for i in range(self.num_of_inputs):
            self.weights.append(0)

    def calculate_net(self, inputs):
        net = 0.0

        # net = bias + xi * wi
        for i in range(len(inputs)):
            net += inputs[i] * self.weights[i]
        net += self.w_bias

        return net

    def calculate_output(self, net):
        if net > self.theta:
            return 1
        elif net < -self.theta:
            return -1
        else:
            return 0

    def check_stop_condition(self, old_weight, old_w_bias):
        for i in range(len(self.weights)):
            if self.weights[i] != old_weight[i]:
                return False

        if self.w_bias != old_w_bias:
            return False

        return True

    def train(self):
        # Initialize old weights and bias
        old_weights = list(self.weights)
        old_w_bias = self.w_bias

        # Iterate through training set
        for training_tuple in self.training_set:
            inputs = training_tuple[0]
            target = training_tuple[1]

            # Get Output
            output = self.calculate_output(self.calculate_net(inputs))

            # If output != target, update weights
            if output != target:
                for i in range(self.num_of_inputs):
                    self.weights[i] = self.weights[i] + self.alpha * inputs[i] * target
                # Update bias
                self.w_bias = self.w_bias + self.alpha * target

        # Test stopping condition
        if self.check_stop_condition(old_weights, old_w_bias):
            self.num_of_epochs += 1
            return self.weights
        else:
            self.num_of_epochs += 1
            return self.train()

    def print(self):
        print("Inputs\t\tTarget")

        for ts in self.training_set:
            print(ts[0], "\t\t", ts[1])

        print("\nWeights:")
        for w in range(len(self.weights)):
            print("\tw" + str(w) + " = " + str(self.weights[w]))
        print("\twb = " + str(self.w_bias))
        print("epochs: " + str(self.num_of_epochs))


if __name__ == "__main__":
    # AND port inputs: bipolar input and target (-1, 1)
    ts = [([1, 1], 1),
     ([1, -1], -1),
     ([-1, 1], -1),
     ([-1, -1], -1)]

    # ts = [([1, 1], 1),
    #       ([1, 0], -1),
    #       ([0, 1], -1),
    #       ([0, 0], -1)]

    perceptron = Perceptron()
    perceptron.update_parameters(ts, 0, 0, 1)
    perceptron.train()
    perceptron.print()
