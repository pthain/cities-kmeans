
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
    int[] a = (int x0, int y0),
    int[] b = (int x1, int y1)

Return: int distance
'''
def distance(a, b):
    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]
    return math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

'''

'''
