import numpy as np
from sklearn.cluster import KMeans

model = KMeans()
type(model)

df = pd.read_csv('planet.csv')

class KMeans:
    def __init__():
        self.name = 'KMeans'
        #self.type = 'KMeans()'
        self.n_clusters = None

    def num_clusters():
        n_clusters = 