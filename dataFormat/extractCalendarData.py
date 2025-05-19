# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:13:33 2024

@author: robin
"""

import re

debug = 0

#Body - text in the main body of the invite
#Location - location field
#Subject - main heading
#Start - start datetime
#End - finish datetime
def getTimeCode(entry):
    subject = entry.Subject
    
    if subject.startswith("Software and Data Systems Daily Standup"):
        subject = "[BEV Beta PhaseA] " + subject
    
    
    #Find what is inside square brackets
    regexResult = re.search(r"\[([A-Za-z0-9_ -]+)\]", subject)
    try:
        result = regexResult.group(1)
    except AttributeError:
        result = "None"
    return  result

def getTicketCode(entry):
    subject = entry.Subject
    
    #if BSW contained -> get the number after that
    regexResult = re.search(r'\bBSW-\w+', subject)
    
    try:
        result = regexResult.group(0)
    except AttributeError:
        result ="None"
    return result

def trimDescription(desc, timeCode, ticketCode):
    '''Run in createDictFromCal function after we have
    gotten the timecode and ticketcode
    '''
    
    #desc = desc.replace(ticketCode + ':','')
    desc = desc.replace('[' + timeCode + ']','')
    
    return desc.strip()

def getDate(entry):
    result = entry.Start.dt.tz_convert(None)
    return result

def getDayOfWeek(entry):
    #Do this once we have a dataframe and datetime index
    #return entry.Start.dt.dayofweek()
    pass



#Add to a dictionary with desired fields
def createDictFromCal(cal):
    '''
    Input: Calendar object from outlook
    
    Output: Dictionary organised with a field for
                - Timecode or Unknown
                - Jira ticket number or None
                - Description
                - Day of week
                - Date
                - Date time as initial index
                
    
    '''
    count = 0;
    entries = {}
    for en in cal:
        
        
        if debug == 1:
            print(f"The timecode is {timeCode}, the ticket is {ticketCode}: {desc}.")
            #print(initialIndex)
            #print(initialIndex[:-6])
            #print(pd.to_datetime(initialIndex,tz='None'))
        
        if not en.Subject.startswith("BREAK:"):
            
            initialIndex = str(en.Start)
            endTime = str(en.End)
            timeCode = getTimeCode(en)
            ticketCode = getTicketCode(en)
            #date = getDate(en)
            #day = getDayOfWeek(en)
            desc = trimDescription(en.Subject,timeCode,ticketCode)
        
        
            #if GBL.DEBUG == 1:
            #    print(f"The timecode is {timeCode}, the ticket is {ticketCode}: {desc}.")
            #    #print(initialIndex)
            #    #print(initialIndex[:-6])
            #    #print(pd.to_datetime(initialIndex,tz='None'))
                
            entries[count] = [initialIndex[:-6], endTime[:-6], timeCode, ticketCode, desc]
            
            count += 1
        
    return entries
        
        
