import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
(X_train,y_train),(X_test,y_test)=keras.datasets.mnist.load_data()
print(X_train.shape)