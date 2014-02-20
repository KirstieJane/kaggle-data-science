kaggle-data-science
===================

For Kaggle data science problems

HelloWorld.py
-------------
A simple program to get started with Python. Run by typing

> python HelloWorld.py


HelloAnyone.py
--------------
An extension of HelloWorld - say hello to anyone. Run by typing

> python HelloAnyone.py Catherine


SimpleClassifier.py
-------------------
A script to get started on Kaggle's 'getting started' challenge. It trains a really simple decision tree classifier using the csv library to read in the data.

The data to use with this is available on Kaggle:

http://www.kaggle.com/c/data-science-london-scikit-learn

It consists of 3 files:
- train.csv
- trainLabels.csv
- test.csv

These are training features and their associated classes (1 or 0), and test features. Run by typing

> python SimpleClassifier.py train.csv trainLabels.csv test.csv

The output is a long list of 1's and 0's corresponding to the predicted class for each example in test.csv.