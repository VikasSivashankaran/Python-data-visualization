import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 6, 1, 9])

plt.barh(x, y, color = "pink")
plt.xticks(np.arange(0, 10, 1))  # Set x-ticks to show every number from 0 to 9
plt.show()
