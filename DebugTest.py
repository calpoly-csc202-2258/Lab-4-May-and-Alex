import matplotlib.pyplot as plt
import numpy as np
import math
x = np.array( [int(i) for i in range( 1, 100 )] )
y = np.array( [math.log2( i ) + 5.0 for i in x] )
plt.plot(x,y, label ="treetime(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph")
plt.grid(True)
plt.legend()
plt.show()