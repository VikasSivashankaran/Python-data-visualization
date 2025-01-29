import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 50, 5, 10])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels)
plt.show() 
