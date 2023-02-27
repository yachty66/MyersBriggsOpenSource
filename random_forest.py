################### IMPORTS ###################

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import data as data

################### Training ###################

d = data.Data()
train_x, train_y, test_x, test_y = d.get_data()

clf = RandomForestClassifier()
clf.fit(train_x, train_y)

################### Evaluation ###################

prediction = clf.predict(test_x)
true = test_y

prediction_for_scores = prediction.tolist()
true_for_scores = true

accuracy = accuracy_score(true_for_scores, prediction_for_scores)
scores = precision_recall_fscore_support(true_for_scores, prediction_for_scores, average='weighted')
print("Accuracy: " + str(accuracy), "Precision: " + str(scores[0]), "Recall: " + str(scores[1]), "F1-Score: " + str(scores[2]))

'''# compare prediction and true in string format
for i in range(0, len(prediction)):
    for key, value in mapping.items():
        if value == prediction[i]:
            prediction[i] = key

for i in range(0, len(true)):
    for key, value in mapping.items():
        if value == true[i]:
            true[i] = key
            
for i in range(len(prediction)):
    print("----")
    print(prediction[i]) 
    print(true[i])
    print("----")'''


