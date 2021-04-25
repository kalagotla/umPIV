#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script creates a cool animation to show
the progress of running expPlane on multiple particle sizes
Uses alive_progress. Credit: https://github.com/rsalmei/alive-progress

By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
Date: 04-23/2021
"""
from alive_progress import alive_bar
import time
from expPlane import expPlane

with alive_bar(397, bar='squares') as bar:
    for i in range(177, 574):
        try:
            # main program
            expPlane("/home/kalagodk/docStuff/xTrack3/output/umData/" +
                     str(i) + "/Z" + str(i) + ".*")
        except:
            print(str(i) + "nm particle size not found")
            
        time.sleep(0.01)
        bar()
