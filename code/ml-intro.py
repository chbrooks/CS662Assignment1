import sklearn

### load a dataset. The independent variables are in X, and the true classifications are in y.
def getDataset(str) :
    X, y = datasets.load_breast_cancer(return_X_y=True)
    return X,y

### train on the first 80% of the data
def dtTrain(Xvals, yvals):
    tlength = len(Xvals) 0.8
    dt = sklearn.tree.DecisionTreeClassifier().fit(X_train[:tlength], y_train[:tlength])
    return dt

## test on the other 20%

### implement 5-fold cross-validation, 10-fold, leave-one-out.
### measure precision and accuracy


  load breast cancer dataset


  train on DecisionTreeClassifier.

  next, use train_test_split to do 5-fold and leave-one-out
  validation.

>>> X, y = datasets.load_breast_cancer(return_X_y=True)
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
>>> cl=tree.DecisionTreeClassifier().fit(X_train, y_train)
>>> scores = cross_val_score(cl, X, y, cv=5)
>>> scores
array([0.9122807 , 0.92105263, 0.92105263, 0.94736842, 0.91150442])
>>> scores = cross_val_score(cl, X, y, cv=5, scoring='average_precision')
>>> scores
  array([0.92245039, 0.91321761, 0.91989687, 0.94981174, 0.92559672])

  explain precision and accuracy.