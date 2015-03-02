
from clawpack.geoclaw import topotools
from pylab import *

dx=.0025;

def maketopo():
    """
    Output topography files
    """
    nxpoints = 260
    nypoints = 12
    xlower = 0.
    xupper = 16.6
    ylower = 0.
    yupper = 0.6
    outfile= "domain.tt1"
    topotools.topo1writer(outfile,topo,xlower,xupper,ylower,yupper,nxpoints,nypoints)

    nxpoints = 260
    nypoints = 12
    xlower = 11.04
    xupper = 11.16
    ylower = 0.24
    yupper = 0.36
    outfile= "column.tt1"
    topotools.topo1writer(outfile,topo,xlower,xupper,ylower,yupper,nxpoints,nypoints)


def topo(x,y):
    """
    flat with cylinder
    """

    z = zeros(x.shape)
    xo=11.1;
    yo=0.3;
    base_r=0.12/2;

    ## cylinder column
#    hi=1.0;
#    dist = sqrt( (x-xo)**2+(y-yo)**2 );
#    zz = hi
#    z = where(dist<base_r, zz, 0.)
    
    ## square column
    hi=1.0
    z = where( ( (abs(x-xo)<base_r) & (abs(y-yo)<base_r) ),hi,0)

    return z

def plot_topo():

    topo1 = topotools.Topography()
    topo1.read('domain.tt1',1)
    figure(figsize=(12,4))
    ax = axes()
    topo1.plot(axes=ax,add_colorbar=False)

    topo2 = topotools.Topography()
    topo2.read('hump.tt1',1)
    topo2.plot(axes=ax)
    ax.set_xlim(0,9.84)
    ax.set_ylim(0,1.52)
    axis('scaled')

if __name__=='__main__':
    maketopo()
    
