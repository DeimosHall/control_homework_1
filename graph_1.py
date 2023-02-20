import matplotlib.pyplot as plt
import numpy as np


class graph_1:
    def __init__(
            self,
            name,
            f_sin: int,
            f_cos: int,
            amplitude_sin: int,
            amplitude_cos: int,
            cycles: int) -> None:
        self._name = name
        self._f_sin = f_sin
        self._f_cos = f_cos
        self._amplitude_sin = amplitude_sin
        self._amplitude_cos = amplitude_cos
        self._cycles = cycles

    def _create(self, num_samples: int = 1000):
        # Define the start and end of the graph
        T = 1 / self._f_sin
        graph_start = 0
        graph_end = self._cycles * T
        print(T)
        print(graph_end)
        t = np.linspace(graph_start, graph_end, num=num_samples)

        # Calculate the signal
        sin = self._amplitude_sin * np.sin(2 * np.pi * self._f_sin * t)
        cos = self._amplitude_cos * np.cos(2 * np.pi * self._f_cos * t)
        signal = sin + cos

        return (t, signal)
    
    def plot_labels(self):
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title(f'Signal: {self._name}')
        plt.grid()
        plt.show()

    def plot(self):
        t, y = self._create()
        plt.plot(t, y)
        self.plot_labels()

    def stem(self, num_samples: int):
        t, y = self._create(num_samples=num_samples)
        plt.stem(t, y, use_line_collection=True)
        self.plot_labels()
