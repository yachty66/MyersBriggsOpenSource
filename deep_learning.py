import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import torch
import torch.nn as nn
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import data as data

d = data.Data()
train_x, train_y, test_x, test_y = d.get_data()

test_x = pd.DataFrame(test_x)
test_y = pd.DataFrame(test_y)
train_x = pd.DataFrame(train_x)
train_y = pd.DataFrame(train_y)

#convert data to tensors
test_x = torch.tensor(test_x.to_numpy()).float()
test_y = torch.tensor(test_y.to_numpy()).float()
train_x = torch.tensor(train_x.to_numpy()).float()
train_y = torch.tensor(train_y.to_numpy()).float()

#create a simple neural network with pytroch
model = torch.nn.Sequential(
    nn.Linear(60, 100), 
    nn.ReLU(),
    nn.Linear(100, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

criterion = torch.nn.MSELoss()

optimizer = torch.optim.AdamW(model.parameters(), lr=0.01)

for epoch in range(1000):
    y_pred = model(train_x)
    loss = criterion(y_pred, train_y.float())
    #print("epoch: ", epoch, "loss: ", loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
#cacluate predictions
pred_y = model(test_x.float())

print(torch.round(pred_y))
print(test_y)