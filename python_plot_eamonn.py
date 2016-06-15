#! /usr/bin/python

# script made by Eamonn O'Shea for easy plotting of data
# first arguement is the data file you want to plot from,
# keyword 'using' if you don't want to use the first two columns

import sys
import pylab as plt


def plotmythings_scatt( ):
    for i in sys.argv:
        print i

    if len(sys.argv)==1:
        print 'Too few arguments'
        sys.exit()


        if len(sys.argv)>2 and sys.argv[2]=='using':
            j=int(sys.argv[3])
            k=int(sys.argv[4])
            i=sys.argv[1]
            plt.scatter(i, delimiter=' ', cols=(j-1,k-1))

        else:
            for i in sys.argv:
                if i==sys.argv[1]:
                    plt.scatter(i, delimiter=' ', cols=(0,1))
                if (i!=sys.argv[1] and i!=sys.argv[0]):
                    plt.scatter(i, delimiter=' ',newfig=False,cols=(0,1))



def plotmythings_lines( ):
    if len(sys.argv)==1:
        print 'Too few arguments'
        sys.exit()


        if len(sys.argv)>2 and sys.argv[2]=='using':
            j=int(sys.argv[3])
            k=int(sys.argv[4])
            i=sys.argv[1]
            plt.plotfile(i, delimiter=' ', cols=(j-1,k-1))

        else:
            for i in sys.argv:
                if i==sys.argv[1]:
                    plt.plotfile(i, delimiter=' ', cols=(0,1))
                if (i!=sys.argv[1] and i!=sys.argv[0]):
                    plt.plotfile(i, delimiter=' ',newfig=False,cols=(0,1))



plt.xlabel('')
plt.ylabel('')

                    
points_switch=0

for arg in sys.argv:
    if arg=='logx':
        plt.xscale('log')
    elif arg=='logy':
        plt.yscale('log')

    if arg=="points":
        points_switch=1
        

if( points_switch==1 ):
    plotmythings_scatt()
else:
    plotmythings_lines()


plt.show()
