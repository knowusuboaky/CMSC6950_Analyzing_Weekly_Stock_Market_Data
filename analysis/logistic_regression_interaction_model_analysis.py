import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
weekly = pd.read_csv('/home/knowusuboaky/dataset-95529.csv')
import statsmodels.api as sm
import statsmodels.formula.api as smf
#Data Changes#
endog = (weekly["Direction"] == "Up").astype("int64")
exog = sm.add_constant(weekly.drop(columns = ["Direction", "Year", "Today"]))

#Interactions model Logistic Regression using pinguoin#
logit_int = pg.logistic_regression(weekly['Lag1'] * weekly['Lag2'], endog)
logit_int.round(4)


#verifying results by pingouin#
#Statsmodel library with one model#
logit_stat_int = sm.Logit(endog, sm.add_constant(weekly['Lag1'] * weekly['Lag2']))
logit_stat_res_int = logit_stat_int.fit()


#Confusion matrix calculation#
matrix_int = pd.DataFrame(logit_stat_res_int.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])
#Plotting Confusion matrix#
fig, ax = plt.subplots()
sns.heatmap(matrix_int, annot = True, cbar = False, ax = ax, fmt = "g", square = True, annot_kws = {"fontsize": "x-large"})
ax.set(xlabel = "predicted label", ylabel = "true label")
ax.figure.savefig('intmodel.png')


#Confusion matrix examination using PyCM#
from pycm import *
cm_int = ConfusionMatrix(matrix={"Class1": {"Class1": 4, "Class2":480}, "Class2": {"Class1": 3, "Class2": 603}})
# Create CM Directly
#Class1=True, Class2=Predicted
print(cm_int)
