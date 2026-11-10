import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/students.csv')
print(df.groupby("Major")["GPA"].mean())