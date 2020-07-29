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

#One Predictor model Logistic Regression using pinguoin#
logit_one = pg.logistic_regression(weekly['Lag2'], endog)
logit_one.round(4)

#verifying results by pingouin
#Statsmodel library with one model#
#use of Statsmodels for Confusion Matrix#
logit_stat_one = sm.Logit(endog, sm.add_constant(weekly['Lag2']))
logit_stat_res_one = logit_stat_one.fit()

#Confusion matrix calculation#
matrix_one = pd.DataFrame(logit_stat_res_one.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])
#Plotting Confusion matrix#
fig, ax = plt.subplots()
sns.heatmap(matrix_one, annot = True, cbar = False, ax = ax, fmt = "g", square = True, annot_kws = {"fontsize": "x-large"})
ax.set(xlabel = "predicted label", ylabel = "true label");
ax.figure.savefig('onemodel.png')

#Confusion matrix examination using PyCM#
from pycm import *
cm_one = ConfusionMatrix(matrix={"Class1": {"Class1": 33, "Class2":451}, "Class2": {"Class1": 26, "Class2": 579}})
# Create CM Directly
#Class1=True, Class2=Predicted
print(cm_one)
