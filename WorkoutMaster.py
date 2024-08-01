#!/usr/bin/python
#coding=utf-8

import pandas as pd
import random
#import plt.matplotlib as plt

Excercises = pd.DataFrame( {'Push':['Push-up','Dip','O cazz'],
              'Pull':['Pull-up','Chin-up','O cazz'],
              'Legs':['Squat','Bulgarian Split Squat','Romanian Leg Row']
              }
                         )

Push = ['Elevated Push-ups','Wide Push-ups','Diamond Push-ups','Pike Push-ups','Dips']   
Pull = ['Wide Pull-ups','Narrow Pull-ups','Chin-ups','Front Rows']      
Legs = ['Squats','Bulgarian Split Squats','Calves Raises']   
Fatti=[]

Ex = [['Declined Push-ups','Wide Push-ups','Diamond Push-ups','Pike Push-ups','Dips'], ['Wide Pull-ups','Narrow Pull-ups','Chin-ups','Front Rows'] ,['Squats','Bulgarian Split Squats','Romanian Leg Rows']]

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

#GenerateTodaysWorkout(Push)

def InsertTodaysWorkout():
  loop = True
  ok1 = True
  ok2 = True
  while loop: 
    row = []
    while ok1:
      print("Select category:")
      print("1. Push\n2. Pull\n3. Legs\n")
      cat = int(input())
      if cat < 4:
        ok1 = False
      else:
        print("Invalid Input, retry\n")
    while ok2:
      print("Select exercise:")
      print(Ex[cat-1])
      e = int(input())
      if e < len(Ex[cat-1])+1:
        ok2 = False
      else:
        print("Invalid Input, retry\n")
    row.append(Ex[cat][e-1])
    print("Insert number of sets:")
    sets = int(input())    
    row.append(sets)
    print("Insert number of reps:")
    reps = int(input())
    row.append(reps)

    print("\nFinito?")
    loop = bool(input('Press any key to continue or just press Enter to finish'))    
    
    print(row)
# How to insert row pandas dataframe
    
InsertTodaysWorkout()


#print(len(Push))

