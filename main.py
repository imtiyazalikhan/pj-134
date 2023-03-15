import pandas as pd
import csv
import matplotlib as plt

df = pd.read_csv("star_with_gravity.csv")
df.head()

#filtering the stars based on distance
bools =[]
for d in df.Distance:
    if d<=100:
        bools.append(True)
    else:
        bools.append(False)

is_dist = pd.Series(bools)
is_dist.head()