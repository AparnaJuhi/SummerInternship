import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)

transaction=[]
for i in range(0,7501):
    transaction.append([str(dataset.values[i,j]) for j in range(0,20)])
    
from apyori import apriori
rules=apriori(transaction, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
#Visualisng the results

result=list(rules)

result=str(result)

frozensets=result.split("RelationRecord")