# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:43:49 2024

@author: robin

take the calender extract and create dataframe from it
"""

import config as GBL
import pandas as pd

def getCalDataFrame(calendarDict):
 
    result = pd.DataFrame.from_dict(data = calendarDict, orient='index')
    result.columns = ['startTime','endTime','timeCode','ticketCode','desc']

    
    if GBL.DEBUG == 1:
        #print(calendarDict)
        print(result)
        
    
    
    return result

