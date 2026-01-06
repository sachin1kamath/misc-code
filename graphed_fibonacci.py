import math
import matplotlib.pyplot as plt

pi = 3.141
phi = 1.618

def fibonacci():
    sequence = [1, 1]
    i = 1

    for i in range(100):
        sequence.append(sequence[i] + sequence[i - 1])

    return sequence

def list_x(sequence):
    x_values = []
    
    for i in range(len(sequence)):
        x_values.append(sequence[i] * math.cos((2 * pi * i) / phi))
    
    return x_values

def list_y(sequence):
    y_values = []
    
    for i in range(len(sequence)):
        y_values.append(sequence[i] * math.sin((2 * pi * i) / phi))
    
    return y_values

plt.plot(list_x(fibonacci()), list_y(fibonacci()))
plt.show()