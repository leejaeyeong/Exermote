from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax, array
from tensorflow.python.lib.io import file_io
from pandas import read_csv
from sklearn.preprocessing import LabelEncoder, MinMaxScaler



(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(10000, 784).astype('float32') / 255.0
y_test = np_utils.to_categorical(y_test)
xhat_idx = np.random.choice(x_test.shape[0], 5)
xhat = x_test[xhat_idx] 

#print(x_test)
#print(y_test)
#print(xhat.tolist())
timesteps = 40
timesteps_in_future = 20
train_file = '../MoviLabData/xin_final.csv'

#file load
file_stream = file_io.FileIO(train_file, mode='r')
dataframe = read_csv(file_stream, header=0)
dataframe.fillna(0,inplace=True)
dataset = dataframe.values

X = dataset[:, [
    2, 3, 4, 5, 6, 7,
    ]].astype(float)

y = dataset[:,0]

# data parameters
data_dim = X.shape[1]
num_classes = len(set(y))
type_classes = list(set(y))
# scale X
scaler = MinMaxScaler(feature_range=(0,1))
X = scaler.fit_transform(X)

# encode Y
encoder = LabelEncoder()
encoder.fit(y)
encoded_y = encoder.transform(y)
hot_encoded_y = np_utils.to_categorical(encoded_y)

# prepare data for LSTM
def create_LSTM_dataset(x,y,timesteps) :
    dataX, dataY = [], []
    for i in range(len(x) - timesteps + 1) :
        dataX.append(x[i : i + timesteps, :])
        dataY.append(y[i + timesteps - timesteps_in_future -1, :])
    return array(dataX), array(dataY)
X, hot_encoded_y = create_LSTM_dataset(X,hot_encoded_y,timesteps)


from keras.models import load_model
model = load_model('best_weights.h5')
model.summary()

# Excercise Predict 
yhat = model.predict_classes(X)
pro = model.predict_proba(X)
print(pro[0])
print(pro[1])
for i in range(len(yhat)):
    print('{} Exercise Predict : '.format(i) + type_classes[yhat[i]])
    #print('{} : '.format(i+2) + 'result -----> break [{0:.2f}],'.format(pro[i][0]) + 'squat [{0:.2f}],'.format(pro[i][1]) + 'pushup [{0:.2f}],'.format(pro[i][2]) + 'sqaut [{0:.2f}],'.format(pro[i][3]) + 'raise [{0:.2f}]'.format(pro[i][4]) + '/ Exercise Predict : ' + type_classes[yhat[i]])
