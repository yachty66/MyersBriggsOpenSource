################### IMPORTS ###################

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import data as data

################### Training ###################

d = data.Data()
train_x, train_y, test_x, test_y = d.get_data()

svm = SVC(kernel='linear', C=1, random_state=0)
svm.fit(train_x, train_y)

################### Evaluation ###################

prediction = svm.predict(test_x)
true = test_y

prediction_for_scores = prediction.tolist()
true_for_scores = true

accuracy = accuracy_score(true_for_scores, prediction_for_scores)
scores = precision_recall_fscore_support(true_for_scores, prediction_for_scores, average='weighted')
print("Accuracy: " + str(accuracy), "Precision: " + str(scores[0]), "Recall: " + str(scores[1]), "F1-Score: " + str(scores[2]))
