#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def intensityField(cache):
    """
    DONOT IMPLEMENT THIS DIRECTLY UNLESS ABSOLUTELY SURE!!
    MEMORY ISSUES with the code that is commented out
    USE multiProcess instead
    cache = (radiusx, radiusy, x, xp, y, yp, sx, sy, frx, fry)
    I = intensityField(cache)

    Parameters
    ----------
    cache : tuple
        Has all the variables needed for intensityField function.
        Created to clean-up the code
        
    Returns
    -------
    intensity : function
        Intensity field as a function of particle locations.
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Mon May 17 11:00:56 2021

    """
    from scipy.special import erf
    import numpy as np
    
    (radiusx, radiusy, x, xp, y, yp, sx, sy, frx, fry) = cache
    
    # Use the commented out part if there is a lot of Memory
    # Computation will be faster
    # array used for computation
    # xc = np.repeat(x[None, :, :], len(xp), axis=0) 
    # yc = np.repeat(y[None, :, :], len(yp), axis=0)
    # xpc = (np.ones(xc.shape).T * xp).T
    # ypc = (np.ones(yc.shape).T * yp).T
    
    
    # intensity = np.sum(np.pi/8 * (2*radiusx) * (2*radiusy) * sx * sy *
    #                     (erf((xc-xpc + 0.5*frx)/(sx * np.sqrt(2)))  - 
    #                       erf((xc-xpc - 0.5*frx)/(sx * np.sqrt(2)))) * 
    #                     (erf((yc-ypc + 0.5*fry)/(sy * np.sqrt(2)))  - 
    #                       erf((yc-ypc - 0.5*fry)/(sy * np.sqrt(2)))), axis=0)
    
    intensity = lambda xp, yp: (np.pi/8 * (2*radiusx) * (2*radiusy) * sx * sy *
                        (erf((x-xp + 0.5*frx)/(sx * np.sqrt(2)))  - 
                          erf((x-xp - 0.5*frx)/(sx * np.sqrt(2)))) * 
                        (erf((y-yp + 0.5*fry)/(sy * np.sqrt(2)))  - 
                          erf((y-yp - 0.5*fry)/(sy * np.sqrt(2)))))
    
    return intensity