
# coding: utf-8

import numpy as np
# import TSAEDistance as TSAE
from scipy.spatial.distance import cdist


def evaluate_centroids(data, clusters):
    k = np.max(clusters) + 1
    centroids = np.empty(shape=(k,) + data.shape[1:])
    for i in range(k):
        np.mean(data[clusters == i], axis=0, out=centroids[i])
    return centroids    


def kmedian(data, k, steps=10):
    
    # randomly pick k data points as centroids
    centroids = data[np.random.choice(np.arange(len(data)), k, False)]
    
    for _ in range(max(steps, 1)):
        # Squared distances between each point and each centroid.
        # sqdists = scipy.spatial.distance.cdist(centroids, data, 'sqeuclidean')
        # print sqdists, 'sqdists'

        # Manhattan distance
        mandist = cdist(centroids, data, 'cityblock')

        # Index of the closest centroid to each data point.
        clusters = np.argmin(mandist, axis=0)
        # print clusters, 'clusters'

        new_centroids = evaluate_centroids(data, clusters)
        # print new_centroids, 'new_centroids'
        
        if np.array_equal(new_centroids, centroids): break
        
        centroids = new_centroids
        
    return centroids, clusters


