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




#iter over predictions and set each element back to value from d.mapping
'''for i in range(0, len(prediction_for_scores)):
    for key, value in d.mapping.items():
        if value == prediction_for_scores[i]:
            prediction_for_scores[i] = key

for i in range(0, len(true_for_scores)):
    for key, value in d.mapping.items():
        if value == true_for_scores[i]:
            true_for_scores[i] = key

for i in range(len(prediction_for_scores)):
    print("----")
    print(prediction_for_scores[i]) 
    print(true_for_scores[i])
    print("----")'''