# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 08:28:06 2017

@author: LCrecraft
"""
"""
csv reader will take a BCSI csv document, plot it and use the standard 
calculations that are used in most situations. 

"""
import csv
import pandas as pd


def main ():   
    
    #make dataFrame with relevent info from file
    dataF = getData()
    
    frConst = 0
    fpConst = 0
    
    rpMut = calcRP(dataF)

def getData ():
    file = tk.askopenfile(tk.askdirectory())
    '''d = {'FR' : pd.Series([], date=[]), 'FP' : pd.Series([], date=[]),
          'RP' : pd.Series([], date=[]), 'PH' : pd.Series([], date=[]),
          'TestID' : pd.Series([], date=[]), 'SN' : pd.Series([], date=[]),
           'Name': pd.Series([], date=[])}'''
    # populate d from csv
    d = pd.read_csv(file) # fill out parameters

    return d
    
def calcRP (data):
    rp = data.pop()
    
 
def calcPH (data):
        
    
main()