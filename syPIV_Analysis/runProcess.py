#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The script used to generate syPIV images. Modify parameters as needed

By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
Date created: Mon May 17 11:01:05 2021

"""
import time
from intensityField import intensityField
from planeTransform import planeTransform
from plotFig import plotFig
from save_to_tiff import save_to_tiff
from createImage import firstImage, secondImage
from multiProcess import multiProcess
import numpy as np

if __name__ == "__main__":
    folderpath = "/home/kalagodk/docStuff/xTrack3/output/umData/temporalAveraging/0.01/Z281.*"
    startTime = time.time()
    # Magnification factor
    mfx = 50
    mfy = 50
    # Other variables needed for intensity field computation
    sx = 2.0  # pattern mean in x-direction in pixels
    sy = 1.6  # patterm mean in y-direction in pixels
    frx = 1.0  # ccd fill ratio in x-direction
    fry = 1.0  # ccd fill ratio in y-direction
    xres = 1280  # pixels
    yres = 1024  # pixels
    my_dpi = 96  # dots per inch used for generating images in matplotlib
    dtime = 1e-6  # laser pulse time in sec
    
    
    # Transform and filter data to exp plane
    x, y, pSize, df = planeTransform(folderpath, frac=0.75)
    
    # Compute relative intensity field and store in I
    #I = intensityField(radiusx, radiusy, x, xp, y, yp, sx, sy, frx, fry)
    
    # Create data for the first image
    radiusx, radiusy, x, xp, y, yp = firstImage(x, y, pSize, df, mfx, mfy)
    # To generate hybrid first image uncomment the following lines
    #xp = np.concatenate((xp, np.random.uniform(x.min(), x.max(), df.shape[0])))
    #yp = np.concatenate((yp, np.random.uniform(y.min(), y.max(), df.shape[0])))
    cache = (radiusx, radiusy, x, xp, y, yp, sx, sy, frx, fry)
    # Use multi-process module to speedup the computation process
    I = multiProcess(intensityField(cache), x, xp, y, yp, chunksize=512)
    # plot the intensity field and scatter plot
    fig, ax = plotFig(x, xp, y, yp, I, xres, yres, my_dpi, snapNum=1)
    # save the intensity plot
    save_to_tiff(fig, ax, pSize, my_dpi, snapNum=1)
    
    
    # Create data for second image
    xp, yp = secondImage(pSize, df, dtime, mfx, mfy)
    cache = (radiusx, radiusy, x, xp, y, yp, sx, sy, frx, fry)
    # Use multi-process module to speedup the computation process
    I = multiProcess(intensityField(cache), x, xp, y, yp, chunksize=512)
    # plot the intensity field and scatter plot
    fig, ax = plotFig(x, xp, y, yp, I, xres, yres, my_dpi, snapNum=2)
    # save the intensity plot
    save_to_tiff(fig, ax, pSize, my_dpi, snapNum=2)
    
    endTime = time.time()
    
    print("Time taken for the whole process: " + str(endTime-startTime) + "s")
    