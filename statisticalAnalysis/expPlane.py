#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def expPlane(folderpath):
    """
    This script reads in the particle data files outputted by xTrack3
    expPlane('../../xTrack3/output/umData/281/Z281*')
    Output: Experimental plane Num-PIV data in p3d format
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: 04-21/2021
    """
    
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    from scipy.interpolate import griddata
    import dask.dataframe as dd
    import re
    import p3dFormat as p3d  # Explicitly sepcify
    
    
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
    
    df["x"] = 25.4 * (2.75 * df.x0 * 1000 - 38.265)
    df["y"] = 25.4 * 2.75 * df.x2 * 1000
    df["z"] = 25.4 * 2.75 * df.x1 * 1000 - 1.125
    
    df = df[(df.x.between(17.7, 65.0)) & (df.y.between(0.01, 20))]
    
    # 86x35 grid in PIV
    x = np.linspace(18.191, 61.851, 86)
    y = np.linspace(0.25681, 17.721, 35)
    
    X, Y = np.meshgrid(x, y)
    
    uPIV = griddata((df.x, df.y), df.v0/603.0,
                    (X, Y), method='linear', fill_value=0)
    vPIV = griddata((df.x, df.y), df.v1/603.0,
                    (X, Y), method='linear', fill_value=0)
    wPIV = griddata((df.x, df.y), df.v2/603.0,
                    (X, Y), method='linear', fill_value=0)
    
    flowData = [uPIV, vPIV, wPIV]
    
    # Explicity using p3d instead of "from plot3d import *"
    p3d.p3dFormat(X, Y, flowData, psize)
    
    # To test if the code is working uncomment below
    # fig, ax = plt.subplots()
    # ax.contourf(X ,Y, uPIV, np.linspace(0, 1, 100), cmap='jet')
    # ax.set_xlabel('X(mm)')
    # ax.set_ylabel('Y(mm)')
    # ax.set_title('Sample output; U-contour')
    # ax.grid()
    
    endTime = time.time()
    
    print('Time taken to write '+ str(psize) + 'nm paritlce data: '
          , endTime-startTime)
    
    
    return

# Test run
if __name__ == "__main__":
    expPlane('/home/kalagodk/docStuff/xTrack3/output/umData/281/Z281.*')
    