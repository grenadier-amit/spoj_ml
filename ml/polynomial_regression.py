import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


filename = 'spoj_metadata_classical.csv'
data = pd.read_csv(filename)

X=data[['thumbs_up','thumbs_down','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['score']

poly=PolynomialFeatures(degree=2)
X_F1_poly=poly.fit_transform(X)

X_train, X_test, y_train, y_test=train_test_split(X_F1_poly,y,random_state=0)

linreg=LinearRegression().fit(X_train,y_train)

print('(poly deg 2)R-squared score(training):{:.3f}'.format(linreg.score(X_train,y_train)))
print('(poly deg 2)R-squared score(test):{:.3f}'.format(linreg.score(X_test,y_test)))
print('\n')

linreg=Ridge().fit(X_train,y_train)
print('(poly deg 2 + ridge)R-squared score(training):{:.3f}'.format(linreg.score(X_train,y_train)))
print('(poly deg 2 + ridge)R-squared score(test):{:.3f}'.format(linreg.score(X_test,y_test)))


















