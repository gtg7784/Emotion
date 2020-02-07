from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('../data/iris.csv')
df.head()
df = df.values
X = df[:, 0:4]
obj_y = df[:, 4]

encoder = LabelEncoder()
encoder.fit(obj_y)
obj_y = encoder.transform(obj_y)
Y = np_utils.to_categorical(obj_y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = Sequential()

model.add(Dense(32, input_dim=4, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])

model.fit(X, Y, epochs=50)

Y_prediction = model.predict_classes(X_test)
for i in range(5):
  print(Y_prediction[i],Y_test[i])