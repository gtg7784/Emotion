from tensorflow import keras
import numpy as np
import cv2
import os
import glob

input_width = 48
input_height = 48

input_channel = 3
input_shape = (input_height, input_width, input_channel)
n_classes = 2

data_dir = './'
match_obj1 = os.path.join( data_dir, 'train', 'gtg', '*.jpg')
paths_obj1 = glob.glob(match_obj1)
match_obj2 = os.path.join( data_dir, 'train', 'lwj', '*.jpg')
paths_obj2 = glob.glob(match_obj2)

match_test = os.path.join(data_dir, 'test', '*.jpg')
path_test = glob.glob(match_test)

n_train = len(paths_obj1) + len(paths_obj2)
n_test = len(path_test)

trainset = np.zeros(
    shape=(n_train, input_height, input_width, input_channel),
    dtype='float32'
)
testset = np.zeros(
    shape=(n_test, input_height, input_width, input_channel),
    dtype='float32'
)
label = np.zeros(
    shape=(n_train, n_classes),
    dtype='float32'
)

path_train = paths_obj1 + paths_obj2

for i, path in enumerate(path_train):
    try:
        img = cv2.imread(path)
        resized_img = cv2.resize(img, (input_width, input_height))
    except Exception as e:
        print(path)

for i, path in enumerate(path_test):
    try:
        img = cv2.imread(path)
        resized_img = cv2.resize(img, (input_width, input_height))
    except Exception as e:
        print(path)

n_obj1 = len(paths_obj1)
n_obj2 = len(paths_obj2)

begin_ind = 0
end_ind = n_obj1
label[begin_ind:end_ind, 0] = 1.0

begin_ind = n_obj1
end_ind = n_obj1 + n_obj2
label[begin_ind:end_ind, 1] = 1.0

trainset = trainset / 255.0
testset = testset / 255.0

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(input_shape)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(n_classes, activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(trainset, label, epochs=10, batch_size=64)
model.save('./model.h5')

result_onehot = model.predict(testset)
result_sparse = np.argmax(result_onehot, axis=1)

print(result_onehot)
print('\n', result_sparse)

if int(result_sparse) == 0:
    print('gtg')
elif int(result_sparse) == 1:
    print('lwj')