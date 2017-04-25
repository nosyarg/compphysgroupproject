###########################################################################
#   Author:  Miguel De Los Reyes, Mridu Nanda, Grayson York                                                 #
#    Class:  PH412, Spring, 2017                                          #
#  Helpers:  none
#                                                                         #
#  Program:  Planetary orbits group project                                              #
# Due Date:  April 25, 2017                                                #
#                                                                         #
# Language:  Python 3                                                   #
#      IDE:  Anaconda                                                     #
#                                                                         #
#  Purpose:  Determine position of planets relative to the sun over time
#  #
#                                                                         #
#   "Bugs":  None
#   #
###########################################################################
from astropy.constants import G
from scipy.optimize import *
from math import *
#source for ellipse parameterization: http://www.pa.msu.edu/~stump/champ/mech3f01.pdf
#Source for year lengths: https://www.exploratorium.edu/ronh/age/
#source for eccentricity calculations: https://socratic.org/questions/if-an-asteroid-has-a-perihelion-distance-of-2-0-a-u-and-an-aphelion-distance-of--1
#planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#mass constants
mass = [0.33e24, 4.87e24, 5.97e24, 0.642e24, 1898e24, 568e24, 86.8e24, 102e24]
#aphelion distances m
aphelion = [69.8e6, 108.9e6, 152.1e6, 249.2e6, 816.6e6, 1514.5e6, 3003.6e6, 4545.7e6]
#perihelion distances m
perihelion = [ 46.0e6,107.5e6, 147.1e6, 206.6e6, 740.5e6, 1352.6e6, 2741.3e6, 4444.5e6]
#calculate eccentricity of ellipse
ecc = []
for i in range(len(planets)):
        ecc.append((aphelion[i]-perihelion[i])/(aphelion[i]+perihelion[i]))
#x and y starting positions in meters relative to the origin at the sun:
x = []
y = []
for i in range(len(planets)):
        x.append(0)
        y.append(aphelion[i])
#orbital period in years:
period = [87.97,224.7,365.26,1.88*365,11.86*365,29.46*365,84.01*365,164.79*365]
#convert from days to months
for i in range(len(period)):
        period[i] = period[i]*12/365
#return time given dummy variable psi and a planet index
def time(psi,pnum):
        return period[pnum]/(2*pi)*(psi-ecc[pnum]*sin(psi))
#accept user input time after alignment
t = int(input("How many months after alignment? (input negative number for past):"))
print("Positions relative to origin at Sun on day " + str(t) + ":")
x = []
y = []
for i in range(len(planets)):
        #set up function for error in time estimate relative to desired time for numerical soln
        def timeerror(psi):
                return abs(t - time(psi,i))
        #numerically find value of psi for posn. equations
        psi = minimize(timeerror,pi).x
        #calculate x and y coordinates based on orbit equations
        x.append((perihelion[i]+aphelion[i])/2*(cos(psi)-ecc[i]))
        y.append((perihelion[i]+aphelion[i])/2*sqrt(1-ecc[i]**2)*sin(psi))
        #output x and y coordinates along with angle of body relative to initial angle
        print(planets[i]+": ("+str(x[i])+" m,"+str(y[i])+" m) "+str(180/pi*atan2(y[i],x[i]))+" degrees")
