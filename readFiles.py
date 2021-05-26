#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def readFiles(folderpath):
    """
    script to read files in a folder and ouput dataframe
    psize, df = readFiles('/home/kalagodk/docStuff/xTrack3/output/umData/281/Z281.*')
    
    Created on Mon May 17 09:52:47 2021
    
    @author: kalagodk
    """
    import time
    import dask.dataframe as dd
    import re
    
    
    startTime = time.time()
    # x --> particle location
    # v --> particle velocity
    # u --> fluid velocity
    # a --> drag acceleration
    # av --> particle acceleration
    # au --> fluid acceleration
    # dt --> time step
    # cellNum --> cell number
    columns = ['x0', 'x1', 'x2', 'v0', 'v1', 'v2', 'u0', 'u1', 'u2',
               'a0', 'a1', 'a2', 'av0', 'av1', 'av2', 'au0', 'au1', 'au2',
               'dt', 'cellNum']
    
    psize = list(map(int, re.findall(r'\d+', folderpath)))[-1]
    df = dd.read_csv(folderpath, delim_whitespace=True, names=columns)
    endTime = time.time()
    
    print("Time taken to read files from " + str(psize) + " folder = " +
          str(endTime-startTime) + "s")
    
    return psize, df


# test case
if __name__ == "__main__":
    psize, df = readFiles('/home/kalagodk/docStuff/xTrack3/output/umData/281/Z281.*')