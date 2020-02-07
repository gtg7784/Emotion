import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

import matplotlib.pyplot as plt

model = Sequential()

x = np.array([1, 2, 3, 4, 5])
y = np.array([0,0,0,1,1])

model.add(Dense(1, input_dim=(1),activation='sigmoid'))
model.compile(loss="binary_crossentropy", optimizer=optimizers.RMSprop(lr=0.1), metrics = ['accuracy'])
hist = model.fit(x,y,epochs=200)

plt.plot(hist.history['loss'])
plt.title('LOSS')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='upper left')
plt.show()

print(model.summary())

print(model.predict([1,2,3,4,5,6,7,8,9,10]))

print(model.predict_classes([1,2,3,4,5,6,7,8,9,10]))
