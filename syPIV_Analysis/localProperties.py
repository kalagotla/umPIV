#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The script is used to obtain local properties at a given location

By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
Date created: Tue June 15 09:05:05 2021

"""

def localProperties(x, y, xx, yy, df, dfp, interpMethod='cubic'):
    from scipy import interpolate
    import matplotlib.pyplot as plt
    
    # Create a 2d flowfield using particle data. This saves particle dynamics
    # streamwise velocity
    vxx = interpolate.griddata((df.x, df.y), df.vx, (xx, yy),
                               method=interpMethod, fill_value=df.vx.min())
    uxx = interpolate.griddata((df.x, df.y), df.ux, (xx, yy),
                               method=interpMethod, fill_value=df.vx.min())
    plt.figure()
    plt.contourf(xx, yy, vxx)
    plt.show()
    
    # Transverse velocity
    vyy = interpolate.griddata((df.x, df.y), df.vy, (xx, yy),
                               method=interpMethod, fill_value=df.vx.min())
    uyy = interpolate.griddata((df.x, df.y), df.uy, (xx, yy),
                               method=interpMethod, fill_value=df.vx.min())
    
    xp = dfp.xp
    yp = dfp.yp
    # Bilinear interpolation to estimate local velocities at particle positions
    f = interpolate.interp2d(x, y, vxx, kind=interpMethod)
    vxp = f(xp, yp)
    
    f = interpolate.interp2d(x, y, vyy, kind=interpMethod)
    vyp = f(xp, yp)
    
    f = interpolate.interp2d(x, y, uxx, kind=interpMethod)
    uxp = f(xp, yp)
    
    f = interpolate.interp2d(x, y, uyy, kind=interpMethod)
    uyp = f(xp, yp)
    
    dfp['vxp'] = vxp[0]
    dfp['vyp'] = vyp[0]
    dfp['uxp'] = uxp[0]
    dfp['uyp'] = uyp[0]
    
    return dfp
    

# Test case
if __name__ == "__main__":
    from planeTransform import planeTransform
    from createImage import firstImage
    folderpath = "/home/kalagodk/docStuff/xTrack3/output/umData/281/Z281.*"
    x, y, pSize, df = planeTransform(folderpath, frac=0.01)
    radiusx, radiusy, x, y, xx, yy, df, dfp = firstImage(x, y, pSize, df,
                                                     mfx=50, mfy=50)
    localProperties(x, y, xx, yy, df, dfp)