import os
import tensorflow as tf
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense
# from tensorflow.python.keras.losses import BinaryCrossentropy #Logistic loss
# from tensorflow.python.keras.losses import MeanSquaredError #linear regression loss 
from tensorflow.keras.losses import SparseCategoricalCrossentropy #softmax loss function 
from tensorflow.keras.optimizers import Adam

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units=15, activation='relu'),
    Dense(units=1, activation='linear'),
])
 
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss= SparseCategoricalCrossentropy(from_logits=True))
#model.compile(loss= MeanSquaredError())

model.fit(X, y, epochs=100)












