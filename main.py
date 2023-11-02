import numpy as np
import pandas as pd
import simpsom as sps
from sklearn.cluster import KMeans

veri = pd.read_csv("Mall_Customers.csv")

X = veri.drop(["CustomerID", "Genre"], axis=1)

net = sps.SOMNet(20, 20, X.values, PBC= True)

net.train(start_learning_rate=0.001, epochs=10000)

harita = np.array((net.project(X.values)))
k_ort = KMeans(n_clusters=3, max_iter= 300, random_state=0)
y_ort = k_ort.fit_predict(harita)
veri["kümeler"] = k_ort.labels_

print(veri[veri["kümeler"]==0].drop(["CustomerID","Genre","Age"], axis=1).head(10))
print(veri[veri["kümeler"]==1].drop(["CustomerID","Genre","Age"], axis=1).head(10))
print(veri[veri["kümeler"]==2].drop(["CustomerID","Genre","Age"], axis=1).head(10))
