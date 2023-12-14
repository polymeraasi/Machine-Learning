"""
To do: Neural classifier for CIFAR-10.
"""
import numpy as np
import pickle
import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense


def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding="latin1")
    return dict


train_b_1 = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/data_batch_1')
train_b_2 = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/data_batch_2')
train_b_3 = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/data_batch_3')
train_b_4 = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/data_batch_4')
train_b_5 = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/data_batch_5')
test_batch = unpickle(
    '/Users/pinja/pythonProject1/cifar-10-python (3)/cifar-10-batches-py/test_batch')

num_of_classes = 10

trainX = np.concatenate(
    [train_b_1['data'], train_b_2['data'], train_b_3['data'],
     train_b_4['data'], train_b_5['data']])
trainX = trainX.astype('float32')
trainX /= 255

trainY = np.concatenate([np_utils.to_categorical(labels, num_of_classes)
                         for labels in
                         [train_b_1['labels'], train_b_2['labels'],
                          train_b_3['labels'], train_b_4['labels'],
                          train_b_5['labels']]])

testX = test_batch['data'].astype('float32') / 255
testY = np_utils.to_categorical(test_batch['labels'], num_of_classes)


def main():
    """
    For 1-NN we got accuracy of 25.41 and naive Bayes we got accuracy of 19.53
    """

    model = Sequential()

    # tested sigmoid, softmax and relu for layer activation & with relu got the highest accuracy
    model.add(Dense(500, input_shape=(32 * 32 * 3,), activation='relu'))
    model.add(Dense(100, input_shape=(32 * 32 * 3,), activation='relu'))
    model.add(Dense(50, input_shape=(32 * 32 * 3,), activation='relu'))
    model.add(Dense(10, activation='sigmoid'))

    keras.optimizers.SGD(lr=0.5)
    model.compile(optimizer='sgd', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(trainX, trainY, validation_data=(testX, testY), epochs=10)


main()