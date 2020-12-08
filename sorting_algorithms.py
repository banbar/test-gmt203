# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:47:01 2020

@author: banbar
"""

def selection_sort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        # Finds the smallest in the remaining items (i -> end)
        for j in range(i+1, n):
            if(theSeq[j] < theSeq[smallNdx]):
                smallNdx = j
        # SWAP operation - swaps the value at i with the smallest remaining value
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
        
        print(theSeq)
    
    return theSeq

def selection_sort_v2(theSeq):
    n = len(theSeq)
    for i in range(n-1, 0, -1):
        highNdx = i
        # Finds the highest in the remaining items (i -> end)
        for j in range(i):
            if(theSeq[j] > theSeq[highNdx]):
                highNdx = j
        # SWAP operation - swaps the value at i with the smallest remaining value
        if highNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[highNdx]
            theSeq[highNdx] = tmp
        
        print(theSeq)
    
    return theSeq