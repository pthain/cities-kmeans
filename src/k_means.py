
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
        Within-cluster sum of squared errors
            For every centroid
                For every datapoint
                    add the sq. distance(c, dp) to a sum

'''

class k_means:
    def __init__(self, k=3, max_iterations=500):
        self.k = k
        self.max_iterations = max_iterations

'''
Description: Calculate the euclidean distance from a to b
Parameters:
    a = (int x0, int y0),
    b = (int x1, int y1)

Return: int distance
'''
def distance(a, b):
    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]
    return math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

'''
Description:
    Given a set of datapoints, determine their centroid by
    calculating the mean of all the datapoints.
    i.e. sum all Xs, sum all Ys, divide by num of datapoints
Parameters:
    ndarray dataset (every tuple has an X and Y coordinates)

Return:
    centroid = (int x, int y)
'''
def getCentroid(dataset):
    xSum = 0.0
    ySum = 0.0
    numberOfTuples = dataset.shape[0]
    for i, datapoint in enumerate(dataset):
        xSum += dataset[i][0]
        ySum += dataset[i][1]
    return ((xSum/numberOfTuples), (ySum/numberOfTuples))
