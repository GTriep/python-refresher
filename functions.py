#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:28:51 2026

@author: triep
"""
import numpy as np

def fahrenheit_to_celcius(temp_f):
    temp_c = (temp_f-32)/1.8
    return temp_c
T_1 = fahrenheit_to_celcius(32)
T_2 = fahrenheit_to_celcius(212)
print (T_1, T_2)

def stats (data):
    """ return the mean, minimum and maximum of a sequence"""
    return np.mean(data), min(data), max(data)

mean, minimum, maximum = stats([4.2, 7.1, 2.9, 8.5, 5.0])
print (mean, minimum, maximum)

def leap_year(year):
    """returns 'True' when the year given is a leap year, otherwise it returns false"""
    if year % 4 != 0:
        return False
    elif year % 100 != 0 :
        return True
    elif year % 400 == 0:
        return True 
    else:
        return False 
    
print (leap_year(2000))
print (leap_year (1900))
print (leap_year (2024))