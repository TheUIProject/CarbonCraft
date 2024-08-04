#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv('CO2.csv')
print(data)


# In[2]:


data.transpose()


# In[3]:


new_df=data[['Engine Size(L)','Cylinders','Fuel Consumption Comb (L/100 km)','CO2 Emissions(g/km)']]
print(new_df.head())


# In[39]:


X=new_df.iloc[:,:3].values
y=new_df.iloc[:,-1:].values
print(y)


# In[105]:


import numpy as np
from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values=np.nan,strategy='mean')
imp.fit(X[:,:3])
X[:,:3]=imp.transform(X[:,:3])  # import numpy as np


# In[106]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


# In[126]:


from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_train,y_train)
reg.score(X_train,y_train)
import joblib
joblib.dump(reg, 'vemodel.pkl')


# In[120]:


y_pred=reg.predict(X_test)
print(y_pred)
print(X_test)


# In[121]:


from sklearn.metrics import r2_score
Accuracy=r2_score(y_test,y_pred)*100
print(" Accuracy of the model-R2 is %.2f" %Accuracy)


# In[122]:


new_data = np.array([[2.0,4.0,8.5]])


# In[123]:


new_prediction =reg.predict(new_data)


# In[124]:


print(f"Prediction for new data: {new_prediction}")


# In[ ]:




