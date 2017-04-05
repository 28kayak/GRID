__author__ = 'kaya'
# !C:\Python27\python.exe
import csv
import pandas as pd
from tqdm import tqdm
import os
import codecs

#path to the data location
path = 'C:/Users/kaya/PycharmProjects/GRID_skillCheck/data'
data_location = path + "/tokyo.csv"
#os.chdir('C:/Users/kaya/PycharmProjects/GRID_skillCheck/data')
#read csv file with encording option
#df = pd.read_csv("wether_tokyo.csv", encoding="cp932")

#column = df.loc[: ,  [u'??????????????']]
#print(column)

df = pd.read_csv(data_location, skiprows=2, header=1, encoding='Shift_JIS')
print(df.head(10))
for i in tqdm(range(10000000)):
    pass

#with codecs.open(data_location, "r", "Shift-JIS", "ignore") as file:
 #   df = pd.read_table(file, delimiter=",")
#
 #   print('df:', df.shape)