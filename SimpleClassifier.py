# This script trains a decision tree for Kaggle's 'getting started' challenge
# The three arguments are:
#  - training features file (csv format)
#  - training classes (0/1)
#  - testing features file (csv format)
# 
# Run using
# > python simple_classifier.py train.csv trainLabels.csv test.csv

import sys
import csv
from sklearn import tree

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

    # Open testing CSV file and save data in X_test
    with open(testfeatfile,'r') as testcsv:
        testreader = csv.reader(testcsv)
        for row in testreader:
            X_test.append(row)

    # Train a decision tree classifier. Though the default settings
    # aren't very good!
    clf = tree.DecisionTreeClassifier()
    clf.fit(X,y)
    predictions = clf.predict(X_test)

    # Print out the predictions, 1 per line
    for predict in predictions:
        print predict

    return

if __name__ == "__main__":
   main(sys.argv[1:])
