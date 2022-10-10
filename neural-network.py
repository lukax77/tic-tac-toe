from matrix import *


# Neural Network Back Propagation
class NeuralNetwork:
    def __init__(self, input_nodes_number, number_of_hidden_layers, hidden_layer_nodes_number, output_nodes_number):
        self.input_nodes_number = input_nodes_number
        self.number_of_hidden_layers = number_of_hidden_layers
        self.hidden_layer_nodes_number = hidden_layer_nodes_number
        self.output_nodes_number = output_nodes_number

        self.input = Matrix(input_nodes_number, 1, 0)
        self.layers = Matrix(hidden_layer_nodes_number, number_of_hidden_layers, 0.0)
        self.output = Matrix(output_nodes_number, 1, 0.0)


def test():
    nn = NeuralNetwork(9, 1, 9, 9)

    nn.input.to_string()


if __name__ == '__main__':
    test()

