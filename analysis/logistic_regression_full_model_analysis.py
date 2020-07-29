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

#Full model Logistic Regression using pinguoin#
logit_full = pg.logistic_regression(exog, endog)
logit_full.round(4)

#verifying results by pingouin
#Statsmodel library with full model#
import statsmodels.api as sm
import statsmodels.formula.api as smf

#use of Statsmodels for Confusion Matrix#
logit_stat_full = sm.Logit(endog, exog)
logit_stat_res_full = logit_stat_full.fit()

#Confusion matrix calculation#
matrix_full = pd.DataFrame(logit_stat_res_full.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])

#Plotting Confusion matrix#
fig, ax = plt.subplots()
sns.heatmap(matrix_full, annot = True, cbar = False, ax = ax, fmt = "g", square = True, annot_kws = {"fontsize": "x-large"})
ax.set(xlabel = "predicted label", ylabel = "true label");
ax.figure.savefig('fullmodel.png')


#Confusion matrix examination using PyCM#
from pycm import *
cm_full = ConfusionMatrix(matrix={"Class1": {"Class1": 54, "Class2":430}, "Class2": {"Class1": 48, "Class2": 557}})
# Create CM Directly
#Class1=True, Class2=Predicted
print(cm_full)
