# Load libraries
import json
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Parse the JSON file
with open('data.json','r+') as f:
    data = json.load(f)
    # Clean the 2 average by rounding them with 2 decimals
    data['average_discount_onoffer'] = round(data['average_discount_onoffer'],2)
    data['average_discount_used'] = round(data['average_discount_used'],2)
    # Reposition at the beginning of the file and override the file with the corrected averages
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()

# Using the number of male items and female items for each customer

#Define the test labels
test_labels = case when data['male_items'] > data['female_items'] then 'male' else 'female' end;

#Build a Logistic Regression model
l_clf = LogisticRegression()
l_clf.fit(data['customer_id'],test_labels)
l_prediction = l_clf.predict(data)]
print l_prediction

#Build a Decision Tree Classifier model
dtc_clf = tree.DecisionTreeClassifier()
dtc_clf = dtc_clf.fit(data['customer_id'],test_labels)
dtc_prediction = dtc_clf.predict(data)
print dtc_prediction

#Build a Random Forest Classifier model
rfc_clf = RandomForestClassifier()
rfc_clf.fit(data['customer_id'],test_labels)
rfc_prediction = rfc_clf.predict(data)
print rfc_prediction

#Build a Support Vector Classifier
s_clf = SVC()
s_clf.fit(X,Y)
s_prediction = s_clf.predict(data)
print s_prediction

#Calculate accuracy scores
dtc_tree_acc = accuracy_score(dtc_prediction,test_labels)
rfc_acc = accuracy_score(rfc_prediction,test_labels)
l_acc = accuracy_score(l_prediction,test_labels)
s_acc = accuracy_score(s_prediction,test_labels)

#Evalute the best classifier for this gender detection problem
classifiers = [‘Decision Tree’, ‘Random Forest’, ‘Logistic Regression’ , ‘SVC’]
accuracy = np.array([dtc_tree_acc, rfc_acc, l_acc, s_acc])
max_acc = np.argmax(accuracy)
print(classifiers[max_acc] + ‘ is the best classifier for this problem’)