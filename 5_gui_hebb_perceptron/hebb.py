class Hebb:
    
    def __init__(self):
        pass

def __init__(self, values_):
    #.
    self.train = values_
def step_zero(self):
    self.weights = []
    for i in range(len(self.train[0][0])):
        self.weights.append(0)

def step_n(self):
    self.step_zero()
    for ct in self.train:
        put = list(ct[0])
    out = ct[1]
    for i in range(len(self.weights)):
        self.weightsh[i] = self.weights[i] + put[i] * out
    return self.weights