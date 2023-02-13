#!/bin/python3

from graph_1 import graph_1

# standard form: y(t) = sin(2πft)
graph = graph_1(
    name='sin(200πt)+0.3cos(400πt)',
    f_sin=100,  # 200 = 2f
    f_cos=200,  # 400 = 2f
    amplitude_sin=1,
    amplitude_cos=0.3,
    cycles=4)
graph.show()
graph.show_samples(num_samples=2)