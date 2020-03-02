import pandas as pd
from variables import *
# import GUI_Import_CSV

# Loading the dataset
dataset = pd.read_csv(data_dir+"\\"+Parasitized)
print(dataset.head())

# Split into training and test dataset
