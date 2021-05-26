#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:01:05 2021

@author: kalagodk
"""

def save_to_tiff(fig, ax, psize, my_dpi, snapNum=0):
    
    folder = "intensityFields/"
    fig.savefig(folder + str(psize) + "_" + str(snapNum) + ".tif", dpi=my_dpi)
    
    return