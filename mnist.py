# dependencies ------------------>
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# program variables ------------------>
# load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# normalize datasets
x_train, x_test = x_train/255, x_test/255

# program execution ------------------>
# model definition
model = tf.keras.models.Sequential()
# hidden layers
# flatten layer turns the image matrix into a 1 dimensional list
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(10, activation='relu'))
model.add(tf.keras.layers.Dense(15, activation='relu'))
model.add(tf.keras.layers.Dense(8, activation='relu'))
# output layer
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# model compilation
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), loss=tf.keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])

# model training
# training history will contain the loss results of the training and the validation phases on each epoch
training_history = model.fit(x_train, y_train, epochs=15, validation_data=(x_train, y_train))

# evaluate model
model.evaluate(x_test, y_test)

# plot training history
plt.plot(training_history.history['loss'])
plt.plot(training_history.history['val_loss'])
plt.title('Training Progress')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

# test with random test dataset elements
result = model.predict(x_test)
n = 0
while n >= 0:
    n = int(input('Index> '))
    print((f"Expected Result: {y_test[n]} => Model Prediction: {np.argmax(result[n])}"))
    plt.imshow(x_test[n], cmap='binary_r')
    plt.show()
