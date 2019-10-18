cities-kmeans app

Author: Phillip Thain
Email: phillip.s.thain@gmail.com
Date: 10/18/2019

Description:
    An algorithm that will produce a set of K clusters of cities based
    off of their location.

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
