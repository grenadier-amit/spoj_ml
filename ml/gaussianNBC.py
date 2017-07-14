import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

filename = 'spoj_metadata_final.csv'
data = pd.read_csv(filename)
X=data[['thumbs_up','thumbs_down','score','ac_percent','imple_diff','concept_diff','year','time_limit','source_limit','user_ac','total_sub','total_ac','total_wa','ct_error','rt_error','total_tle']]
y=data['type']

X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=0)

nbclf=GaussianNB().fit(X_train,y_train)

print('Accuracy of GaussianNB on training set:{:.3f}'.format(nbclf.score(X_train,y_train)))
print('Accuracy of GaussianNB on test set:{:.3f}'.format(nbclf.score(X_test,y_test)))





















