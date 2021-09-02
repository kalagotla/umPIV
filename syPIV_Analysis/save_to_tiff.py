#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:01:05 2021

@author: kalagodk
"""

def save_to_tiff(fig, ax, pSize, my_dpi, snapNum=0):
    
    folder = "intensityFields/"
    name = folder + str(pSize) + "_" + str(snapNum) + ".tif"
    fig.savefig(name, dpi=my_dpi)
    
    return name

def stack_images(name1, name2, pSize):
    from PIL import Image
    
    images = [Image.open(x) for x in [name1, name2]]
    widths, heights = zip(*(i.size for i in images))
    
    maxWidth = max(widths)
    totalHeight = sum(heights)
    
    new_im = Image.new('RGB', (maxWidth, totalHeight))
    
    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]
        
    new_im.save('intensityFields/' + str(pSize) +'Stacked.tif')
    
    return