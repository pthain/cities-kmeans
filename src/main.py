'''
    Author: Phillip Thain
    Date: 10/17/19
    Email: phillip.s.thain@gmail.com
    Description:
        An algorithm that will produce a set of K clusters of cities based
        off of their location.
'''

#Imports
import sys
import pandas as pd
import numpy as np
import k_means as km


def get_dataset(datasetPath):
    data_frame = pd.read_excel(datasetPath, sheet_name='Sheet1')
    data_frame = data_frame[['Latitude', 'Longitude']]
    #print(data_frame)
    d_set = data_frame.as_matrix()
    return d_set

#Program start
if (len(sys.argv) == 3):
    datasetPath = sys.argv[1]
    k = int(sys.argv[2])
    dataset = get_dataset(datasetPath)
    km.k_means(dataset, k)
    #print(km.distance((0,-5),(-20,10)))

else:
    print("Required input:")
    print("\t<python clustering.py [dataset path] [size of k]>")
