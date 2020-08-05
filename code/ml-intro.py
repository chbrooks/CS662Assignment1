from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClssifier

### load a dataset. The independent variables are in X, and the true classifications are in y.
def getDataset() :
 # change to iris
   X, y = sklearn.datasets.load_iris(return_X_y=True)
   return X,y


### instantiate a decision tree and train on the data. Xvals are the features, and yvals are the classifications
def dtTrain(Xvals, yvals):
  dt = sklearn.tree.DecisionTreeClassifier()
  ## fit here
  return dt


### use a loop to:
### call dtTrain 80% of the data
### use predict() on the other 20%
### count the number of incorrect classifications
### Print the average number of misclassifications.
def fiveFold(Xvals, yvals) :


  

  

