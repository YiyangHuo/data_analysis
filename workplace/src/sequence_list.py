import numpy as np
from dtw import dtw
COLOUMN_SIZE = 4
LABEL_NUM = 7
X_ACC_INDEX = 0
Y_ACC_INDEX = 1
Z_ACC_INDEX = 2
LABEL_INDEX = 3


class SequenceList():
    def __init__(self):
        self._sequences = {}
        labels = range(1, LABEL_NUM + 1)
        for key in labels:
            self._sequences[key] = []

    def addData(self, file_name):
        file_data = np.genfromtxt(
            file_name,
            delimiter=",",
            dtype=None,
            invalid_raise=False)
        file_data = np.delete(file_data, 0, 1)
        current_label = file_data[0][LABEL_INDEX]
        current_sequences = []
        for row in file_data:
            if row.size == 0 or \
                    row[LABEL_INDEX] == 0:
                continue
            elif row[LABEL_INDEX] == current_label:
                current_sequences.append(row)
            else:
                self._sequences[current_label].append(current_sequences)
                current_label = row[LABEL_INDEX]
                current_sequences = [row]
        self._sequences[current_label].append(current_sequences)

    def getNearestLabel(self, target_query):
        output = []
        for label in self._sequences:
            total_distance = 0
            if len(self._sequences[label]) == 0:
                continue
            for template_sequence in self._sequences[label]:
                template_sequence = np.delete(
                    template_sequence,
                    LABEL_INDEX, 1)
                alignment = dtw(
                    target_query,
                    template_sequence,
                    dist_method='euclidean',
                    keep_internals=True)
                total_distance += alignment.normalizedDistance
            avg_distance = total_distance / len(self._sequences[label])
            output.append(avg_distance)
        return output.index(min(output))
