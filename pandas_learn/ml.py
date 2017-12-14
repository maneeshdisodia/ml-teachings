import numpy as np
import matplotlib.pyplot  as plt

x = np.linspace(0, 5, 11)

print(x)
y = x ** x
plt.plot(x,y)
plt.show()
