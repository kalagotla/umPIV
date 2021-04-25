#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def p3dFormat(X, Y, flowData, psize):
    """
    This internal script creates p3d format files
    run expPlane(folderpath)
    Output: gridData.x and flowData.q files
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: 04-22/2021
    """
    
    import numpy as np
    
    # shapes of the dataset
    xSize = int(X.shape[0])
    ySize = int(X.shape[1])
    fSize = int(len(flowData))
    
    # write grid data in p3d format
    f = []
    [f.append(X[:, j]) for j in range(ySize)]
    [f.append(Y[:, j]) for j in range(ySize)]
    [f.append([0]*xSize) for j in range(ySize)]
    
    fline1 = str(xSize) + " " + str(ySize) + " " + str(1)
    folder = 'expPlaneData/'
    np.savetxt(folder + 'gridData' + str(psize) + '.x',
               f, header=fline1, comments='')
    
    # write flow data in p3d format
    g = []
    for m in range(fSize):
        [g.append(flowData[m][:, j]) for j in range(ySize)]     
    
    gline1 = str(xSize) + " " + str(ySize) + " " + str(1) + " " + str(fSize)
    np.savetxt(folder + 'flowData' + str(psize) +'.q',
               g, header=gline1, comments='')
    
    
    return