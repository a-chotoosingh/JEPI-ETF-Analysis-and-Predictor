import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from datetime import datetime

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings

warnings.filterwarnings('ignore')


#Import ETF data
jp_etf_df = pd.read_csv('C:/Users/achot/Downloads/JPMorgan Equity Premium Income ETF (JEPI).csv')
spy_df = pd.read_csv("C:/Users/achot/Downloads/SPY (1).csv")
#Check data
spy_df

#Covert Date column to datatime type
jp_etf_df['Date'] = pd.to_datetime(jp_etf_df['Date'], utc=True, infer_datetime_format = True)
jp_etf_df['Date2'] = jp_etf_df['Date'].dt.strftime('%m/%d/%y')


#Create basic plots
x = jp_etf_df['Date']
y = jp_etf_df['Close']
plt.plot(x, y)

#Plot SP500
spy_df['Date'] = pd.to_datetime(spy_df['Date'], utc=True, infer_datetime_format = True)
spy_df['Date2'] = spy_df['Date'].dt.strftime('%m/%d/%y')
spy_x = spy_df['Date']
spy_y = spy_df['Close']
plt.plot(spy_x,spy_y)

#Get SPY time frame that matches JP Morgan ETF data
start_time = jp_etf_df['Date2'][0]
end_time = jp_etf_df['Date2'][671]

time = (spy_df['Date'] >= start_time) & (spy_df['Date'] <= end_time)
spy_jp_timeframe = pd.DataFrame(spy_df.loc[time])
spy_jp_timeframe

#Create Label columns for each dataframe
jp_etf_df['Label'] = 'JP Morgan ETF'
spy_jp_timeframe['Label'] = 'SP500'

#Merge dataframes to begin plotting comparisons
jp_etf_spy_df = pd.merge(jp_etf_df[['Close', 'Adj Close', 'Volume', 'Date2']], spy_jp_timeframe, how = 'left', on = 'Date2')
jp_etf_spy_df = jp_etf_spy_df.drop(['Date'], axis=1)
jp_spy_ret_df = pd.DataFrame()
jp_spy_ret_df['JP Ret'] = jp_etf_spy_df['Close_x'].pct_change()
jp_spy_ret_df['SPY Ret'] = jp_etf_spy_df['Close_y'].pct_change()
jp_spy_ret_df = jp_spy_ret_df.dropna()
jp_spy_ret_df['Date'] = pd.to_datetime(jp_etf_spy_df['Date2'], format = '%m/%d/%y')
#Output summary statics
jp_spy_ret_df.describe()

#Plot the adjsuted close for the JP Morgan ETF and SPY500
plt.plot(jp_spy_ret_df['Date'], jp_spy_ret_df['JP Ret'], label='JP Morgan ETF')
plt.plot(jp_spy_ret_df['Date'], jp_spy_ret_df['SPY Ret'],alpha = 0.3, label='SPY 500')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.show()

#Plot barplot of returns to compare means
sns.barplot(data = jp_spy_ret_df )

