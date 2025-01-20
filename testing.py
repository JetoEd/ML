import tensorflow as tf
from tensorflow.python.keras import Sequential 
from tensorflow.python.keras.layers import Dense
# from tensorflow.python.keras.losses import BinaryCrossentropy #Logistic loss
# from tensorflow.python.keras.losses import MeanSquaredError #linear regression loss 
from tensorflow.python.keras.losses import SparseCategoricalCrossentropy #softmax loss function 
from tensorflow.python.keras.optimizers import Adam 





model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units=15, activation='relu'),
    Dense(units=1, activation='linear'),
])
 
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3), loss= SparseCategoricalCrossentropy(from_logits=True))
#model.compile(loss= MeanSquaredError())

model.fit(X, y, epochs=100)











