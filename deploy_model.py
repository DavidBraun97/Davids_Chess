from model import *
from utility.NN_utils import *

'''RUN this script "deploy_model.py" to train!
   After training, the model architecture and the weights are saved!'''

## Loading training data ##
X,y = load_training_data()
print(np.shape(X),np.shape(y))
n = len(y)
## split into train&validation sets ##
X_train = X[:,0:n-100]
y_train = y[:n-100]
X_val =  X[:,-100:]
y_val = y[-100:]
shape_X = np.shape(X_train)[0]
shape_y = np.shape(y_train)

## Initialize model and start training ##
model = NN(shape_X)
chess_model = model.build_model()
model.train(chess_model, X_train.T, y_train, X_val.T, y_val, 128)
