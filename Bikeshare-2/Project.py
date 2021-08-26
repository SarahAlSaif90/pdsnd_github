# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:46:58 2021

@author: Alsai
"""

import time
import pandas as pd
import numpy as np


df = pd.read_csv("chicago.csv")

#1 Popular times of travel
print("------#1 Popular times of travel:-------\n")


# most common month
df['Start Time'] = pd.to_datetime(df['Start Time'])

df['month'] = df['Start Time'].dt.month

popular_month = df['month'].mode()[0]

#most common day of week
df['day'] = df['Start Time'].dt.day

popular_day = df['day'].mode()[0]

#most common hour of day
df['hour'] = df['Start Time'].dt.hour

popular_hour = df['hour'].mode()[0]


print('1)Most common month of travel:', popular_month)
print('2)Most common day of travel:', popular_day)
print('3)Most common hour of travel:', popular_hour)


#2 Popular stations and trip
print("\n------#2 Popular stations and trip:------\n")

 #most common start station
#start_station = df['Start Station'].value_counts()

#x=max(df['Start Station'],key=df['Start Station'].count)

#print(x,"occurs ",max_occ(df['Start Station'],x),"times")


#print("1)Most common start station:",start_station)

##most common end station
#End_station = df['End Station'].value_counts()
#print("2)Most common End station:",End_station)



 
 

