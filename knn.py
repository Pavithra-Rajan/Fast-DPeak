from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import timeit

start = timeit.default_timer()


 

df = pd.read_csv('shortened.data',sep=',')

X=df.values[:,[0]+[i for i in range(4,16)]]
Y=df.values[:,[-1]]
Y=np.ravel(Y)


 
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
             X, Y, test_size = 0.2, random_state=42)
 
knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X_train, y_train)
 
# Predict on dataset which model has not seen before
output=knn.predict(X_test)


end = timeit.default_timer()
print(len(output),len(X_train))

print("runtime: ",end-start)