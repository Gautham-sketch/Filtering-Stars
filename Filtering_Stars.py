import csv
import pandas as pd
import matplotlib.pyplot as plt

whole = []
with open('Final_Projet.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        whole.append(row)
headers = whole[0]
data = whole[1: ]

lightyear_frame = pd.DataFrame()
gravity_frame = pd.DataFrame()

for i in data[6]:
    if(data[6] < 100 or data[6] == 100):
        lightyear_frame.append(i)

for j in data[9]:
    if(data[9] > 150 and data[9] < 350):
        gravity_frame.append(j)

with open('Final_Project_Data.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
    writer.writerow(lightyear_frame)
    writer.writerow(gravity_frame)