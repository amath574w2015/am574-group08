#!/usr/bin/python

from clawpack.visclaw.data import ClawPlotData
import matplotlib.pyplot as plt
import os
import csv
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#for case without a column
def plot_no_column():
    plotdata = ClawPlotData()
    plotdata.outdir = '_output_nocolumn'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
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


    #plot wave height history
    plt.figure()
    plt.plot(g.t,g.q[0,:],'b-.',label='geoclaw')
    plt.plot(waveHeightNoColumnOF[:,0],waveHeightNoColumnOF[:,1],'r--',label='OpenFOAM')
    plt.plot(waveHeightNoColumnExp[:,0],waveHeightNoColumnExp[:,1],'g--',label='Exp')
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.xlim(3.0,4.0)
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at x=11.1')
    plt.savefig('./myplot/waveheight_nocolumn_xlim_x=11.0.png', bbox_inches='tight')
    plt.close()

    #plot velocity u history
    plt.figure()
    #q[1] is hu instead of u
    u=np.zeros(g.t.size)
    for i in range(g.t.size):
        u[i] = g.q[1,i]/g.q[0,i]
    plt.plot(g.t,u,'b-',label='geoclaw')
    plt.plot(velocity_nocolumn_exp[:,0],velocity_nocolumn_exp[:,1],'r--',label='Exp')
    legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')
    plt.xlabel('time (s)')
    plt.ylabel('velocity u (m/s)')
    plt.title('velocity u history at x=11.1')
    plt.savefig('./myplot/velocityU_nocolumn.png', bbox_inches='tight')
    plt.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#for case with a cylinder
def plot_cylinder():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #gauge 6
    plotdata = ClawPlotData()
    plotdata.outdir = '_output_cylinder_2'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
    g1 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_finerColumntt1'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
    g2 = plotdata.getgauge(gaugeno)
    if not('myplot' in os.listdir('./')):
        os.mkdir('myplot')
    #read experiment result and OpenFOAM result
    with open('./dataForComp/waveheight_cylinder_dist=-40.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        wave_height_cylinder = list(reader)
        wave_height_cylinder = np.array(wave_height_cylinder)
        wave_height_cylinder = wave_height_cylinder.astype(np.float)#convert string to floats
        wave_height_cylinder[:,1] = wave_height_cylinder[:,1]/1000.0#convert to meters

    #plot waveheight history
    plt.figure()
    plt.plot(g1.t,g1.q[0,:],'b-',label='geoclaw')
    #plt.plot(g2.t,g2.q[0,:],'g-',label='geoclaw2')
    plt.plot(wave_height_cylinder[:,0],wave_height_cylinder[:,1],'r--',label='Exp')
    legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at x=11.0')
    plt.xlim(3.0,4.0)
    plt.savefig('./myplot/waveheight_cylinder_x=11.0.png', bbox_inches='tight')
    plt.close()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #gauge 1
    plotdata = ClawPlotData()
    plotdata.outdir = '_output_finerColumntt1'   # set to the proper output directory
    gaugeno = 1                   # gauge number to examine
    g1 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_cylinder_3'   # set to the proper output directory
    gaugeno = 1 #gauge at tailing edge of cylinder
    g3 = plotdata.getgauge(gaugeno)
    with open('./dataForComp/waveheight_cylinder_dist=120.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        wave_height_cylinder = list(reader)
        wave_height_cylinder = np.array(wave_height_cylinder)
        wave_height_cylinder = wave_height_cylinder.astype(np.float)#convert string to floats
        wave_height_cylinder[:,1] = wave_height_cylinder[:,1]/1000.0#convert to meters

    #plot waveheight history
    plt.figure()
    plt.plot(g1.t,g1.q[0,:],'g-',label='geoclaw_gauge_located at the edge')
    plt.plot(g3.t,g3.q[0,:],'b-',label='geoclaw_gauge_shifted 5mm away from edge')
    plt.plot(wave_height_cylinder[:,0],wave_height_cylinder[:,1],'r--',label='Exp')
    legend = plt.legend(loc='upper center', shadow=True,prop={'size':10})
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at x=11.16')
    plt.xlim(3.0,4.0)
    plt.savefig('./myplot/waveheight_cylinder_x=11.16_compare_shifted_gauge.png', bbox_inches='tight')
    plt.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#for case with a square
def plot_square():
    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
    g1 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square_2'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
    g2 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square_3'   # set to the proper output directory
    gaugeno = 6                   # gauge number to examine
    g3 = plotdata.getgauge(gaugeno)
    if not('myplot' in os.listdir('./')):
        os.mkdir('myplot')

    #read experiment result and OpenFOAM result
    with open('./dataForComp/waveheight_square_dist=-40.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        wave_height_square = list(reader)
        wave_height_square = np.array(wave_height_square)
        wave_height_square = wave_height_square.astype(np.float)#convert string to floats
        wave_height_square[:,1] = wave_height_square[:,1]/1000.0

    #plot waveheight history
    plt.figure()
    #plt.plot(g1.t,g1.q[0,:],'y-',label='geoclaw1')
    #plt.plot(g2.t,g2.q[0,:],'g-.',label='geoclaw2')
    plt.plot(g3.t,g3.q[0,:],'b-',label='geoclaw')
    plt.plot(wave_height_square[:,0],wave_height_square[:,1],'r--',label='Exp')
    legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at x=11.0')
    plt.xlim(3.0,4.0)
    plt.savefig('./myplot/waveheight_square_x=11.0.png', bbox_inches='tight')
    plt.close()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #gauge 1
    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square'   # set to the proper output directory
    gaugeno = 1                   # gauge number to examine
    g1 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square_2'   # set to the proper output directory
    gaugeno = 1                   # gauge number to examine
    g2 = plotdata.getgauge(gaugeno)

    plotdata = ClawPlotData()
    plotdata.outdir = '_output_square_3'   # set to the proper output directory
    gaugeno = 1                   # gauge number to examine
    g3 = plotdata.getgauge(gaugeno)
    with open('./dataForComp/waveheight_square_dist=120.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        wave_height_cylinder = list(reader)
        wave_height_cylinder = np.array(wave_height_cylinder)
        wave_height_cylinder = wave_height_cylinder.astype(np.float)#convert string to floats
        wave_height_cylinder[:,1] = wave_height_cylinder[:,1]/1000.0#convert to meters

    #plot waveheight history
    plt.figure()
    plt.plot(g1.t,g1.q[0,:],'b-',label='geoclaw')
    #plt.plot(g2.t,g2.q[0,:],'g-.',label='geoclaw2')
    #plt.plot(g3.t,g3.q[0,:],'y-o',label='geoclaw3')
    plt.plot(wave_height_cylinder[:,0],wave_height_cylinder[:,1],'r--',label='Exp')
    legend = plt.legend(loc='lower center', shadow=True, fontsize='x-large')
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at x=11.16')
    plt.xlim(3.0,4.0)
    plt.savefig('./myplot/waveheight_square_x=11.16.png', bbox_inches='tight')
    plt.close()


plot_cylinder()
#plot_square()
#plot_no_column()
