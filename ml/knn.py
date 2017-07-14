import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.tools.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

filename = 'spoj_metadata_final.csv'
data = pd.read_csv(filename)

#data.hist()
#scatter_matrix(data)
#plt.show()
#good_columns=data._get_numeric_data()
#print(good_columns.columns)

X=data[['thumbs_up','thumbs_down','score','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['type']

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=0)

k_range=range(1,50)
scores=[]
for k in k_range:
	knn=KNeighborsClassifier(n_neighbors=5)
	#knn.fit(X_train, y_train)
	cv_scores=cross_val_score(knn,X_train,y_train)
	#scores.append(knn.score(X_test,y_test))
	print(k)
	print('cross-validation scores(3-fold):',cv_scores)
	print('\n')
	scores.append(np.mean(cv_scores))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range,scores)
plt.xticks([0,5,10,15,20,25,30,35,40,45,50])
plt.show()











