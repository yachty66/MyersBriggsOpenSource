import h2o
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import data as data
from h2o.automl import H2OAutoML
import csv

h2o.init()
model = h2o.load_model("models/GBM_model_python_1677660125612_1")

d = data.Data()
train_x, train_y, test_x, test_y = d.get_data()
fieldnames = ['target'] + ['a{}'.format(i) for i in range(1, len(test_x[0])+1)]

with open('data/test_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(test_y)):
        row = {'target': test_y[i]}
        for j in range(len(test_x[i])):
            row['a{}'.format(j+1)] = test_x[i][j]
        writer.writerow(row)

test = h2o.import_file("data/test_data.csv")

predict = model.predict(test)

predict_column=predict['predict']
predictions_l = predict_column.as_data_frame()
predictions_l = [item for sublist in predictions_l for item in sublist][1:]

true_l = []
with open('data/test_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        true = row['target']
        true_l.append(true)

prediction_for_scores = predictions_l
true_for_scores = true_l

accuracy = accuracy_score(true_for_scores, prediction_for_scores)
scores = precision_recall_fscore_support(true_for_scores, prediction_for_scores, average='weighted')
print("Accuracy: " + str(accuracy), "Precision: " + str(scores[0]), "Recall: " + str(scores[1]), "F1-Score: " + str(scores[2]))