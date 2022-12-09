from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd 

for dirname, _, filenames in os.walk('/in'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        