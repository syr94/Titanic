# -*- coding: utf-8 -*-
"""lesson6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x-1O27l_sMqBuhh-Cp5A2Vms6n6GSfhz
"""

import numpy as np
import pandas as pd

data = pd.read_csv('TITANIC_full.csv', index_col = 0) # Downloading dataset
data

"""<b>Survived</b> - Выжил (0 = нет, 1 = да)<br>
<b>Pclass</b> - Класс билета(1-первый, 2-второй, 3-третий)<br>
<b>Name</b> -  Имя пассажира<br>
<b>Sex</b> - Пол человека male - муж., female - жен.<br>
<b>Age</b> - Возраст в годах <br>
<b>Sibsp</b> - количество сестер, братьев, жен, мужей на Титанике<br>
<b>Parch</b> - Количество родителей или детей на Титанике<br>
<b>Ticket</b> - Билет <br>
<b>Fare</b> - Цена Билета<br>
<b>Cabin</b> - номер каюты<br>
<b>Embarked</b> - Порт посадки (C-Cherbourg, Q-Queenstown, S - Southampton<br>
"""

data.isna().sum() # how many columns of values ​​from NAN

data.Age.fillna(data.Age.mode()[0], inplace = True) # Fulling with mode
data.Cabin.fillna(data.Cabin.mode()[0], inplace = True)
data.Embarked.fillna(data.Embarked.mode()[0], inplace = True)

target = data['Survived'] # Y 
data = data.drop('Survived', axis = 1) # X

data.iloc[700]

Me = [1.0, 'Mr. Mikhail Syropyatov', 'male', 25.0, 1, 0, 'PC 17758', 300.0, 'C62 C64', 'C'] # Creating myself

data.loc[891] = Me # add myself to the end of the dataset
data.tail(5)

from sklearn.preprocessing import LabelEncoder #Encoder for str

le = LabelEncoder() # Initialization of Encoder

data['Sex'] = le.fit_transform(data['Sex']) # Encode of of columns where we can find str
data['Name'] = le.fit_transform(data['Name'])
data['Ticket'] = le.fit_transform(data['Ticket'])
data['Cabin'] = le.fit_transform(data['Cabin'])
data['Embarked'] = le.fit_transform(data['Embarked'])

from sklearn.model_selection import train_test_split #import split of data set method

x_train, x_test, y_train, y_test = train_test_split(data, target, test_size = 0.2, random_state = 0)
# spliting train/test 80/20

params ={ # for GridSerachCV
    'ccp_alpha' : 0.00001,
    'max_depth' : 1000,
    'criterion' : 'gini',
    'min_samples_split' : [1, 2]
}

from sklearn.ensemble import RandomForestClassifier #importing model
#from sklearn.model_selection import GridSearchCV


RFC = RandomForestClassifier() #Init model

#GS = GridSearchCV(RFC, params, cv=5) можно использовать GridSearch для поиска лучших параметров,
# как он работает смотрите видеоурок.

RFC.fit(x_train, y_train) # training our model
#GS.fit(x_train, y_train)

#GS.best_params_ #best params

#GS.best_score_ #best accuracy

from sklearn.metrics import accuracy_score #method for 

pred_RFC_train = RFC.predict(x_train) #prediction for train data
pred_RFC_test = RFC.predict(x_test) #prediction for test data

print('Правильность на обучающем наборе:', np.round(accuracy_score(y_train, pred_RFC_train), 2)) #Printing our acc score
print('Правильность на тестовом наборе:', np.round(accuracy_score(y_test, pred_RFC_test), 2)) #

{el:0  for el in data} #new passanger

Me = {'Age': 25.0, # looking mine encoded  params from last position of data
 'Cabin': 73.0,
 'Embarked': 0.0,
 'Fare': 300.0,
 'Name': 563.0,
 'Parch': 0.0,
 'Pclass': 1.0,
 'Sex': 1.0,
 'SibSp': 1.0,
 'Ticket': 610.0}

Me = pd.DataFrame(data = [Me]) # creating DataFrame from dict

prediction = RFC.predict(Me) # Prediction of surviving me, where 0 - not survived, 1 - survived
print(prediction)

"""<b>Ниже представлены другие модели</b>
<br>
и как они себя ведут<br>
<b>Below are other models</b>
"""

data.iloc[890] #

from sklearn.tree import  DecisionTreeClassifier

DTC = DecisionTreeClassifier()

DTC.fit(x_train, y_train)

pred_DTC_train = DTC.predict(x_train)
pred_DTC_test = DTC.predict(x_test)

print('Правильность на обучающем наборе:', np.round(accuracy_score(y_train, pred_DTC_train), 2))
print('Правильность на тестовом наборе:', np.round(accuracy_score(y_test, pred_DTC_test), 2))

from sklearn.neighbors import KNeighborsClassifier

KNC = KNeighborsClassifier(leaf_size= 100, n_neighbors=2)

KNC.fit(x_train, y_train)

pred_KNC_train = KNC.predict(x_train)
pred_KNC_test = KNC.predict(x_test)

print('Правильность на обучающем наборе:', np.round(accuracy_score(y_train, pred_KNC_train), 2))
print('Правильность на тестовом наборе:', np.round(accuracy_score(y_test, pred_KNC_test), 2))

from sklearn.linear_model import SGDClassifier

SGD = SGDClassifier(alpha=0.001,max_iter=15000)

SGD.fit(x_train, y_train)

pred_SGD_train = SGD.predict(x_train)
pred_SGD_test = SGD.predict(x_test)

print('Правильность на обучающем наборе:', np.round(accuracy_score(y_train, pred_SGD_train), 2))
print('Правильность на тестовом наборе:', np.round(accuracy_score(y_test, pred_SGD_test), 2))