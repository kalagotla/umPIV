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
    
    # Make a projection onto CCD
    x = x * mfx
    y = y * mfy
    x, y = np.meshgrid(x, y)
    
    xp = df.x.to_numpy() * mfx
    yp = df.y.to_numpy() * mfy
    
    # Convert integer pSize to actual particle size
    radiusx = pSize * 1e-9 * mfx / 2
    radiusy = pSize * 1e-9 * mfy / 2
    
    return radiusx, radiusy, x, xp, y, yp

def secondImage(pSize, df, dtime, mfx, mfy):
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
    
    # convert velocity to mm/s
    df.vx = 1e3 * df.vx
    df.vy = 1e3 * df.vy
    
    # Calculate the shift in particle positions
    xp = df.x + df.vx * dtime
    yp = df.y + df.vy * dtime
    
    # Make a projection onto CCD plane
    xp = xp.to_numpy() * mfx
    yp = yp.to_numpy() * mfy
    
    return xp, yp