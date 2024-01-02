#Import the necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as st
%matplotlib inline

#Reading the dataset; with utf-8 encoding
data = pd.read_csv('big_mart_sales.csv',encoding='utf-8')

#Dimensions of the dataset
data.shape

#Info on the dataset
data.info()

#Checking for null values
data.isna().sum()

#Filling the null values
med_IW = st.median(data['Item_Weight'])
data['Item_Weight'] = data['Item_Weight'].fillna(med_IW)

mode = st.mode(data.Outlet_Size)
data['Outlet_Size'] = data['Outlet_Size'].fillna(mode)

#Visulaizing a Continous variable
plt.figure(figsize=(12,7))
sns.histplot(data.Item_Outlet_Sales, bins = 25, color = 'yellow')
plt.xlabel("Item_Outlet_Sales")
plt.ylabel("Number of Sales")
plt.title("Item_Outlet_Sales Distribution")

#Visulaizing a Categorical variable
plt.title('Item Outlet Size')
data['Item_Outlet_Size'].value_counts().plot(kind = 'bar', color = 'red')
plt.show()
