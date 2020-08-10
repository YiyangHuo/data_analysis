import csv
import os
import numpy as np
from plot.plotfuncs import plot_scatter
from dtw import *
COLOUMN_SIZE = 4
LABEL_NUM = 7
X_ACC_INDEX = 0
Y_ACC_INDEX = 1
Z_ACC_INDEX = 2
LABEL_INDEX = 3

class SequenceList(object):
    def __init__(self):
        self._sequences = [[]for i in range(LABEL_NUM)]
    
    def addData(self, file_name):
        file_data = np.genfromtxt(file_name,delimiter=",",dtype=None, invalid_raise=False)
        file_data = np.delete(file_data, 0, 1)
        row_size = file_data.shape[0]
        current_label = file_data[0][LABEL_INDEX]
        current_sequences = []
        for index in range(row_size):
            if file_data[index].size == 0 or file_data[index][LABEL_INDEX] == 0:
                continue
            if index == row_size - 1:
                self._sequences[current_label - 1].append(current_sequences)
            elif file_data[index][LABEL_INDEX] == current_label:
                current_sequences.append(file_data[index])
            else:
                self._sequences[current_label - 1].append(current_sequences)
                current_label = file_data[index][LABEL_INDEX]
                current_sequences = []
                current_sequences.append(file_data[index])
    
    def getNearestLabel(self, target_query):
        output = []
        for index in range(len(self._sequences)):
            total_distance = 0
            if len(self._sequences[index]) == 0:
                continue
            for template_sequence in self._sequences[index]:
                template_sequence = np.delete(template_sequence, LABEL_INDEX, 1)
                alignment = dtw(target_query, template_sequence,dist_method='euclidean', keep_internals=True)
                total_distance += alignment.normalizedDistance
                print(total_distance)
            avg_distance = total_distance / len(self._sequences[index])
            output.append(avg_distance)
        print(output)
        return output.index(min(output))
        
sequence1 = SequenceList()
sequence1.addData('../data/test.csv')
targetquery = [
[1502,2215,2153],
[1667,2072,2047],
[1611,1957,1906],
[1601,1939,1831],
[1643,1965,1879],
[1604,1959,1921],
[1640,1829,1940],
[1607,1910,1910],
[1546,2045,1910],
[1529,2049,1972],
]
print(sequence1.getNearestLabel(targetquery))

