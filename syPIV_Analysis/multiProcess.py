#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiProcess(function, x, xp, y, yp, chunksize=512):
    """
    I = multiProcess(intensityField(cache), x, xp, y, yp, chunksize=512)

    Parameters
    ----------
    function : function
        Intensity field function with particle locations (xp, yp) as vars
    x : 2D numpy array
        Grid X co-ordinates of the exp plane
        DESCRIPTION.
    xp : 1D numpy array
        Filtered particle locations x-coordinates
    y : 2D numpy array
        Grid Y co-ordinates of the exp plane
    yp : 1D numpy array
        Filetered particle locations y-coordinates
    chunksize : int, optional
        Use in 2**n for better performance. The default is 512.

    Returns
    -------
    I : 2D numpy array
        Intensity field based on particle locations and other factors.
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Mon May 24 12:05:52 2021

    """
    
    import numpy as np
    from multiprocessing.dummy import Pool as ThreadPool
    from multiprocessing import cpu_count
    
    # Using multiprocessing to compute relative intensity field
    I = np.zeros(x.shape)
    i = 0
    j = chunksize
    while j <= len(xp):
        n = max(1, cpu_count()-1)
        pool = ThreadPool(n)
        Itemp = pool.starmap(function, zip(xp[i:j], yp[i:j]))
        pool.close()
        pool.join()
        
        I += np.sum(Itemp, axis=0)
        i = j
        j += chunksize
    
    n = max(1, cpu_count()-1)
    pool = ThreadPool(n)
    Itemp = pool.starmap(function, zip(xp[i:-1], yp[i:-1]))
    pool.close()
    pool.join()
    
    I += np.sum(Itemp, axis=0)
    
    # Average intensity field
    I = I/len(xp)
    
    return I