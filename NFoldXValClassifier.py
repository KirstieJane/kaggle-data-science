# This script does n-fold cross validation for Kaggle's getting started 
# challenge
# The three arguments are:
#  - training features file (csv format)
#  - training classes (0/1)
#  - testing features file (csv format)
# 
# Run using
# > python NFoldXValClassifier.py train.csv trainLabels.csv test.csv

import sys
import csv
from sklearn import tree
from scorer import Scorer
from sklearn.cross_validation import StratifiedKFold

def main(argv):

    # Check number of command line arguments
    if len(argv) != 3:
        print "Error usage:"
        print "python simple_classifier.py <train_features> <train_classes> <test_features>"
        sys.exit()
    else:
        trainfeatfile = argv[0]
        trainclassfile = argv[1]
        testfeatfile = argv[2]

    y=[] # y is the classes, 1st column
    X=[] # X is the features, 2nd column onwards
    X_test=[] # X_test is features to test on

    # Open training CSV file and save data in X
    with open(trainfeatfile,'r') as traincsv:
        trainreader = csv.reader(traincsv)
        for row in trainreader:
            X.append(row)

    # Open training classes file and save in y
    with open(trainclassfile,'r') as trainclass:
        for row in trainclass:
            y.append(int(row))
    predictions = [0] * len(y)

    # Open testing CSV file and save data in X_test
    with open(testfeatfile,'r') as testcsv:
        testreader = csv.reader(testcsv)
        for row in testreader:
            X_test.append(row)

    # Do N-fold X-val
    N=10
    skf = StratifiedKFold(y, N)

    for train, test in skf:
        # Get training and test subsets
        X_sub = [X[a] for a in train]
        y_sub = [y[a] for a in train]
        X_test_sub = [X[a] for a in test]
        #Train a decision tree classifier for each split.
        clf = tree.DecisionTreeClassifier(min_samples_leaf=50)
        clf.fit(X_sub,y_sub)
        #Predict on test subset and save results
        predictions_sub = clf.predict(X_test_sub)
        for i in range(0,len(test)):
            predictions[test[i]] = predictions_sub[i]


    # Score results
    scorer=Scorer(0)

    # Compute classification performance
    scorer.printAccuracy(predictions, y, "Training set performance")

    return

if __name__ == "__main__":
   main(sys.argv[1:])
