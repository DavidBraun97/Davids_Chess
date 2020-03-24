from keras import models,layers


## Simple NN using keras ##
class NN():
    def __init__(self,X_shape):
        self.Input_size = X_shape

    def build_model(self):
        model = models.Sequential()
        # input layer
        model.add(layers.Dense(768, input_shape=(self.Input_size,), activation='relu'))
        # hidden layer
        model.add(layers.Dense(384, activation='relu'))
        # output layer
        model.add(layers.Dense(1, activation='tanh'))

        return model
