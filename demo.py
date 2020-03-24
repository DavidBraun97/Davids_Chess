import chess
import chess.pgn
import numpy as np
import random
import time
from utility.NN_utils import *
from model import *

## import
#pullandstore(500)

X,y = load_training_data()
print(np.shape(X),np.shape(y))
n = len(y)
X_train = X[:,0:n-100]
y_train = y[:n-100]
X_val =  X[:,-1:]
y_val = y[-1:]
print(np.shape(X_val),np.shape(y_val))
print(X_val)
print(y_val)

model = NN()

score = model.predict(X_val.T)
print("Score: {} .".format(score))
