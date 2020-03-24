import keras.models
from keras.callbacks import ModelCheckpoint

from model import *
from utility.NN_utils import *

## import data
X,y = load_training_data()
print(np.shape(X),np.shape(y))
n = len(y)
X_train = X[:,0:n-100]
y_train = y[:n-100]
X_val =  X[:,-100:]
y_val = y[-100:]
shape_X = np.shape(X_train)[0]
shape_y = np.shape(y_train)
model = NN(shape_X)
chess_model = model.build_model()

chess_model.compile(optimizer='adam',
                loss='mse',
                metrics=['accuracy'])
checkpoint = ModelCheckpoint("C:/Users/David/Documents/Projekte/Davids_Chess/trained_nets/best_model.hdf5", monitor='loss', verbose=1,
    save_best_only=True, mode='auto', period=1)
chess_model.fit(X_train.T, y_train,
          batch_size=128,
          epochs=10,
          verbose=1,
          validation_data=(X_val.T, y_val),
          callbacks=[checkpoint])
