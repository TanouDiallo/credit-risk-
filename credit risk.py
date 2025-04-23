import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# import de données  : 

df = pd.read_csv("/workspaces/credit-risk-/exemple.csv")

df.columns

df.sample(10)
df.describe()
df.info()