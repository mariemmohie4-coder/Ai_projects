import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-10,10)

sigmoid = 1/(1 + np.exp(-x) )

plt.plot(x , sigmoid , color="red")
plt.title("Sigmoid function curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.style.use("ggplot")
plt.show()