#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

### fit and predict ###
def svm_clf(features_train, features_test, labels_train, labels_test, kernel="rbf", C=1):

    # Import scikit-learn metrics module for SVC
    from sklearn.svm import SVC
    # Import scikit-learn metrics module for accuracy calculation
    from sklearn import metrics

    # Create a SVC Classifier
    clf = SVC(kernel=kernel, C=C)

    # Train the model using the training sets
    t0 = time()
    clf.fit(features_train, labels_train)
    training_time = round(time() - t0, 3)

    # Predict the response for test dataset
    t0 = time()
    labels_test_pred = clf.predict(features_test)
    prediction_time = round(time() - t0, 3)

    # Model Accuracy, how often is the classifier correct?
    accuracy = metrics.accuracy_score(labels_test, labels_test_pred)

    return labels_test_pred, accuracy, training_time, prediction_time




if __name__ == "__main__":
    C = 10000

    labels_test_pred, accuracy, training_time, prediction_time = svm_clf(features_train, features_test, labels_train, labels_test, kernel="rbf", C=c)
    print "C = ", c
    print "Accuracy:", accuracy
    print "Training time:", training_time, "s"
    print "Prediction time:", prediction_time, "s"

#########################################################


