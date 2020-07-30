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
* Github page: [data](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/dataset-95529.csv), [analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/analysis), [report](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/report), [plots](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/plots), [jupyter](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/jupyter), FINAL REPORT

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

* Download [data](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/dataset-95529.csv)
* Check the structure of data
* Check the data description
* Check for normality of variables of data [(pingouin package)](https://doi.org/10.21105/joss.01026)
* Plot the data (seaborn and matplotlib)
* Plot the correlated data (matplotlib)
* Verify correlated data [(pingouin package)](https://doi.org/10.21105/joss.01026)
* Build the three models [(pingouin package)](https://doi.org/10.21105/joss.01026)
* Verify the three models results (statsmodels package)
* Build confusion matrix for three models (statsmodel package)
* Analyze confusion matrix for three models [(PyCM package)](https://doi.org/10.21105/joss.00729)
        
#### Second task: Use version control (git) and collaboration tools(GitHub) for the project

* Re-run all earlier [jupyter analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/blob/master/jupyter/Analysis_on_Jupyter.ipynb) on (python3 on shell)
* Create python files for all [plots](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/plots) and [analysis](https://github.com/knowusuboaky/CMSC6950_Analyzing_Weekly_Stock_Market_Data/tree/master/analysis) (.py) 
* Create a LaTeX report summarizing the results of your project (nano and pdflatex)
* Implement our entire workflow as a Makefile and project is reproducible.
* Create a Readme.md file to explain how to use/build your project.

## Sources

### Data 

* You may download the data used for the project [here](https://www.picostat.com/dataset/r-dataset-package-islr-weekly)

### Software 

* [Vallat, R. (2018). Pingouin: statistics in Python. Journal of Open Source Software](https://doi.org/10.21105/joss.01026)
* [Haghighi et al., (2018). PyCM: Multiclass confusion matrix library in Python. Journal of Open Source Software](https://doi.org/10.21105/joss.00729)
