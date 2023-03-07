#!/usr/bin/python
#coding=utf-8

import pandas as pd
import random

Excercises = pd.DataFrame( {'Push':['Push-up','Dip','O cazz'],
              'Pull':['Pull-up','Chin-up','O cazz'],
              'Legs':['Squat','Bulgarian Split Squat','Romanian Leg Row']
              }
                         )

Push = ['Elevated Push-ups','Wide Push-ups','Diamond Push-ups','Pike Push-ups','Dips']   
Pull = ['Wide Pull-ups','Narrow Pull-ups','Chin-ups','Front Rows']      
Legs = ['Squats','Bulgarian Split Squats','Romanian Leg Rows']   
Fatti=[]


def GenerateTodaysWorkout(Push) :
    print("\nRimasti da Fare:")
    random.shuffle(Push)
    print(Push)
    print("Fatti:")
    print(Fatti)
    print("Da Fare Oggi:")
    a = Push.pop()
    print(a)
    Fatti.append(a)
    if  len(Push) == 0 :
      Push = Fatti.copy()
      Fatti.clear()
GenerateTodaysWorkout(Push)
GenerateTodaysWorkout(Push)

#print(len(Push))

