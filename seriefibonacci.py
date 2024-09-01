import matplotlib.pyplot as plt
import numpy as np

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def plot_fibonacci_spiral(n):
    fib_sequence = fibonacci_sequence(n)
    
    plt.figure(figsize=(8, 8))
    x, y = [0], [0]  # Initial position
    
    angle = 0
    for i in range(1, n):
        angle += np.pi/2  # Rotate 90 degrees
        x.append(x[-1] + fib_sequence[i-1] * np.cos(angle))
        y.append(y[-1] + fib_sequence[i-1] * np.sin(angle))
        
        plt.plot([x[-2], x[-1]], [y[-2], y[-1]], color='blue')

    # Plotting the spiral
    for i in range(1, n):
        theta = np.linspace(0, np.pi/2, 100)
        x_arc = fib_sequence[i-1] * np.cos(theta + i*np.pi/2)
        y_arc = fib_sequence[i-1] * np.sin(theta + i*np.pi/2)
        plt.plot(x_arc + x[i-1], y_arc + y[i-1], color='orange')

    plt.title(f'Spiral de Fibonacci con {n} términos')
    plt.axis('equal')
    plt.show()

# Número de términos en la secuencia de Fibonacci
n = 10
plot_fibonacci_spiral(n)

