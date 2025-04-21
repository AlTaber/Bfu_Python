import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, -1]
unique_species, counts = np.unique(species_column, return_counts=True)

for species, count in zip(unique_species, counts):
    print(f"{species.decode('utf-8')}: {count}")