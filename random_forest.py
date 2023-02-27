################### IMPORTS ###################

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier
import numpy as np

################### PREPROCEESING ###################
with open("results.txt", "r") as file:
    l_with_all_data = file.readlines()
    l_with_all_data = [line.split(";") for line in l_with_all_data]
    X = [line[1::2] for line in l_with_all_data]
    Y = [line[-1] for line in l_with_all_data]

#iter over x and y and encode them
for i in range(0, len(X)):
    for j in range(0, len(X[i])):
        if X[i][j] == "agree max":
            X[i][j] = 1
        elif X[i][j] == "agree med":
            X[i][j] = 2
        elif X[i][j] == "agree min":
            X[i][j] = 3
        elif X[i][j] == "neutral":
            X[i][j] = 4
        elif X[i][j] == "disagree max":
            X[i][j] = 5
        elif X[i][j] == "disagree med":
            X[i][j] = 6
        elif X[i][j] == "disagree min":
            X[i][j] = 7

#mapping for all available personality types
mapping = {
"ISTJ-T": 1,
"ISTJ-A": 2,
"ISFJ-T": 3,
"ISFJ-A": 4,
"INFJ-T": 5,
"INFJ-A": 6,
"INTJ-T": 7,
"INTJ-A": 8,
"ISTP-T": 9,
"ISTP-A": 10,
"ISFP-T": 11,
"ISFP-A": 12,
"INFP-T": 13,
"INFP-A": 14,
"INTP-T": 15,
"INTP-A": 16,
"ESTJ-T": 17,
"ESTJ-A": 18,
"ESFJ-T": 19,
"ESFJ-A": 20,
"ENFJ-T": 21,
"ENFJ-A": 22,
"ENTJ-T": 23,
"ENTJ-A": 24,
"ESTP-T": 25,
"ESTP-A": 26,
"ESFP-T": 27,
"ESFP-A": 28,
"ENFP-T": 29,
"ENFP-A": 30,
"ENTP-T": 31,
"ENTP-A": 32
}

#encode y
Y = [pt.strip("()\n") for pt in Y]
Y = [mapping[personality] for personality in Y]

################### Training ###################

#create train and test set (80/20)
train_x = X[:int(len(X)*0.8)]
train_y = Y[:int(len(Y)*0.8)]
test_x = X[int(len(X)*0.8):]
test_y = Y[int(len(Y)*0.8):]

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


