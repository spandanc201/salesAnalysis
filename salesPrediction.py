import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
import sqlite3
import pandas as pd

df = pd.read_csv('train.csv')
conn = sqlite3.connect('demo.db')

