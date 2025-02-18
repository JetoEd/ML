import tensorflow as tf
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy #Logistic loss
from tensorflow.keras.losses import MeanSquaredError #linear regression loss 
from tensorflow.keras.losses import SparseCategoricalCrossentropy #softmax loss function 
from tensorflow.keras.optimizers import Adam

model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units=15, activation='relu'),
    Dense(units=1, activation='linear'),
])
 
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss= SparseCategoricalCrossentropy(from_logits=True))
model.compile(loss= MeanSquaredError())

# model.fit(X, y, epochs=100)


# print(tf.__version__)











