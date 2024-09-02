import matplotlib
import numpy as np
import matplotlib.pyplot as plt

N = 10000
T = np.linspace(0, 1000, N+1, dtype=np.float32)
colors = list(matplotlib.colors.get_named_colors_mapping().values())
i=0
for a in range(1,10):
    for b in range(1, 10):
        X = np.cos(a * T)
        Y = np.sin(b * T)
        color = a*b
        line, = plt.plot(X, Y, color=colors[i])
        plt.savefig(f'liss_{a}_{b}.png')
        line.remove()
        i += 1
