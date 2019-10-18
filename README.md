cities-kmeans app

Author: Phillip Thain
Email: phillip.s.thain@gmail.com
Date: 10/18/2019
References: Purdue CS37300 (Datamining and Machine Learning) Course Material


Description:
    An algorithm that will produce a set of K clusters of cities based
    off of their location.

**************************
**Usage and requirements**
**************************

To use this program:
  Navigate to "cities-kmeans/src" and run 'main.py' with python2.7.

  Usage: 'python main.py [path_to_file] [size of k]'

  Parameters:
      - 'path to file':
          Path to an .xlsx file with atleast two columns titled 'Latitude' and 'Longitude'.

      - 'size of k':
          K is the number of clusters you would like to have.

In order to run, Python2.7 must be installed along with the following Python packages:
  xlrd
  numpy
  pandas

**********************************************
**Brief Description of the K-Means algorithm**
**********************************************

The K-Means algorithm is an unsupervised machine learning technique.
This algorithm groups a set of data up into 'K' clusters.
This is done by matching a city to a centroid using a distance metric. In this implementation, the euclidean distance is used to determine which centroid a city is closest to.

The logical flow of this algorithm is as follows:

While(The centroids do not change) {
  for every city {
    //add city to the closest cluster
  }
  //compute a new centroid at the center of all cities in the cluster
}

In this implementation, this process is repeated several times to find, with high probability, the global minimum of error (i.e. it finds the best centroids after many trials)


*******************************************************************************
**How I would modify the algorithm to consider another feature, like 'Demand'**
*******************************************************************************

Incorporating a new feature, like 'Demand', is fairly straightforward in this algorithm. The current implementation handles two features: Latitude and Longitude. The updated version would handle 'Demand' just like these two established features.

The only core logic needing changed will be the distance function when calculating error. Instead of calculating the euclidean distance for two points on a 2-D plane, it will need to calculate for two points on a 3-D plane. This could be extrapolated for N features and a N-D plane.

Additionally, I would refractor some of the data structures and function's parameters to handle not just two features, but n features.
