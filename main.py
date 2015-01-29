# -*- coding: utf-8 -*-
"""
Example: 3d scatter plot of data stored in a CSV file.

It uses matplotlib and mplot3d
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

#Read the data from a csv file
thedata = np.genfromtxt(
                        #file name
                        'scatterdata.csv',\
                        #column delimiter
                        delimiter='\t',\
                        #data type, if None its atuomatically determined
                        dtype='int',
                        #only use columns 1,3,4 and 6
                        usecols = (0,1,2),\
                        #Label the columns
                        names=['a','b','c'])

#Set the axes labels
ax.set_xlabel('column a')
ax.set_ylabel('column b')
ax.set_zlabel('column c')

#Set the axes limites
ax.set_xlim(-6, 56)
ax.set_ylim(-6, 66)
ax.set_zlim(-6, 76)

#Control the elevation and angle of the "camera"
ax.view_init(elev=12,azim=40)
#Set the distance of the "camera" from the plot, default value: 10
ax.dist=12
                        
#the data from columns a, b and c is ploted.
ax.scatter(thedata['a'], thedata['b'], thedata['c'],color='purple',\
            marker='o', s=30)

#plt.show()
plt.savefig('scatterplot3d.png')