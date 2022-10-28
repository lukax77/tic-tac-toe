import math
from matrix import *

WIN_VALUE = 1.0
DRAW_VALUE = 1.0
LOSS_VALUE = 0.0

# Neural Network Back Propagation
class NeuralNetwork:
    def __init__(self, input_nodes_number, number_of_hidden_layers, hidden_layer_nodes_number, output_nodes_number):
        self.input_nodes_number = input_nodes_number
        self.number_of_hidden_layers = number_of_hidden_layers
        self.hidden_layer_nodes_number = hidden_layer_nodes_number
        self.output_nodes_number = output_nodes_number

        self.input = Matrix(input_nodes_number, 1, 0)
        self.output = Matrix(output_nodes_number, 1, 0.0)
        self.weights = []
        self.layers = []
        self.bias = []

        # Input weight matrix
        iwm = Matrix(hidden_layer_nodes_number, input_nodes_number, 0.0)
        self.weights.append(iwm)

        # First layer matrix
        flm = Matrix(hidden_layer_nodes_number, 1, 0.0)
        self.layers.append(flm)
        # First layer bias matrix
        flbm = Matrix(hidden_layer_nodes_number, 1, 0.5)
        self.bias.append(flbm)

        for i in range(1, number_of_hidden_layers):
            # N layer weight matrix
            self.weights.append(Matrix(hidden_layer_nodes_number, hidden_layer_nodes_number, 0.0))
            # N layer matrix
            self.layers.append(Matrix(hidden_layer_nodes_number, 1, 0.0))
            # N layer bias matrix
            self.bias.append(Matrix(hidden_layer_nodes_number, 1, 0.5))

        # Output weight matrix
        owm = Matrix(output_nodes_number, hidden_layer_nodes_number, 0.0)
        self.weights.append(owm)
        # Output bias matrix
        obm = Matrix(output_nodes_number, 1, 0.5)
        self.bias.append(obm)


    def forward_propagation(self):
        first_propagation = self.weights[0].product(self.input)
        first_propagation.addition(self.bias[0])
        first_propagation.apply_function(sigmoid)

        current_propagation = first_propagation
        for i in range(1, self.number_of_hidden_layers):
            n_propagation = self.weights[i].product(current_propagation)
            n_propagation.addition(self.bias[i])
            n_propagation.apply_function(sigmoid)
            current_propagation = n_propagation

        last_propagation = self.weights[-1].product(current_propagation)
        last_propagation.addition(self.bias[-1])
        last_propagation.apply_function(sigmoid)
        self.output = last_propagation

    # TODO: Compute back_propagation

    def loss_function(self):
        return WIN_VALUE - self.output.find_max_value()


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def test():
    # For the input into our network, we will flatten out the board position into an array of 9 values:
    # 1 represents an X, -1 represents an O, and 0 is an empty cell. The output layer will be an
    # array of 9 values representing the Q-value for each possible move: Something close to 0
    # represents a loss and a value close to 1 represents a win or a draw. After training, the
    # network will choose the move corresponding to the highest output value from this model.
    nn = NeuralNetwork(9, 2, 36, 9)

    # nn.input.to_string()

    nn.forward_propagation()

    nn.output.to_string()

    max = nn.output.find_max_value()

    print(f'Best play = {max}')


if __name__ == '__main__':
    test()
