import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler

filename = 'spoj_metadata_classical.csv'
data = pd.read_csv(filename)

X=data[['thumbs_up','thumbs_down','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['score']

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=0)

scaler=MinMaxScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
for this_alpha in [0,1,2,5,10,20,50,100]:
	linlasso=Lasso(alpha=this_alpha,max_iter=10000).fit(X_train_scaled,y_train)
	print(this_alpha)
	print('R-squared score(training):{:.3f}'.format(linlasso.score(X_train_scaled,y_train)))
	print('R-squared score(test):{:.3f}'.format(linlasso.score(X_test_scaled,y_test)))
	print('\n')


















