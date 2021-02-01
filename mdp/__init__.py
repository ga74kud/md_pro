import numpy as np


'''
    get adjacency
'''
def get_adjacency(A, S):
    am_nodes = len(S)
    new_A = np.eye(am_nodes, dtype=bool)
    for wlt in A:
        new_A[int(wlt[1])][int(wlt[0])] = True
    return new_A