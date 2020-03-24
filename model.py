from keras import models,layers
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
import json


## Simple NN using keras ##
class NN():
    def __init__(self):
        pass

    def build_model(self,X_shape):
        model = models.Sequential()
        # input layer
        model.add(layers.Dense(768, input_shape=(X_shape,), activation='relu'))
        # hidden layer
        model.add(layers.Dense(384, activation='relu'))
        # output layer
        model.add(layers.Dense(1, activation='tanh'))

        model.compile(optimizer='adam',
                        loss='mse',
                        metrics=['accuracy'])
        return model

    def train(self, model, X_train, y_train, X_val, y_val, batch_size):
        print('\n### Starting training on {} chess moves. ###'.format(len(y_train)))
        checkpoint = ModelCheckpoint("C:/Users/David/Documents/Projekte/Davids_Chess/trained_nets/best_model.hdf5", monitor='loss', verbose=1,
            save_best_only=True, mode='auto', period=1)
        model.fit(X_train, y_train,
                  batch_size=batch_size,
                  epochs=10,
                  verbose=1,
                  validation_data=(X_val, y_val),
                  callbacks=[checkpoint])
        # Save the model architecture
        with open('C:/Users/David/Documents/Projekte/Davids_Chess/trained_nets/model_architecture.json', 'w') as f:
            f.write(model.to_json())
        print('### Finished training. ###')

    def predict(self,X_test):
        # Model reconstruction from JSON file
        with open('C:/Users/David/Documents/Projekte/Davids_Chess/trained_nets/model_architecture.json', 'r') as f:
            model = model_from_json(f.read())
        # Load weights into the new model
        model.load_weights('C:/Users/David/Documents/Projekte/Davids_Chess/trained_nets/best_model.hdf5')
        # Check models
        model.summary()
        model.compile(optimizer='adam',
                        loss='mse',
                        metrics=['accuracy'])
        # Evaluate
        score = model.predict(X_test, verbose=0)
        return score
