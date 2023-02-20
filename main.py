#!/bin/python3

from graph_1 import graph_1

# standard form: y(t) = Asin(2πft)
graph = graph_1(
    name='sin(200πt)+0.3cos(400πt)',
    f_sin=100,  # 200 = 2f
    f_cos=200,  # 400 = 2f
    amplitude_sin=1,
    amplitude_cos=0.3,
    cycles=8)
graph.plot()
graph.stem(num_samples=4)  # 1 sample per cycle
graph.stem(num_samples=4*2)  # 2 samples per cycle
graph.stem(num_samples=4*10)  # 10 samples per cycle