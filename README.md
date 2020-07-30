# Project Name
[Analyzing the Weekly S&P Stock Market Data using Logistic Regression](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/FINAL_REPORT.pdf)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Tasks completed](#tasks-completed)
* [Sources](#sources)

## General info
This project is a part fulfillment of the requirement for CMSC 6950 (Computer Tools and Applications). The main focus of the project is to analyze the Weekly S &P Stock Market Data using logistic regression. 

## Technologies
Project is created with:
* Python version: 3.8.2
* GNU nano version: 4.8
* Jupyter-Notebook version: 6.0.3
* Pip version: 20.0.2

## Setup
### Installation
To run this project, install it locally using pip:

```
$ pip install pandas
$ pip install numpy
$ pip install matplotlib
$ pip install wget 
$ pip install statsmodels
$ pip install pingouin
$ pip install pycm
$ pip install seaborn

```
### Python Packages
* Pandas
* Numpy
* Seaborn	
* Pingouin
* Matplotlib
* PyCm
* Wget
* Csv

### Repository
* Master: code, test
* Github page: [data](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/dataset-95529.csv), [analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/analysis), [report](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/report), [plots](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/plots), [jupyter](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/jupyter), [final report](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/FINAL_REPORT.pdf)

### Create the local repository

```
$ cd desktop
$ mkdir folderName
$ git init
$ git remote add origin https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data
$ git pull
```
### Create your branch

* git branch branch_name

```
Run
#To call the Makefile and execute all.
$make
#To removing all the downloaded data and complied files
$make clean
To run the test case. If there is no reply, that means success.
$make test
#To generate files by file name (Ex. report.pdf).
$make report.pdf
```

## Tasks completed

### Tasks

#### First task: Analyzing first with jupyter-notebook

* Download [data](https://www.picostat.com/dataset/r-dataset-package-islr-weekly)

```
$wget.download("https://www.picostat.com/system/files/datasets/dataset-95529.csv")
```
* Check the structure of data

```
$weekly = pd.read_csv('dataset-95529.csv')
$weekly.head()
```
* Check the data description

```
$weekly.describe()
```
* Check for normality of variables of data [(pingouin package)](https://doi.org/10.21105/joss.01026)

```
$pg.normality (weekly)
```
* Plot the data (seaborn and matplotlib)
```
$sns_plot = sns.pairplot(weekly, hue = "Direction");
```
* Plot the correlated data (matplotlib)

```
$fig = plt.figure(figsize = (10, 8))
$ax = plt.axes()
$ax.scatter(x = weekly.index, y = weekly["Volume"], alpha = 0.5)
$ax.set(xlabel='Year', ylabel='Volume', title='Scatter Plot of Volume and Year')
$ax.grid()
```
* Verify correlated data [(pingouin package)](https://doi.org/10.21105/joss.01026)

```
$pg.corr(weekly["Year"], weekly["Volume"])
```
* Build the three models [(pingouin package)](https://doi.org/10.21105/joss.01026)

```
#Full model
$endog = (weekly["Direction"] == "Up").astype("int64")
$exog = sm.add_constant(weekly.drop(columns = ["Direction", "Year", "Today"]))
$logit_full = pg.logistic_regression(exog, endog)
$logit_full.round(4)

#Reduced model
$logit_one = pg.logistic_regression(weekly['Lag2'], endog)
$logit_one.round(4)

#Interaction model
$logit_int = pg.logistic_regression(weekly['Lag1'] * weekly['Lag2'], endog)
$logit_int.round(4)
```
* Verify the three models results (statsmodels package)

```
#Full model
$logit_stat_full = sm.Logit(endog, exog)
$logit_stat_res_full = logit_stat_full.fit()
$print(logit_stat_res_full.summary())

#Reduced model
$logit_stat_one = sm.Logit(endog, sm.add_constant(weekly['Lag2']))
$logit_stat_res_one = logit_stat_one.fit()
$print(logit_stat_res_one.summary())

#Interaction model
$logit_stat_int = sm.Logit(endog, sm.add_constant(weekly['Lag1'] * weekly['Lag2']))
$logit_stat_res_int = logit_stat_int.fit()
$print(logit_stat_res_int.summary())
```
* Build confusion matrix for three models (statsmodel package)

```
#Full model
$matrix_full = pd.DataFrame(logit_stat_res_full.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])

#Reduced model
$matrix_one = pd.DataFrame(logit_stat_res_one.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])

#Interaction model
$matrix_int = pd.DataFrame(logit_stat_res_int.pred_table(), columns = ["Down", "Up"], index = ["Down", "Up"])
```
* Analyze confusion matrix for three models [(PyCM package)](https://doi.org/10.21105/joss.00729)

```
$cm_full = ConfusionMatrix(matrix={"Class1": {"Class1": 54, "Class2":430}, "Class2": {"Class1": 48, "Class2": 557}}) 
$cm_one = ConfusionMatrix(matrix={"Class1": {"Class1": 33, "Class2":451}, "Class2": {"Class1": 26, "Class2": 579}}) 
$cm_int = ConfusionMatrix(matrix={"Class1": {"Class1": 4, "Class2":480}, "Class2": {"Class1": 3, "Class2": 603}}) 
```


        
#### Second task: Use version control (git) and collaboration tools(GitHub) for the project

* Re-run all earlier [jupyter analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/jupyter/Analysis_on_Jupyter.ipynb) on (python3 on shell)
* Create python files for all [plots](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/plots) and [analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/analysis) (.py) 
* Create a [LaTeX report](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/report/report.tex) summarizing the results of your project (nano and pdflatex)
* Implement our entire workflow as a [Makefile](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/report/Makefile) and project is reproducible.
* Create a [README.md file](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/README.md) to explain how to use/build your project.

## Sources

### Data 

* You may download the data used for the project [here](https://www.picostat.com/dataset/r-dataset-package-islr-weekly)

### Software 

* [Vallat, R. (2018). Pingouin: statistics in Python. Journal of Open Source Software](https://doi.org/10.21105/joss.01026)
* [Haghighi et al., (2018). PyCM: Multiclass confusion matrix library in Python. Journal of Open Source Software](https://doi.org/10.21105/joss.00729)
