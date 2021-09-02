#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def firstImage(x, y, pSize, df, mfx, mfy):
    """
    radiusx, radiusy, x, xp, y, yp = firstImage(x, y, pSize, df, mfx, mfy)
    
    Parameters
    ----------
    x : 2D numpy array
        Grid X co-ordinates of the exp plane
    y : 2D numpy array
        Grid Y co-ordinates of the exp plane
    pSize : int
        Size of the particle in nm
    df : pandas dataframe
        Required data set for the analysis
    mfx : float
        Maginification factor for lens in x-direction.
    mfy : float
        Maginification factor for lens in y-direction.

    Returns
    -------
    radiusx : float
        particle radius in x-direction after applying mfx.
    radiusy : float
        particle radius in y-direction after applying mfy.
    x : 2D numpy array
        Grid X co-ordinates of the exp plane
        DESCRIPTION.
    xp : 1D numpy array
        Filtered particle locations x-coordinates
    y : 2D numpy array
        Grid Y co-ordinates of the exp plane
    yp : 1D numpy array
        Filtered particle locations y-coordinates
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Mon May 24 09:22:40 2021

    """
    import numpy as np
    import pandas as pd
    # Make a projection onto CCD
    x = x * mfx
    y = y * mfy
    xx, yy = np.meshgrid(x, y)
    
    # Project the particle locations from xTrack3
    df.x = df.x * mfx
    df.y = df.y * mfy
    
    # Create particles in a uniform distribution on ccd
    xp = np.random.uniform(x.min(), x.max(), df.shape[0])
    yp = np.random.uniform(y.min(), y.max(), df.shape[0])
    data = {'xp': xp, 'yp': yp}
    dfp = pd.DataFrame(data)
    
    # Convert integer pSize to actual particle size in mm
    radiusx = pSize * mfx * 1e-6 / 2
    radiusy = pSize * mfy * 1e-6 / 2
    
    return radiusx, radiusy, x, y, xx, yy, df, dfp

def secondImage(pSize, xp, yp, vxp, vyp, dtime, mfx, mfy):
    """
    xp, yp = secondImage(pSize, df, dtime, mfx, mfy)

    Parameters
    ----------
    pSize : int
        Size of the particle in nm
    df : pandas dataframe
        Required data set for the analysis
    dtime : float
        Laser-pulse time or time-step for particle movement in sec.
    mfx : float
        Maginification factor for lens in x-direction.
    mfy : float
        Maginification factor for lens in y-direction.

    Returns
    -------
    xp : 1D numpy array
        New particle locations x-coordinates
    yp : 1D numpy array
        New particle locations y-coordinates
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Mon May 24 09:22:40 2021

    """
    
    # Calculate the shift in particle positions
    xp = xp + vxp * dtime
    yp = yp + vyp * dtime
    
    return xp, yp