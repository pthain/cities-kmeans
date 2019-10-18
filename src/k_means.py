
#Imports
import sys
import math
import pandas as pd
import numpy as np
import random as rand

TRIALS = 100
MAX_ITERS = 100
TOLERANCE = 0.001

### DATA FUNCTIONS ###

'''
    Append a column to dataset associating each tuple with a cluster.
    The column represents the 'id' of the cluster. Default value is -1.
'''
def addCentroidCol(dataset):
    centroid_col = np.full((len(dataset), 1), -1)
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

### CORE K-MEANS ##

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

#Todo: def classifyData, write doc
'''
Description:
    Wrapper function that returns an updated dataset where
    each tuple is classified to a centroid.
'''
def classifyData(dataset, clusters):
    for datapoint in dataset:
        datapoint[2] = classifyDatapoint((datapoint[0], datapoint[1]), clusters)
    return dataset

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
    (ndarray, int SSE)
'''
def calcSSE(dataset, clusters):
    SSE = 0
    for datapoint in dataset:
        c_id = datapoint[2]
        datapoint = (datapoint[0], datapoint[1])
        centroid = clusters[c_id]
        SSE += (distance(datapoint, centroid) ** 2)
    return SSE

'''
Description:
    For every cluster K, calculate the average x,y coords of all
    points associated with it, and update its centroid.
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
        c_id = int(datapoint[2])
        xSum[c_id] += datapoint[0]
        ySum[c_id] += datapoint[1]
        numberOfTuples[c_id] += 1

    for c_id in range(0, k):
        if(numberOfTuples[c_id] != 0):
            clusters[c_id] = (
                (xSum[c_id]/numberOfTuples[c_id]),
                (ySum[c_id]/numberOfTuples[c_id])
                )
    return clusters

'''
Description:
    Generate a cluster centroid from a random datapoint in the dataset for
    kth cluster.
Parameters:
    ndarray dataset (every tuple has an X and Y coordinates)
    int k   - Number of clusters
Return:
    clusters
'''
def getRandomCentroids(dataset, clusters):
    for c_id in range(0, len(clusters)):
        randomCoefficient = rand.randrange(len(dataset))
        tmp_cluster = (
                dataset[randomCoefficient][0],
                dataset[randomCoefficient][1]
            )
        clusters[c_id] = tmp_cluster

    return clusters


'''
Description:
    Implementation of the K-means algorithm to find the centroids of several
    cities by geographical location.
Parameters:
    ndarray dataset (every tuple has an X and Y coordinates)
    int k   - Number of clusters
Return:
    clusters
'''

def k_means(dataset, k):
    #Prepare data
    dataset = addCentroidCol(dataset)
    clusters = initClusters(k)
    clusters = getRandomCentroids(dataset, clusters);
    #print('line 159: Initial clusters', clusters)

    #todo perform learning several times, average results
    #Perform learning
    lowestSSE = sys.maxint
    bestFitClusters = clusters
    for t in range(0, TRIALS):
        clusters = getRandomCentroids(dataset, clusters);
        prevSSE = 0
        for i in range(0, MAX_ITERS):
            dataset = classifyData(dataset, clusters)   #Update data assignment
            currentSSE = calcSSE(dataset, clusters)
            #Calculate Error
            if ((currentSSE >= (prevSSE - TOLERANCE)) and
                (currentSSE <= (prevSSE + TOLERANCE))):
                #No significant change in error
                break
            prevSSE = currentSSE
            clusters = updateClusters(dataset, clusters) #Update centroids

        #Save the set of clusters with the lowest SSE
        if(prevSSE < lowestSSE):
            lowestSSE = prevSSE
            bestFitClusters = clusters

    print("result:", lowestSSE)
    return clusters #Max_iterations reached

'''
Description:
    Display results to console.
'''
def print_clusters(clusters):
    c_str = ""
    for i in range(0, len(clusters)):
        lat = clusters.get(i)[0]
        long = clusters.get(i)[1]
        cityNum = (i + 1)
        c_str += ("\tCity #"+ str(cityNum) +" | ( " + str(lat) + ", " + str(long) + " )\n")

    print("\nK Centroids for this dataset:")
    print("\tCity #  | (Latitude, \tLongitude )")
    print (c_str)
