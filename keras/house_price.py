from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import pandas as pd

df = pd.read_csv('../data/house_price.csv', delim_whitespace=True, header=None)

df = df.values
X = df[:, 0:13]
Y = df[:, 13]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(X_train, Y_train, epochs=200, batch_size=10)

Y_prediction = model.predict(X_test)
for i in range(5):
  print(Y_prediction[i],Y_test[i])