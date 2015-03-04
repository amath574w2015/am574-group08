#!/usr/bin/python

from clawpack.visclaw.data import ClawPlotData
import matplotlib.pyplot as plt
import os
import csv
import numpy as np


plotdata = ClawPlotData()
plotdata.outdir = '_output_no_column'   # set to the proper output directory
gaugeno = 1                   # gauge number to examine
g = plotdata.getgauge(gaugeno)
#g.t is the array of times
#g.q is the array of values recorded at the gauges (g.q[m,n] is the m`th variable at time `t[n])


if not('myplot' in os.listdir('./')):
    os.mkdir('myplot')

#read experiment result and OpenFOAM result
with open('./dataForComp/waveHeightNoColumnExp.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    waveHeightNoColumnExp = list(reader)
    waveHeightNoColumnExp = np.array(waveHeightNoColumnExp)
    waveHeightNoColumnExp = waveHeightNoColumnExp.astype(np.float)#convert string to floats
    waveHeightNoColumnExp[:,1] = waveHeightNoColumnExp[:,1]+0.005751788#The exp data should be shifted before being used
with open('./dataForComp/waveHeightNoColumnOF.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    waveHeightNoColumnOF = list(reader)
    waveHeightNoColumnOF = np.array(waveHeightNoColumnOF)
    waveHeightNoColumnOF = waveHeightNoColumnOF.astype(np.float)

with open('./dataForComp/velocity_nocolumn_exp.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    velocity_nocolumn_exp = list(reader)
    velocity_nocolumn_exp = np.array(velocity_nocolumn_exp)
    velocity_nocolumn_exp = velocity_nocolumn_exp.astype(np.float)

#compute depth-averaged velocity u from experiment data



    



#plot wave height history
#plt.subplot(211)
plt.figure()
plt.plot(g.t,g.q[0,:],'b-.',label='geoclaw')
plt.plot(waveHeightNoColumnOF[:,0],waveHeightNoColumnOF[:,1],'r--',label='OF')
plt.plot(waveHeightNoColumnExp[:,0],waveHeightNoColumnExp[:,1],'g--',label='Exp')
legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.xlabel('time (s)')
plt.ylabel('wave height')
plt.title('wave height history at x=11.1')
plt.savefig('./myplot/waveheight.png', bbox_inches='tight')
plt.close()

#plot velocity u history
plt.figure()
plt.plot(g.t,g.q[1,:],'b-')
plt.xlabel('time (s)')
plt.ylabel('velocity u')
plt.title('velocity u history at x=11.1')
plt.savefig('./myplot/velocityU.png', bbox_inches='tight')
plt.close()
