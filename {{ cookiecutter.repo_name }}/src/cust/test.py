# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:34:41 2019

@author: RemyLagrois
"""
import pandas as pd
import numpy as np
from sklearn.externals import joblib


def test():
    print("it works")
    
def test2():
    print('auto works')
    
def save_model(path, model):
    if path[0] == '.' or path[0] == 'r':
        fp = path
    elif '\\' in path or '/' in path:
        fp = path
    else:
        print('Please add r to the left of the first quotation mark on path and reenter')
        return
    
    joblib.dump(model, fp)
    
    
def available():
    print('test() - tests for proper importing')
    print('save_model(path, model) - saves .pkl of model. Be sure to add filename.pkl to path')