# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:54:07 2024

@author: robin

Develop a package that can be configured to run once per week to automate my
timesheets.
- First define a format for tickets / ODT / ODXT / BFM... that are used
- It should pull my time tracing from outlook
- It should look things up on Jira and determine which code the ticket sits in
- It should export an excel or csv that can be copied into myob / connect
to MYOB via API to submit a timesheet.
"""

import queryOutlook.getCalendar as gc
import dataFormat.extractCalendarData as ecd
import dataFormat.getCalDataFrame as gcd
import dataFormat.organiseDataFrame as odf
import datetime as dt

#Then turn that dictioanary into a dataframe, index it properly, and output
#to csv / excel file.
#initial: Today - 6
#final: Today + 1
def calToCsv():
    cal = gc.getCalendar(dt.datetime.today().date() - dt.timedelta(6),\
                             dt.datetime.today().date() + dt.timedelta(1))
    
    q = ecd.createDictFromCal(cal)
    b = gcd.getCalDataFrame(q)
    
    c = odf.organiseDataFrame(b)
    
    c.to_csv('timesheetEntries.csv')


if __name__ == '__main__':
    #cal = gc.getCalendar(dt.datetime(2024,10,31), dt.datetime(2024,6,11))
    #cal = gc.getCalendar(dt.datetime(year=2024,month=10,day=31),\
    #                     dt.datetime(year=2024,month=11,day=6))
                         
    #q = ecd.createDictFromCal(cal)
    #b = gcd.getCalDataFrame(q)
    
    #c = odf.organiseDataFrame(b)
    
    calToCsv()
    
    
    