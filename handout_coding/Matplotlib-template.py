import numpy as np
import matplotlib.pyplot as plt

def nice_plot(x,y,
    flag_save=True, #save the figure?
    xlabel='x', #x-axis label
    ylabel='y', #y-axis label
    lcolor='red', #line color
    fs=14, #font size
    fname='plot.png'):

    fig, ax = plt.subplots(1,1,figsize=(4,4))
#plot y vs. x
    ax.plot(x,y,color=lcolor,linewidth=1.5)
#label our axes
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)

    plt.show()
#save the plot?
    if(flag_save):
        plt.savefig(fname,bbox_inches='tight',dpi=400)
###################
# define main
###################
def main():
# yay!
    print('Making a plot!')
#make a dummy x variable
    x = np.linspace(0,1,10)
#make a dummy y variable
    y = x**2
#make the plot
    nice_plot(x,y)
###################
# execute main()
###################
if __name__=='__main__':
    main()