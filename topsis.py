
# Required Libraries
import numpy as np

from pyDecision.algorithm import topsis_method

# TOPSIS

# Weights
weights = np.array([ [16.6, 10.2, 15.2, 6.6, 6.9, 9.1, 11.3, 3.0, 7.5, 5.5, 8.1] ])

# Load Criterion Type: 'max' or 'min'
criterion_type = ['max', 'max', 'max', 'max', 'max', 'max', 'max', 'max', 'max', 'max', 'max']

# Dataset
dataset = np.array([
         #a1  #a2  #a3  #a4  #a5   #a6   #a7   #a8   #a9   #a10  #a11   
        [1,   2,   1,   3,   4,    1,    2,    4,    2,    3,    3],  #a1
        [1/2, 1,   1/3, 2,   2,    1,    1/2,  7,    2,    2,    1],  #a2
        [1,   3,   1,   2,   1,    2,    3,    3,    2,    2,    2],  #a3
        [1/3, 1/2, 1/2, 1,   1,    1,    1/3,  3,    1/2,  2,    1],  #a4
        [1/4, 1/2, 1,   1,   1,    1,    1,    2,    1/2,  1,    1],  #a5
        [1,   1,   1/2, 1,   1,    1,    1,    3,    1,    1,    2],  #a6
        [1/2, 2,   1/3, 3,   1,    1,    1,    4,    3,    3,    1/2],  #a7
        [1/4, 1/7, 1/3, 1/3, 1/2,  1/3,  1/4,  1,    1/2,  1/2,  1/3],  #a8
        [1/2, 1/2, 1/2, 2,   2,    1,    1/3,  2,    1,    1,    1],  #a9
        [1/3, 1/2, 1/2, 1/2, 1,    1,    1/3,  2,    1,    1,    1/2],  #a10
        [1/3, 1,   1/2, 1,   1,    1/2,  2,    3,    1,    2,    1]   #a11
        ])

# Call TOPSIS
relative_closeness = topsis_method(dataset, weights, criterion_type, graph = True)