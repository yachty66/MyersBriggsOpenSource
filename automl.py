################### IMPORTS ###################

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import data as data
import h2o
from h2o.automl import H2OAutoML
import csv

################### Training ###################

h2o.init()

d = data.Data()
train_x, train_y, test_x, test_y = d.get_data()
fieldnames = ['target'] + ['a{}'.format(i) for i in range(1, len(train_x[0])+1)]
#i need to create a csv file where the first column is train_y and the rest are train_x. write it into data/train.csv
with open('data/train_data.csv', 'w', newline='') as file:
    # Create a CSV DictWriter object
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header row
    writer.writeheader()
    # Write the data rows
    for i in range(len(train_y)):
        row = {'target': train_y[i]}
        for j in range(len(train_x[i])):
            row['a{}'.format(j+1)] = train_x[i][j]
        writer.writerow(row)
        
with open('data/test_data.csv', 'w', newline='') as file:
    # Create a CSV DictWriter object
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header row
    writer.writeheader()
    # Write the data rows
    for i in range(len(test_y)):
        row = {'target': test_y[i]}
        for j in range(len(test_x[i])):
            row['a{}'.format(j+1)] = test_x[i][j]
        writer.writerow(row)

train = h2o.import_file("data/train_data.csv")
test = h2o.import_file("data/test_data.csv")

# Identify predictors and response
x = train.columns
y = "target"
x.remove(y)

train[y] = train[y].asfactor()
test[y] = test[y].asfactor()

aml = H2OAutoML(max_models=1, seed=1, include_algos=["GBM"])
aml.train(x=x, y=y, training_frame=train)

# View the AutoML Leaderboard
print("Leaderboard:")
print(aml.leaderboard)
print("Leader:")
print(aml.leader)

h2o.save_model(aml.leader, path="", force=True)


################### Evaluation ###################

'''prediction = clf.predict(test_x)
true = test_y

prediction_for_scores = prediction.tolist()
true_for_scores = true

accuracy = accuracy_score(true_for_scores, prediction_for_scores)
scores = precision_recall_fscore_support(true_for_scores, prediction_for_scores, average='weighted')
print("Accuracy: " + str(accuracy), "Precision: " + str(scores[0]), "Recall: " + str(scores[1]), "F1-Score: " + str(scores[2]))'''





