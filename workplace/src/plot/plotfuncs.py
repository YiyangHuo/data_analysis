import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


color_index_zh = [
    ['b','伏案工作'],
    ['g','站起'],
    ['r','站立'],
    ['c','行走'],
    ['m','上下楼梯'],
    ['y','边走边与人交谈'],
    ['k','站立与人交谈'],

]
color_index = [
    ['b','sit and work'],
    ['g','stand up'],
    ['r','standing'],
    ['c','walk'],
    ['m','go up or down stairs'],
    ['y','walk and talk'],
    ['k','stand and talk'],

]

def plot_scatter(sequence):
    fig=plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    #fig=plt.figure()
    ax = Axes3D(fig)
    for i in range(0,7):
        points = sequence._sequence[np.where(sequence._sequence[:,3]==i+1)]
        ax.scatter(points[:, 0],points[:, 1] ,points[:, 1], c=color_index[i][0], label=color_index[i][1])
    ax.legend(loc='best')
    ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
    ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
    ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
    plt.show()
