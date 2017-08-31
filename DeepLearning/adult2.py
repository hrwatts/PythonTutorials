#neural networks, preprocessing data
#python3 ~/PythonTutorials/DeepLearning/adult2.py

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
features = df.iloc[:,:13]
nation = df.iloc[:,13]
target = df.iloc[:,14]
print(features.head())
print(nation.head())
print(type(nation))
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

#now we will change nation from classes to continuous with GDP/c
def shorter(word):
	return word[1:]

nation = nation.apply(shorter)
#many of these must be resolved manually, some are outright typos
nation[nation=='Laos']='Lao PDR'
nation[nation=='El-Salvador']='El Salvador'
nation[nation=='Taiwan']='Korea, Rep.'
nation[nation=='Trinadad&Tobago']='Trinidad and Tobago'
nation[nation=='Yugoslavia']='Serbia'
nation[nation=='Hmonitor = EarlyStopping(patience=2)olland-Netherlands']='Netherlands'
nation[nation=='Holand-Netherlands']='Netherlands'
nation[nation=='Scotland']='United Kingdom'
nation[nation=='South']='Solomon Islands'
nation[nation=='England']='United Kingdom'
nation[nation=='Dominican-Republic']='Dominican Republic'
nation[nation=='Outlying-US(Guam-USVI-etc)']='Guam'
nation[nation=='Puerto-Rico']='Puerto Rico'
nation[nation=='Columbia']='Colombia'
nation[nation=='Hong']='Hong Kong SAR, China'
nation[nation=='United-States']='United States'
nation[nation=='?']='United States'
nation[nation=='Iran']='Iran, Islamic Rep.'
gdp = pd.read_csv('/home/christian/Downloads/gdpc/gdpc.csv')
print(gdp.head())
for country in gdp['Country Name']:
	if country in list(nation):
		val = (gdp[gdp['Country Name']==country])['2012'].iloc[0]
		nation[nation==country]=val
nation = nation.as_matrix().astype(float)
X.append(nation)

X = np.transpose(np.array(X))
n_cols = X.shape[1]

#now that preprocessing is done let us build our model
def get_model(n_cols, node, layers=1, half=True):
	model = Sequential()
	model.add(Dense(node, activation='sigmoid', input_shape=(n_cols,)))
	for lay in range(layers):
		if half:
			model.add(Dense(int(node*.5), activation='sigmoid'))
			half=True
		else:
			model.add(Dense(node, activation='sigmoid'))
	model.add(Dense(2, activation='softmax'))
	return model
#changes in architecture we want to try
nodes = [16,32,64,128,256]

#for recording histories of models
histories=[]

#early stopping monitor
monitor = EarlyStopping(patience=2)

#fit our models over our varius setting on data
for node in nodes:
	print('Fitting with '+str(node)+' nodes per layer')
	model = get_model(n_cols,node, 3,False)
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	fitted = model.fit(X, y, epochs=10, callbacks=[monitor])
	histories.append(fitted.history['acc'])

#plot for visuals
colors=['y','g','r','b','k']
for c,h in enumerate(histories):
	plt.plot(h,colors[c])
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()
