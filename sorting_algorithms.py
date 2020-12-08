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