import os
import glob

import cv2
import numpy as np
from keras.models import Model
from keras.layers import Dense, Activation, MaxPool2D, Conv2D, Flatten, Dropout, Input, BatchNormalization, Add
from keras.optimizers import Adam

# from google.colab import drive
# drive.mount('/content/gdrive')

def conv_block(x, filters):
    x = BatchNormalization()(x)
    x = Conv2D(filters, (3, 3), activation='relu', padding='same') (x)

    x = BatchNormalization()(x)
    shortcut = x
    x = Conv2D(filters, (3, 3), activation='relu', padding='same') (x)
    x = Add() ([x, shortcut])
    x = MaxPool2D((2, 2), strides=(2, 2)) (x)

    return x

def custom_model(input_shape, n_classes):

    input_tensor = Input(shape=input_shape)

    x = conv_block(input_tensor, 32)
    x = conv_block(x, 64)
    x = conv_block(x, 128)
    x = conv_block(x, 256)
    x = conv_block(x, 512)

    x = Flatten() (x)
    x = BatchNormalization() (x)
    x = Dense(512, activation='relu') (x)
    x = Dense(512, activation='relu') (x)

    output_layer = Dense(n_classes, activation='softmax') (x)

    inputs = [input_tensor]
    model = Model(inputs, output_layer)

    return model


def main():
    # Data parameter
    input_height = 48
    input_width = 48    
    input_channel = 3
    input_shape = (input_height, input_width, input_channel)
    n_classes = 4 # 4 objects

    # Modeling
    # 'custom':
    model = custom_model(input_shape, n_classes)
  
    adam = Adam()
    model.compile(
        optimizer=adam,
        loss='categorical_crossentropy',
        metrics=['acc'],
    )

    
    # data_dir = './gdrive/My Drive/emotion_cnn'   
    data_dir = './'
    match_obj1 = os.path.join( data_dir, 'gtg', '*.jpg')
    paths_obj1 = glob.glob(match_obj1)
    match_obj2 = os.path.join( data_dir, 'lwj', '*.jpg')
    paths_obj2 = glob.glob(match_obj2)

    match_test = os.path.join(data_dir, 'test', '*.jpg')
    paths_test = glob.glob(match_test)

    n_train = len(paths_obj1) + len(paths_obj2)
    n_test = len(paths_test)

    # Initialization dataset matrix
    trainset = np.zeros(
        shape=(n_train, input_height, input_width, input_channel),
        dtype='float32',
    )
    
    label = np.zeros(
        shape=(n_train, n_classes),
        dtype='float32',
    )
    
    testset = np.zeros(
        shape=(n_test, input_height, input_width, input_channel),
        dtype='float32',
    )

    # Read image and resize to data set
    paths_train = paths_obj1 + paths_obj2

    for ind, path in enumerate(paths_train):      
        try:
            image = cv2.imread(path)
            resized_image = cv2.resize(image, (input_width, input_height))
            trainset[ind] = resized_image

        except Exception as e:
            print(path) # print out the Image that cause exception error
        
    for ind, path in enumerate(paths_test):
        try:
            image = cv2.imread(path)
            resized_image = cv2.resize(image, (input_width, input_height))
            testset[ind] = resized_image
            
        except Exception as e:
            print(path) # print out the Image that cause exception error

    # Set the mark of the training set
    n_obj1 = len(paths_obj1)
    n_obj2 = len(paths_obj2)
  
    begin_ind = 0
    end_ind = n_obj1
    label[begin_ind:end_ind, 0] = 1.0

    begin_ind = n_obj1
    end_ind = n_obj1 + n_obj2
    label[begin_ind:end_ind, 1] = 1.0


    # Normalize the value between 0 and 1
    trainset = trainset / 255.0
    testset = testset / 255.0

    # # Training model
    model.fit(
        trainset,
        label,    
        epochs=20,  # no. of rounds of training => 8 rounds
        validation_split=.2,   # percentage of dataset use for validation at trainiing => 20% (2000 images, 1600 for training, 400 for validation)
        validation_data=trainset
    )
    # model.fit(trainset, label, epochs=20, batch_size=64)

    # Saving model architecture and weights (parameters)
    model_desc = model.to_json()
    model_file = './Data/model.json'
    with open(model_file, 'w') as file_model:                           
        file_model.write(model_desc)

    weights_file = './Data/weights.h5'
    model.save_weights(weights_file )

    # Execution predication
    if testset.shape[0] != 0:
        result_onehot = model.predict(testset)
        print(result_onehot)
        result_sparse = np.argmax(result_onehot, axis=1)
    else:
        result_sparse = list()
    
    # Print predication results
    print(' File name \t forecast category')

    for path, label_id in zip(paths_test, result_sparse):
        filename = os.path.basename(path)
        if label_id == 0:
            label_name = 'gtg'
        elif label_id == 1:
            label_name = 'lwj'
     
        print('%s\t%s' % (filename, label_name))
    
if __name__ == '__main__':
    main()