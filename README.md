By: Dilip Kalagotla ~ kal @ dilip.kalagotla@gmail.com
Date created: 04-25/2021

Script to create **NPIV** data in explerimental plane for **UM Wind Tunnel**
Input the folder with data files Eg: "xTrack3/output/umPIV/280/Z280.\*"
Run **python runProcess.py** for a preset automated execution

**Note:** The script uses *alive_progress* to create animation. Install to run
[Credit: rsalmei](https://github.com/rsalmei/alive-progress)

The data generated from *runProcess.py* will be used for statistically averaging

Run **python statAnalysis.py** to obtain the averaged data using normal distribution.
Parameters like *standard deviation* need to be adjusted

Date: 05-26/2021

**BUG:** There seems to be a bug when running from the terminal

New scripts are created to generate **syPIV** images.
All of these scripts are in **./syPIV_Analysis**

The code is based on the formulation from [EUROPIV](https://link.springer.com/chapter/10.1007/978-3-642-18795-7_11)
*One big difference physics wise is we keep track of particle dynamics history*
Theoretically this should make a major difference when looking to understand particle lag

Note: *The images are currently implemented only for 2D Planar PIV*

A lot of parameters are needed for the process to work
Most of them are described in EUROPIV documentation
One new parameter is *my_dpi*, which is used for adjusting pixels on a matplotlib plot

Workflow:
1. Paritcles are generated using **xTrack3**
2. All of these are read into syPIV_Analysis using **./readFiles.py**
3. These are transformed into experimental plane and are flitered randomly to replicate PIV
4. This information is then used to generate the intensity field
5. Multi-processing is implemented using *multiprocessing* module

Run **runProcess.py** in spyder to get the correct images.
