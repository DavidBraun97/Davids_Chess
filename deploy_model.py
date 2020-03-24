from model import *
from utility.NN_utils import *

'''RUN this script "deploy_model.py" to train!
   After training, the model architecture and the weights are saved!'''

## Loading training data ##
X,y = load_training_data()
print(np.shape(X),np.shape(y))
n = len(y)
## split into train&validation sets ##
# X_train = X[:,0:n-100]
# y_train = y[:n-100]
X_train = X[0:n-100,:]
y_train = y[:n-100]
print(np.shape(X_train),np.shape(y_train))
# X_val =  X[:,-100:]
# y_val = y[-100:]
X_val =  X[-100:,:]
y_val = y[-100:]
print(np.shape(X_val),np.shape(y_val))
shape_X = np.shape(X_train)[1]
shape_y = np.shape(y_train)

## Initialize model and start training ##
model = NN()
chess_model = model.build_model(shape_X)
model.train(chess_model, X_train, y_train, X_val, y_val, 128)
