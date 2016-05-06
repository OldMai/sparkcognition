
# coding: utf-8

import pandas as pd
import os
import operator
from collections import Counter


# This function fetches the most frequent season if the data is for three months.
# It takes the DataFrame from append_appliances function as an argument
def get_season(DataFrame):
    df = DataFrame

    #first we check if the number of unique month-year pairs is higher than specified number, 3 
    NUMBER_OF_MONTHS = 3
    month_and_year = df['localminute'].str[0:7]
    
    #We print unique month-year pairs to make sure what files we have from timestamps perspective
    print(month_and_year.unique())
    print(len(month_and_year.unique()))
    if len(month_and_year.unique()) > NUMBER_OF_MONTHS :
        most_frequent_season = "Over three months"
        return most_frequent_season      
       
    # Now we specify seasons as sums of true values at corresponding months
    winter = sum(df['localminute'].str[5:7].isin(['12', '1', '2']))
    spring = sum(df['localminute'].str[5:7].isin(['03', '04', '05']))
    summer = sum(df['localminute'].str[5:7].isin(['06', '07', '08']))
    autumn = sum(df['localminute'].str[5:7].isin(['09', '10', '11']))
    
    # Finally we look for season with maximum entries and return it   
    max_count = max(autumn, winter, summer, spring)
     
    if max_count == winter:
        most_frequent_season = "Winter"
    elif max_count == autumn:
        most_frequent_season = "Autumn"
    elif max_count == summer:
        most_frequent_season = "Summer"
    elif max_count == spring:
        most_frequent_season = "Spring"         
    
    return most_frequent_season     
  

#This function creates a DataFrame for other functions appending columns with similar appliencies, e.g. air1 and air2
#It takes the path to the cvs file as an argument
def append_appliances(path):
    df = pd.read_csv(path)
    
    df['air'] = df['air1'] + df['air2'] +df['air3'] + df['airwindowunit1']
    df.drop(['air1','air2','air3', 'airwindowunit1'],inplace=True,axis=1,errors='ignore')
    
    df['aquarium'] = df['aquarium1']
    df.drop(['aquarium1'],inplace=True,axis=1,errors='ignore')
    df['bathroom'] = df['bathroom1'] + df['bathroom2']
    df.drop(['bathroom1','bathroom2'],inplace=True,axis=1,errors='ignore')
    df['bedroom'] = df['bedroom1'] + df['bedroom2'] + df['bedroom3'] + df['bedroom4'] + df['bedroom5']
    df.drop(['bedroom1','bedroom2', 'bedroom3', 'bedroom4', 'bedroom5'],inplace=True,axis=1,errors='ignore')
    df['car'] = df['car1']
    df.drop(['car1'],inplace=True,axis=1,errors='ignore')
    df['clotheswasher'] = df['clotheswasher1'] + df['clotheswasher_dryg1']
    df.drop(['clotheswasher1', 'clotheswasher_dryg1'],inplace=True,axis=1,errors='ignore')
      
    df['diningroom'] = df['diningroom1'] + df['diningroom2']
    df.drop(['diningroom1','diningroom2'],inplace=True,axis=1,errors='ignore')
    df['dishwasher'] = df['dishwasher1']
    df.drop(['dishwasher1'],inplace=True,axis=1,errors='ignore')
    df['disposal'] = df['disposal1']
    df.drop(['disposal1'],inplace=True,axis=1,errors='ignore')
    df['dryer'] = df['drye1'] + df['dryg1']
    df.drop(['drye1', 'dryg1'],inplace=True,axis=1,errors='ignore')
    
    df['freezer'] = df['freezer1']
    df.drop(['freezer1'],inplace=True,axis=1,errors='ignore')
    df['furnace'] = df['furnace1'] + df['furnace2']
    df.drop(['furnace1','furnace2'],inplace=True,axis=1,errors='ignore')
    df['garage'] = df['garage1'] + df['garage2']
    df.drop(['garage1','garage2'],inplace=True,axis=1,errors='ignore')
    df['heater'] = df['heater1']
    df.drop(['heater1'],inplace=True,axis=1,errors='ignore')
    df['housefan'] = df['housefan1']
    df.drop(['housefan1'],inplace=True,axis=1,errors='ignore')
    df['icemaker'] = df['icemaker1']
    df.drop(['icemaker1'],inplace=True,axis=1,errors='ignore')
    df['jacuzzi'] = df['jacuzzi1']
    df.drop(['jacuzzi1'],inplace=True,axis=1,errors='ignore')
    df['kitchen'] = df['kitchen1'] + df['kitchen2']
    df.drop(['kitchen1','kitchen2'],inplace=True,axis=1,errors='ignore')
    df['kitchenapp'] = df['kitchenapp1'] + df['kitchenapp2']
    df.drop(['kitchenapp1','kitchenapp2'],inplace=True,axis=1,errors='ignore')
    df['lights_plugs'] = df['lights_plugs1'] + df['lights_plugs2'] + df['lights_plugs3'] + df['lights_plugs4'] + df['lights_plugs5'] + df['lights_plugs6']
    df.drop(['lights_plugs1','lights_plugs2', 'lights_plugs3', 'lights_plugs4', 'lights_plugs5', 'lights_plugs6'],inplace=True,axis=1,errors='ignore')
    df['livingroom'] = df['livingroom1'] + df['livingroom2']
    df.drop(['livingroom1','livingroom2'],inplace=True,axis=1,errors='ignore')
    df['microwave'] = df['microwave1']
    df.drop(['microwave1'],inplace=True,axis=1,errors='ignore')
    df['office'] = df['office1']
    df.drop(['office1'],inplace=True,axis=1,errors='ignore')
    df['outsidelights_plugs'] = df['outsidelights_plugs1'] + df['outsidelights_plugs2']
    df.drop(['outsidelights_plugs1','outsidelights_plugs2'],inplace=True,axis=1,errors='ignore')
    df['oven'] = df['oven1'] + df['oven2']
    df.drop(['oven1','oven2'],inplace=True,axis=1,errors='ignore')
    df['pool'] = df['pool1'] + df['pool2'] + df['poollight1'] + df['poolpump1']
    df.drop(['pool1','pool2', 'poollight1', 'poolpump1'],inplace=True,axis=1,errors='ignore')
    df['pump'] = df['pump1']
    df.drop(['pump1'],inplace=True,axis=1,errors='ignore')
    df['range'] = df['range1']
    df.drop(['range1'],inplace=True,axis=1,errors='ignore')
    df['refrigerator'] = df['refrigerator1'] + df['refrigerator2']
    df.drop(['refrigerator1','refrigerator2'],inplace=True,axis=1,errors='ignore')
    df['security'] = df['security1']
    df.drop(['security1'],inplace=True,axis=1,errors='ignore')
    df['shed'] = df['shed1']
    df.drop(['shed1'],inplace=True,axis=1,errors='ignore')
    df['sprinkler'] = df['sprinkler1']
    df.drop(['sprinkler1'],inplace=True,axis=1,errors='ignore')
    df['unknown'] = df['unknown1'] + df['unknown2'] + df['unknown3'] + df['unknown4']
    df.drop(['unknown1','unknown2', 'unknown3', 'unknown4'],inplace=True,axis=1,errors='ignore')
    df['utilityroom'] = df['utilityroom1']
    df.drop(['utilityroom1'],inplace=True,axis=1,errors='ignore')
    df['venthood'] = df['venthood1']
    df.drop(['venthood1'],inplace=True,axis=1,errors='ignore')
    df['waterheater'] = df['waterheater1'] + df['waterheater2']
    df.drop(['waterheater1','waterheater2'],inplace=True,axis=1,errors='ignore')
    df['winecooler'] = df['winecooler1']
    df.drop(['winecooler1'],inplace=True,axis=1,errors='ignore')
    
    return df


