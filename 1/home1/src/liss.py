import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from os.path import join, abspath

def liss(begin, end, path='.'):
    N = 10000
    T = np.linspace(0, 1000, N+1, dtype=np.float32)
    colors = list(matplotlib.colors.get_named_colors_mapping().values())
    i=0
    for a in range(begin,end+1):
        for b in range(begin, end+1):
            X = np.cos(a * T)
            Y = np.sin(b * T)
            #line, = plt.plot(X, Y, color=colors[i])
            plt.plot(X, Y, color=colors[i])
            plt.axis('equal')   #масштаб по осям одинаковый
            plt.axis([-1.1, 1.1, -1.1, 1.1])    #диапазон по осям

            filepath = join(path, f'liss_{a}_{b}.png')
            filepath = abspath(filepath)
            plt.savefig(filepath)
            #line.remove()
            i += 1
            plt.clf()   #очистка
            print(a,b)  #для удобства
