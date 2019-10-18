
#Imports
import sys
import math
import pandas as pd
import numpy as np


'''
    Focus of this implementation

    #Initialize centroids; returns a matrix of K centroids
    #Limit the number of Iterations
    #For each iteration
        For every datapoint
            For every centroid
                Distance(datapoint, centroid)
            Classify datapoint to a cluster
        Now, each cluster has a list of datapoints associated with it
        Re-calculate the centroids
        +The WC SSE does the following:
        Within-cluster sum of squared errors
            For every centroid
                For every datapoint
                    add the sq. distance(c, dp) to a sum

'''

'''
    Append a column to dataset associating each tuple with a cluster.
    The column represents the 'id' of the cluster. Default value is -1.
'''
def addCentroidCol(dataset):
    centroid_col = np.full((len(dataset), 1), -1)
    print(np.append(dataset, centroid_col, 1))
    return np.append(dataset, centroid_col, 1)

'''
    Returns a dictionary of clusters, each containing a centroid(x,y)
    Index represents 'c_id', or cluster id.
'''
def initClusters(k):
    #Declare dicitonary of clusters
    clusters = {}
    for c_id in range(0, k):
        clusters[c_id] = []
    return clusters

'''
Description:
    Calculate the euclidean distance from a to b
Parameters:
    a = (int x0, int y0),
    b = (int x1, int y1)
Return:
    int distance
'''
def distance(a, b):
    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]
    return math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

'''
Description:
    Find the closest cluster to this datapoint and return its c_id.
'''
def classifyDatapoint(datapoint, clusters):
    minDist = sys.maxint
    c_id = -1
    for i in range(0, len(clusters)):
        distToCluster = distance(datapoint, clusters[i])
        if (distToCluster < minDist):
            minDist = distToCluster
            c_id = i

    return c_id

'''
Description:
    Calculate the Within-Cluster Sum Squared Error (WC SSE).
    For every cluster, and for every datapoint in that cluster,
    sum the squared distance from the datapoint and the cluster's centroid.
    The sum of every datapoint's squared distance to its
    respective centroid is the SSE for the whole model.
Parameters:
    ndarray dataset
Return:
    int SSE
'''
def calcSSE(dataset, clusters):
    SSE = 0
    for datapoint in dataset:
        c_id = classifyDatapoint(datapoint, clusters)
        datapoint[2] = c_id #Associate this point w/ cluster @ c_id
        datapoint = (datapoint[0], datapoint[1])
        centroid = clusters[c_id]
        sSE += (distance(datapoint, centroid) ** 2)
    return SSE

'''
Description:
    For every cluster K, average the respective x,y coords of all points associated
    with it, and update its centroid.
Parameters:
    ndarray dataset (every tuple has an X and Y coordinates)
    dict clusters = { (int x_1, int y_1), (x_2, y_2), ..., (x_k, y_k)}
Return:
    dict updated_clusters
'''
def updateClusters(dataset, clusters):
    k = len(clusters)
    xSum = [0.0] * k
    ySum = [0.0] * k
    numberOfTuples = [0.0] * k
    for datapoint in dataset:
        if (dataset.shape[1] < 2 or datapoint[2] == -1):
            print("Error in calcClusters: Datapoint not assigned a cluster.")
            return "Exit (-1)"
        c_id = datapoint[2]
        xSum[c_id] += datapoint[0]
        ySum[c_id] += datapoint[1]

    for c_id in range(1, k):
        clusters[c_id] = (
            (xSum[c_id]/numberOfTuples[c_id]),
            (ySum[c_id]/numberOfTuples[c_id])
            )
    return clusters


def k_means(dataset, k):
    
