# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:02:10 2024

@author: robin
"""

import win32com.client # type: ignore

def getCalendar(begin,end):
    outlook = win32com.client.Dispatch('Outlook.Application').\
        GetNamespace('MAPI')
        
    calendar = outlook.getDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')
    
    #IT SEEMS LIKE THIS DEPENDS ON YOUR ACTUAL CALENDAR SETTING FOR YMD
    #IT WILL SILENTLY TRY TO FIX ERRORS IF THE MONTH ENTERED IS GREATER THAN 12
    restriction = "[Start] >= '" +\
        begin.strftime('%d/%m/%Y') + "' AND [END] <= '" + \
            end.strftime('%d/%m/%Y') + "'"
            
    calendar = calendar.Restrict(restriction)
    return calendar


