#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def plotFig(xx, xp, yy, yp, I, xres, yres, my_dpi=96, snapNum=0):
    """
    fig, ax = plotFig(x, xp, y, yp, I, xres, yres, my_dpi, snapNum=1)

    Parameters
    ----------
    x : 2D numpy array
        Grid X co-ordinates of the exp plane
        DESCRIPTION.
    xp : 1D numpy array
        Filtered particle locations x-coordinates
    y : 2D numpy array
        Grid Y co-ordinates of the exp plane
    yp : 1D numpy array
        Filetered particle locations y-coordinates
    I : 2D numpy array
        Intensity field based on particle locations and other factors.
    xres : int (pixels)
        Resolution of CCD in x-direction.
    yres : int (pixels)
        Resolution of CCD in y-direction.
    my_dpi : int (pixels), optional
        dots per inch for the image. The default is 96.
    snapNum : int, optional
        Number of snap to save the fig. The default is 0.

    Returns
    -------
    fig : matplotlib.figure.Figure
        figure used to save the image.
    ax : matplotlib.axes._subplots.AxesSubplot
        Can be used to change parameters of the plot.
        
    By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
    Date created: Mon May 17 11:01:05 2021

    """
    
    
    import matplotlib.pyplot as plt
    
    # Set the plot resolution
    xsize = xres/my_dpi
    ysize = yres/my_dpi
    
    # Plot the contour
    fig = plt.figure(figsize=[xsize, ysize], dpi=my_dpi)
    ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(xx.min(), xx.max()),
                  ylim=(yy.min(), yy.max()))
    ax.contourf(xx, yy, I, cmap='jet')
    ax.set_title("Contour plot for intensities: Snap-" + str(snapNum))
    
    # Scatter plot
    fig = plt.figure(figsize=[xsize, ysize], dpi=my_dpi)
    ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(xx.min(), xx.max()),
                  ylim=(yy.min(), yy.max()))
    ax.scatter(xp, yp, color='r')
    ax.grid()
    ax.set_title("Scatter plot for intensities: Snap-" + str(snapNum))
    
    # Image to save
    fig = plt.figure(figsize=[xsize, ysize], dpi=my_dpi)
    ax = plt.axes([0.0, 0.0, 1.0, 1.0])
    ax.imshow(I, cmap='gray', origin='lower')
    ax.axis('tight')
    #ax.set_title("Image for intensities: Snap-" + str(snapNum))
    plt.show()
   
    
    return fig, ax