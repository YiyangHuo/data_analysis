import csv
import os
import numpy as np
from plot.plotfuncs import plot_scatter
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
        print(row_size)
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
        print(self._sequences[0][1]) # use for test
        
sequence1 = SequenceList()
sequence1.addData('../data/test.csv')

