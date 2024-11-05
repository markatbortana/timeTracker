# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:37:56 2024

@author: robin
"""
import pandas as pd

def organiseDataFrame(df):
    
    '''Take the dataframe with the extra columns and collapse it into
    subject/ticket/timeCode matches with the hours added up'''
    
    #Need a multi-index dataframe of Subject-Timecode-Ticketcode
    #then just sum?
    
    #b = df
    
    #Get the right formats for things
    df['startTime'] = pd.to_datetime(df['startTime'])
    df['endTime'] = pd.to_datetime(df['endTime'])
    df['duration'] = (df['endTime'] - df['startTime'])
    
    #Convert to hrs
    df['duration_hrs'] = df['duration'].apply(lambda x: x.total_seconds() / 3600.0)
    
    #Pull the date
    df['date'] = df['endTime'].apply(lambda x: x.date())
    
    #Lookup for days of week, dayofweek output is 0-6
    daysOfWeek = {0:'Monday',
                  1:'Tuesday',
                  2:'Wednesday',
                  3:'Thursday',
                  4:'Friday',
                  5:'Saturday',
                  6:'Sunday'}
    df['day'] = df['endTime'].apply(lambda x: daysOfWeek[x.dayofweek])
    
    #Don't need duration after this
    df.drop(['duration'],axis=1,inplace=True)
    
    #Organise so can get hours per day (date, day) so can run over two weeks
    qq = df.pivot(index=['desc','startTime','endTime','timeCode','ticketCode'],columns=['date','day'])
    
    #Sum the duration_hrs across each day
    result = qq.groupby(['timeCode', 'ticketCode', 'desc']).sum()
    
    return result
                            