import pandas as pd
from sklearn.model_selection import train_test_split
from variables import *

# import GUI_Import_CSV

# Loading the dataset
dataset = pd.read_csv(data_dir + "\\" + Parasitized)
print(dataset)

# Split into training and test dataset
x = dataset.drop(["Label"], axis=1)
print(x)
y = dataset["Label"]
# print(y)
# x_train, x_test, y_train, y_test = train_test_split
