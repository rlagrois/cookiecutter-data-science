# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:34:41 2019

@author: RemyLagrois
"""

import operator
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
    
    print("Saving.....")
    joblib.dump(model, fp)
    print("Saved!")

def lab_wt(y):
    vals = {}
    if not isinstance(y, np.array):
        y = np.array(y)
    total = len(y)
    wts = {}
    # Get counts of values in y
    for i in y:
        if i in vals:
            vals[i] += 1
        else:
            vals[i] = 1
   
    # Find value with largest count
    key =  max(vals.items(), key=operator.itemgetter(1))[0]
    
    # Build dict with value weights
    for i in vals:
        wts[i] = vals[key] / vals[i] 
    
    # Build results list
    res = [wts[y[i]] for i in range(total)]

    
    return res
    
def rand_sample(df,labels=None,wt=None,n=1000,names=None):
    if labels is not None and wt is not None:
        print("Please pass only labels or weights!")
        print('Passing labels will generate weights automatically (balanced)')
        print("Use wt if you'd like custom weights")
        return
    
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
        if names is not None:
            df.columns = names

    elif labels is not None:
        weights = lab_wt(labels)
        smpl = df.sample(n=n,weights=weights)
        return smpl
    elif wt is not None:
        smpl = df.sample(n=n,weights=wt)
        return smpl
    else:
        smpl = df.sample(n=n)
        return smpl
        
    
def available():
    print('Avalable cust.func functions:')
    print('test() - tests for proper importing')
    print('save_model(path, model) - saves .pkl of model. Be sure to add filename.pkl to path')
    print("lab_wt(y): returns list of record weights using target column")
    print("rand_sample(df,labels=None,wt=None,n=1000,names=None): returns random sample from provided data")