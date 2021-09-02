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
from save_to_tiff import save_to_tiff, stack_images
from createImage import firstImage, secondImage
from multiProcess import multiProcess
from localProperties import localProperties

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
    yres = 512  # pixels
    my_dpi = 96  # dots per inch used for generating images in matplotlib
    dtime = 1e-4  # laser pulse time in sec
    
    
    # Transform and filter data to exp plane
    x_exp, y_exp, pSize, df = planeTransform(folderpath, frac=1)
    
    # Create data for the first image
    radiusx, radiusy, x, y, xx, yy, df, dfp = firstImage(x_exp, y_exp, pSize, df, mfx, mfy)
    # To generate hybrid first image uncomment the following lines
    cache = (radiusx, radiusy, xx, dfp.xp, yy, dfp.yp, sx, sy, frx, fry)
    # Use multi-process module to speedup the computation process
    I = multiProcess(intensityField(cache), xx, dfp.xp, yy, dfp.yp, chunksize=512)
    # plot the intensity field and scatter plot
    fig, ax = plotFig(xx, dfp.xp, yy, dfp.yp, I, xres, yres, my_dpi, snapNum=1)
    # save the intensity plot
    name1 = save_to_tiff(fig, ax, pSize, my_dpi, snapNum=1)
    
    
    # Create data for second image
    dfp = localProperties(x, y, xx, yy, df, dfp)
    xp, yp = secondImage(pSize, dfp.xp, dfp.yp, dfp.uxp, dfp.uyp, dtime, mfx, mfy)
    cache = (radiusx, radiusy, xx, xp, yy, yp, sx, sy, frx, fry)
    # Use multi-process module to speedup the computation process
    I = multiProcess(intensityField(cache), xx, xp, yy, yp, chunksize=512)
    # plot the intensity field and scatter plot
    fig, ax = plotFig(xx, xp, yy, yp, I, xres, yres, my_dpi, snapNum=2)
    # save the intensity plot
    name2 = save_to_tiff(fig, ax, pSize, my_dpi, snapNum=2)
    
    stack_images(name1, name2, pSize)
    
    endTime = time.time()
    
    print("Time taken for the whole process: " + str(endTime-startTime) + "s")
    