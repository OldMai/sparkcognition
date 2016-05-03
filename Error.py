  
# coding: utf-8

# In[6]:

import pandas as pd
import numpy as np
import glob

files = glob.glob('test/*.csv')
print files
k=' '
for j in files:
    print len(j)	
    if j.endswith('__weekday_out.csv'):
        k = j[5:-17]
    	frame1=pd.read_csv(j)
    	frame2=pd.read_csv('solution_'+str(k)+'.csv')
    	frame2.columns=['Air predicted','Dryer predicted','Furnace predicted','Light plugs predicted','Refrigerator predicted']
    	frame2['Timestamp']=frame1['Timestamp']
    	df2=pd.merge(frame1,frame2)
#    	print(df2)
#    	df=df2.drop(df2.columns[[0,6,7,8]],axis=1,inplace=True)
    	df=df2.drop(['Unnamed: 0','Timestamp','Total','weekday'], axis=1)
#    	print(df)
    	errormp=[]
    	mse=[]
    	rmse=[]
    	norm_error=[]
    	dev=[]
        mape=[]
    	appliance=['Air','Dryer', 'Furnace','Light plugs','Refrigerator']
   	# for i in range(len(df.columns)/2):
    	for words in appliance:
        	print(words)
        	i=words
            	nzdf=[df[i],df[str(i)+" predicted"]]
        	nzdf=pd.DataFrame(nzdf, columns='str(i)','str(i)+ predicted')
		print (type(nzdf))
		dev2=pd.DataFrame(np.array(df[i])-np.array(df[str(i)+" predicted"]))
        	e2=(np.sum(np.array(dev2)**2))/len(dev2)
        	rms=e2**0.5
        	ne=(np.sum(np.absolute(np.array(dev2))))/np.sum(np.array(df[i]))
              	devabs=pd.DataFrame(np.array(nzdf[i])-np.array(nzdf[str(i)+" predicted"]))
            	ma=(np.sum(np.absolute(np.array(devabs))/np.array(nzdf[i])))*100
        	mse.append(e2)
        	rmse.append(rms)        
        	norm_error.append(ne)
            	mape.append(ma)
    	errormp=[mse,rmse,norm_error,mape]
    	errormp=pd.DataFrame(errormp) 
    	errormp.to_csv('error_'+str(k)+'.csv', mode='a', index = False, index_label = False, header=False)
