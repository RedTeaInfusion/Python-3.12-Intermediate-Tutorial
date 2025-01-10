'''
Lesson 09 - Virtual Environment
venv
activate deactivate
where python
matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

def setup_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title('Function visualizer')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)
    ax.plot(0, 0, 'ro')
    return fig, ax

def plot_function(func):
    def visualize():
        x = np.linspace(-4, 4, 1000)
        y = func(x)
        fig, ax = setup_plot()
        ax.plot(x, y, lw=2, color='blue', label='Function')
        ax.legend()
        plt.show()
    return visualize

@plot_function
def sin_func(x):
    return np.sin(x)

@plot_function
def cos_func(x):
    return np.cos(x)

def main():
    sin_func()
    cos_func()

if __name__ == '__main__':
    main()