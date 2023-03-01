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
model = h2o.load_model("models/GBM_5_AutoML_1_20230301_90513")

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

model.train(x=x, y=y, training_frame=train)

h2o.save_model(model, path="")
