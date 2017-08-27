#neural networks, classification, optimization tuning, architecture tuning
#based on a course I got from Datacamp.com 'Deep Learning in Python'
#python3 ~/Documents/pyfiles/dl/adult.py


#imports
#also, I set the random seed so that the console output is reproducable
import numpy as np
np.random.seed(16)
import pandas as pd
from urllib.request import urlopen
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import Sequential
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping

#dowload, prepare data, which by the way, is a lot of data
raw_data = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
df = pd.read_csv(raw_data, header=None)
features = df.iloc[:,:14]
target = df.iloc[:,14]
print(features.head())
print(target.head())
del df, raw_data
y_factors, y_indices = np.unique(target, return_inverse=True)
y = to_categorical(y_indices)
X = []
total_cols=0
for col in features:
	if type(features[col][0])==str:
		X_factors, X_indices = np.unique(features[col], return_inverse=True)
		new_cols = to_categorical(X_indices)
		total_cols=total_cols+new_cols.shape[1]
		for n in range(new_cols.shape[1]):
			X.append(new_cols[:,n])
	else:
		total_cols+=1
		X.append(features[col].as_matrix())
		
X = np.transpose(np.array(X))

#FINALLY, the data is in a state that can be read by the neural network
#make a model with options
def get_model(n_cols, node, layers=1, half=True):
	model = Sequential()
	model.add(Dense(node, activation='tanh', input_shape=(n_cols,)))
	for lay in range(layers):
		if half:
			model.add(Dense(int(node*.5), activation='tanh'))
			half=True
		else:
			model.add(Dense(node, activation='tanh'))
	model.add(Dense(2, activation='softmax'))
	return model
#changes in architecture we want to try
nodes = [32,128,512,1024]

#for recording histories of models
histories=[]

#fit our models over our varius setting on data
for node in nodes:
	print('Fitting with '+str(node)+' nodes per layer')
	model = get_model(108,node, 1,False)
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	fitted = model.fit(X, y, epochs=4)
	histories.append(fitted.history['acc'])

#plot for visuals
colors=['y','g','r','b','k']
for c,h in enumerate(histories):
	plt.plot(h,colors[c])
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()


#output to console
'''
Using TensorFlow backend.
   0                  1       2           3   4                    5   \
0  39          State-gov   77516   Bachelors  13        Never-married   
1  50   Self-emp-not-inc   83311   Bachelors  13   Married-civ-spouse   
2  38            Private  215646     HS-grad   9             Divorced   
3  53            Private  234721        11th   7   Married-civ-spouse   
4  28            Private  338409   Bachelors  13   Married-civ-spouse   

                   6               7       8        9     10  11  12  \
0        Adm-clerical   Not-in-family   White     Male  2174   0  40   
1     Exec-managerial         Husband   White     Male     0   0  13   
2   Handlers-cleaners   Not-in-family   White     Male     0   0  40   
3   Handlers-cleaners         Husband   Black     Male     0   0  40   
4      Prof-specialty            Wife   Black   Female     0   0  40   

               13  
0   United-States  
1   United-States  
2   United-States  
3   United-States  
4            Cuba  
0     <=50K
1     <=50K
2     <=50K
3     <=50K
4     <=50K
Name: 14, dtype: object
Fitting with 32 nodes per layer
Epoch 1/4
32561/32561 [==============================] - 1s - loss: 0.5475 - acc: 0.7647      
Epoch 2/4
32561/32561 [==============================] - 1s - loss: 0.5386 - acc: 0.7717     
Epoch 3/4
32561/32561 [==============================] - 1s - loss: 0.5410 - acc: 0.7698     
Epoch 4/4
32561/32561 [==============================] - 1s - loss: 0.5443 - acc: 0.7674     
Fitting with 128 nodes per layer
Epoch 1/4
32561/32561 [==============================] - 1s - loss: 0.5438 - acc: 0.7730      
Epoch 2/4
32561/32561 [==============================] - 1s - loss: 0.5492 - acc: 0.7656     
Epoch 3/4
32561/32561 [==============================] - 1s - loss: 0.5476 - acc: 0.7656     
Epoch 4/4
32561/32561 [==============================] - 1s - loss: 0.5417 - acc: 0.7699     
Fitting with 512 nodes per layer
Epoch 1/4
32561/32561 [==============================] - 4s - loss: 0.5637 - acc: 0.7659      
Epoch 2/4
32561/32561 [==============================] - 4s - loss: 0.5550 - acc: 0.7659     
Epoch 3/4
32561/32561 [==============================] - 4s - loss: 0.5593 - acc: 0.7650     
Epoch 4/4
32561/32561 [==============================] - 4s - loss: 0.5599 - acc: 0.7651     
Fitting with 1024 nodes per layer
Epoch 1/4
32561/32561 [==============================] - 16s - loss: 1.6866 - acc: 0.7565      
Epoch 2/4
32561/32561 [==============================] - 16s - loss: 0.5714 - acc: 0.7572     
Epoch 3/4
32561/32561 [==============================] - 16s - loss: 0.5742 - acc: 0.7573     
Epoch 4/4
32561/32561 [==============================] - 16s - loss: 0.5730 - acc: 0.7569 
'''
