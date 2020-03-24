import chess
import numpy as np
from utility.NN_utils import *
from model import *

## import
#pullandstore(500)

X,y = load_training_data()
n = len(y)
X_test =  X[-10:,:]
y_test = y[-10:]

# board = chess.Board()
# print(board)
# X_test = preprocess_board(board)
print(X_test)
print(np.shape(X_test))
model = NN()
score = model.predict(X_test)
print("Score: {} .".format(score))
print(y_test)

score = model.predict(X_test[0:1,:])
print("Score: {} .".format(score))
print(y_test[0])
