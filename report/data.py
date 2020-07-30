import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wget
url = "https://www.picostat.com/system/files/datasets/dataset-95529.csv"
wget.download(url)
weekly = pd.read_csv('dataset-95529.csv')
