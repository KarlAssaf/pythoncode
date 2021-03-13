import tensorflow as tf
import numpy as np
import cv2
data = np.load("traindata.npy" , allow_pickle=True)
while (len(data)%32 != 0):
     data = np.delete(data , 1 , 0)
print(len(data))
nnetwork = tf.keras.Sequential([
tf.keras.layers.Conv2D(3 , kernel_size={3, 2}, strides=(1, 1), input_shape=(50 , 50, 1), activation=tf.nn.softmax, batch_size=32, data_format='channels_last'),
tf.keras.layers.MaxPooling2D(pool_size=(2 , 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(2 , activation=tf.nn.softmax)])
input = []
output = []
for i in data:
    input.append(i[0])
    output.append(i[1])
input = np.reshape(np.array(input) , (len(data), 50, 50, 1))
output = np.reshape(np.array(output) , (len(data) , 2))
print(input.shape)
print(output.shape)
nnetwork.compile(loss="binary_crossentropy" , optimizer="adam" , metrics=["accuracy"])
print(len(data)%32)
nnetwork.fit(input , output , epochs=5 , batch_size=32)
nnetwork.save("cock")
test = np.load("testdata.npy" , allow_pickle=True)
test = np.reshape(test, (32, 50, 50, 1))
for i in nnetwork.predict(test):
 if i[0] > i[1]:
  print("kid: ")
 else:
  print("adult: ")
