
import math
import time
import matplotlib.pyplot as plt

pi = 3.141
phi = 1.618

def fibonacci():
    sequence = []
    
    for i in range(20):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])

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

def animated_plot(x_list, y_list):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    
    for i in range(len(x_list)):
        ax.clear()
        ax.plot(x_list[:i+1], y_list[:i+1], 'b-o')
        plt.draw()
        plt.pause(0.1)
    
    plt.ioff()  # Turn off interactive mode
    plt.show()

animated_plot(list_x(fibonacci()), list_y(fibonacci()))