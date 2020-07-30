import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
weekly = pd.read_csv('dataset-95529.csv')
import seaborn as sns
sns_plot = sns.pairplot(weekly, hue = "Direction")
sns_plot.savefig("graphical_summary_of_data.png")
