import matplotlib.pyplot as plt
import numpy as np

k=np.array([3,4,5,6,10,20,40])
y1=np.array([17.80,18.08,18.30,18.42,19.76,20.47,22.4])

y2=np.array([3.78,3.89,3.96,4.08,4.367,4.829,5.276])

y3=np.array([10.85,11.25,11.55,11.91,12.42,13.91,15.74])


plt.title("Runtime comparision")
plt.xlabel("K values")
plt.ylabel("Runtime")

plt.plot(k, y1,'r-',marker='^',label='Normal KNN n=3000')
plt.plot(k, y2,'b-',marker='*',label='Fast Dpeak n=3000')
plt.plot(k, y3,'g-',marker='s',label='Fast Dpeak n=6000')
plt.legend( loc=5, bbox_to_anchor=(1.0,0.3))
plt.show()