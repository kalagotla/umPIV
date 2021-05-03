#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script averages the data of different particle
sizes based on given mean, and standard deviation

By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
Date: 04-23/2021
"""

def statAnalysis(pmin=177, pmax=574, mu=281, sd=0.1):
    import numpy as np
    import matplotlib.pyplot as plt
    from alive_progress import alive_bar
    import time
    
    # Sizes of particles to be averaged
    x = np.arange(pmin, pmax)
    
    # using normal distribution
    f = 1/(sd*np.sqrt(2*np.pi)) * np.e**(-0.5 * ((x-mu)/(sd))**2)
    print("Sum of values in the distribution = ", np.sum(f))
        
    # Plot of the distribution
    fig, ax = plt.subplots()
    ax.plot(x, f)
    ax.set_xlabel('Particle sizes (nm)')
    ax.set_ylabel('f(x)')
    ax.set_title('Probability density function')
    ax.grid()
    
    data = []
    filePath = "expPlaneData/flowData"
    with alive_bar(x.size, bar='squares') as bar:
        for i in x:
            try:
                temp = np.loadtxt(filePath + str(i) + ".q",
                               skiprows=1)
                data.append(temp)
            except:
                data.append(np.zeros(temp.shape))
                print('Particle size ' + str(i) + 'nm not found.' + 
                      ' Used zeros for averaging')
            
            time.sleep(0.01)
            bar()
        
    print("&"*100)
    print("Done computing. Writing the file to flowData.q...")
    
    # To multiply each row with a value in f
    avgData = (f * np.array(data).T).T
    avgData = sum(avgData)
    
    gline1 = np.loadtxt(filePath + str(x[0]) + ".q",
                        dtype=int, max_rows=1)
    gline1 = str(gline1).strip('[]')
    np.savetxt(filePath + ".q",
               avgData, header=gline1, comments='')
    
    print("Done writing! Use any girdData.x and flowData.q for visualizing")
    
    return

if __name__ == "__main__":
    statAnalysis(sd = 10.0)