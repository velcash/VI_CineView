#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
'''This class is used to load and filter data'''
class DataFilter:
    path = 'VI_CineView/Data'
    def __init__(self, path):
        self.path = path
        
    def load_BOdata(self,file):
        df = pd.read_csv(self.path +'/'+ file, sep = ';')
        return df
    #load data about Oscar
    def load_oscarData(self, file):
        df = pd.read_csv(self.path +'/'+ file,sep = ';')
        return df
    #Load dataabout palme d'or
    def load_palmeData(self,file):
        palmeDF = pd.read_csv(self.path +'/'+ file,sep = ';',engine='python',encoding='ISO-8859-1')
        return palmeDF
    
        #To select BOdata from one year
    def select_boxOfficemovieFrom(self,df,from_year):
        '''Require a value of year from which we select data'''
        data = df.copy().loc[(df['release_date'] >= from_year)]
        return data
    
    #select BOdata from at one year
    def select_boxOfficemovieOn(self,df, year):
        '''Require a value of year on which we select data'''
        data = df.copy().loc[(df['release_date'] == year)]
        return data  

    def selectTopBudgetOfBox(self,df,number):
        '''Sort relation of budget and revenue for top  boxOffice movie, receive the number of views as arguments'''
        data = df.sort_values(['revenue'],ascending=[False])
        dx=data.head(number)
        return dx

    def sortMovieByBudget(self,df,criteria, number):
        if criteria =="ascending":
            data = df[['title','budget', 'revenue' ]].sort_values(['budget'],ascending=[True])
        if criteria =="descending":
            data = df[['title','budget','revenue' ]].sort_values(['budget'],ascending=[False])
        dx=data.head(number)
        return dx
    

    


# In[ ]:





# In[ ]:




