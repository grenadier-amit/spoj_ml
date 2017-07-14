import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filename = 'spoj_metadata_classical.csv'
data = pd.read_csv(filename)

X=data[['thumbs_up','thumbs_down','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['score']

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=0)

linreg=LinearRegression().fit(X_train,y_train)
print('R-squared score(training):{:.3f}'.format(linreg.score(X_train,y_train)))
print('R-squared score(test):{:.3f}'.format(linreg.score(X_test,y_test)))






















