import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# import de données  : 

df = pd.read_csv("https://raw.githubusercontent.com/TanouDiallo/credit-risk-/refs/heads/main/exemple.csv")

df.columns

df.sample(10)
df.describe()
df.info()