# In[196]:

#This function returns the list of 5 top-used appliencies for each homeID
def find_top_appliencies(DataFrame):
    df = DataFrame
    
    # First, we make sure to account for only summer data if it is a two-year file  
    df0 = df[df['localminute'].str[5:7].isin(['06', '07', '08'])]
    
    # We need to start with column 4 of the cvs
    df1 = df0.ix[:,4:]
    
    # We create a dictionary with applience as key and total usage as value, then we sort by value.
    my_dict = dict()    
    for column in df1:
        my_dict[column] = df1[column].sum()
        
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse = True)
    
    NUMBER_OF_TOP = 5;
    sorted_dict5 = sorted_dict[:NUMBER_OF_TOP]
    
    #To have our output as list with appliencies and home_id as its first element
    my_list = list()
    #my_list.extend(df['dataid'].unique())
    for item in sorted_dict5:
        my_list.append(item[0])
    
    return my_list


# In[199]:

# This is our main method. We iterate over each cvs file in our directory. We make sure to iterate only over .cvs files
# We then print each file's ID with its most frequent seoson or "Over three months" string if it is for more than three months
# We then make sure that we find top-5 appliencies only for Summer files in case of three months or two-year files as 
# they will contain summer too. 
def get_top_list (path):
    my_list = list()
    for doc in os.listdir(path):
        if doc.endswith(".csv"):

            season = get_season(append_appliances(os.path.join(path, doc)))
            print(doc + " " + season)
            if season == "Summer" or season == "Over three months":
                top_list = find_top_appliencies(append_appliances(os.path.join(path, doc)))
                print top_list
                my_list.extend(top_list)


    mcommon= [ite for ite, it in Counter(my_list).most_common(5)]
    return mcommon
            


# In[219]:

def aggregate (path):
    top5 = get_top_list(path)
    print "top5 list: ", top5
    output_path = os.path.join(path, "output")
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    for doc in os.listdir(path):
        if doc.endswith(".csv"):
            print "processing ", doc
            df = append_appliances(path + doc)
            
            df1 = df[['localminute'] + top5]
            df1.to_csv(os.path.join(output_path, doc.split('.')[0]+"_out.csv"))
            
    
    


# In[220]:

aggregate('/home/minbaev/Downloads/SC/')


# In[ ]:




# In[ ]:



