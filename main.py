## Importing packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

sns.set_theme(style='whitegrid')

## Loading in the data
df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_Microcourse_Visualization/main/Data/Georgia_COVID/Georgia_COVID-19_Case_Data.csv')
df

## Information about the data
len(df)
df.shape
df.info()
list(df)
df['COUNTY'].value_counts()

df_counties = df['COUNTY'].value_counts()
df_counties.head(5)

