#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def planeTransform(folderpath, frac=0.5, random_state=7):
    """
    x, y, pSize, df = planeTransform(folderpath, frac=0.05, random_state=7)

    Parameters
    ----------
    folderpath : string
        The path to where the particle field is located
    frac : float, optional
        Randomly filters the particle field passed. The default is 0.5.
    random_state : int, optional
        Change to get different fields for the same frac. The default is 7.

    Returns
    -------
    x : 2D numpy array
        Grid X co-ordinates of the exp plane
    y : 2D numpy array
        Grid Y co-ordinates of the exp plane
    pSize : int
        Size of the particle in nm
    df : pandas dataframe
        Required data set for the analysis
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Wed May  5 08:46:12 2021

    """
    import sys
    sys.path.append("../")
    import numpy as np
    from readFiles import readFiles
    
    pSize, df = readFiles(folderpath)
    
    df = df.compute()
    # Only use what's needed for the current computation
    df = df.iloc[:, :6]
    
    # Transform to experimental plane in mm
    df["x"] = 25.4 * (2.75 * df.x0 * 1000 - 38.265)
    df["y"] = 25.4 * 2.75 * df.x2 * 1000
    df["z"] = 25.4 * (2.75 * df.x1 * 1000 - 1.125)
    
    df['vx'] = df.v0
    df['vy'] = df.v2
    df['vz'] = df.v1
    
    # Drop columns that are not needed for future computation
    df.drop(np.arange(0, 6), inplace=True)
    
    # Filter the experimental plane
    df = df[(df.x.between(17.7, 65.0)) & 
            (df.y.between(0.01, 20))]
    
    # Randomize the data
    df = df.sample(frac=frac, random_state=random_state)
    
    x = np.linspace(18.191, 61.851, 1280)
    y = np.linspace(0.25681, 17.721, 1024)
    
    return x, y, pSize, df

if __name__ == "__main__":
    planeTransform("/home/kalagodk/docStuff/xTrack3/output/umData/281/Z281.*")
    
