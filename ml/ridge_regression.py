import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler

filename = 'spoj_metadata_classical.csv'
data = pd.read_csv(filename)

X=data[['thumbs_up','thumbs_down','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['score']

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=0)

linridge=Ridge(alpha=20.0).fit(X_train,y_train)
print('R-squared score(training):{:.3f}'.format(linridge.score(X_train,y_train)))
print('R-squared score(test):{:.3f}'.format(linridge.score(X_test,y_test)))
print('Number of non-zero features: {}'.format(np.sum(linridge.coef_!=0)))
print('\n')

scaler=MinMaxScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
for this_alpha in [0,1,10,20,50,100,1000]:
	clf=Ridge(alpha=this_alpha).fit(X_train_scaled,y_train)
	#r2_score=clf.score(X_test_scaled,y_test)
	print(this_alpha)
	print('R-squared score after feature normalization(training):{:.3f}'.format(clf.score(X_train_scaled,y_train)))
	print('R-squared score after feature normalization(test):{:.3f}'.format(clf.score(X_test_scaled,y_test)))
	print('\n')



















