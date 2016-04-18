import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as pl
from matplotlib.animation import FuncAnimation

def plot_ne(num, ax, d=0.5,p1=0.9,p2=0.2,q=0):
    if num <=100:
        q=num/100.0
    else:
        q=1-(num-100)/100.0

    print d, p1, p2, q
    ax.clear()

#    red_patch = mpatches.Patch(color='gold', label='Disclose, Attack')
#    pl.legend(handles=[red_patch])
    x = np.arange(0.0, 1.01, 0.01)
    y1 = d*x
    y1 = np.minimum(y1,[1 for i in x])
    y2 = (d+p1*(2*q-1))*x+p1
    y2 = np.minimum(y2,[1 for i in x])
    y3 = (d-p2*(2*q-1))*x+p2
    y3 = np.minimum(y3,[1 for i in x])
    y4 = [1 for i in x]
    y5 = np.minimum(y2,y3)
    y6 = np.maximum(y2,y3)
    y6 = np.minimum(y6,[1 for i in x])
    ax.set_ylim(top=1.2)
    ax.fill_between(x,y2,y3,where=y3<=y2,facecolor="gold",
            lw=0.0, alpha=0.7)
    blue = "#1f77b4"
    ax.fill_between(x,y3,y2,where=y3>y2,facecolor=blue,
            lw=0.0, alpha=0.7)
    ax.fill_between(x,y1,y5,facecolor="yellowgreen", lw=0.0, alpha=0.7)
    ax.fill_between(x,y6,y4,facecolor="#9467bd", lw=0.0, alpha=0.7)
    ax.fill_between(x,y1,[0 for i in x],facecolor="#ff9896",
            lw=0.0, alpha=0.7)
    pl.xlabel(r'$\gamma$',fontsize=20)
    pl.ylabel(r'$1-c$',fontsize=20)
    yellow_patch = mpatches.Patch(color='gold', alpha=0.7, label='Attack, Disclose')
    blue_patch = mpatches.Patch(color=blue, alpha=0.7, label='Disclose, Attack')
    green_patch = mpatches.Patch(color='yellowgreen', alpha=0.7,
            label='Disclose, Attack & Attack, Disclose')
    red_patch = mpatches.Patch(color='#ff9896', alpha=0.7,
            label='Disclose, Disclose')
    purple_patch = mpatches.Patch(color='#9467bd', alpha=0.7,
            label='Attack, Attack')

    ax.legend(handles=[red_patch, yellow_patch, green_patch, blue_patch,
              purple_patch],loc="center left",bbox_to_anchor=(1.05,0.5))
    # ax.plot(x,y1,"black",x,y2,"yellow",x,y3,"blue",x,y4,"black",
    #        alpha=0)

    return ax



def animate():
    fig, ax = pl.subplots()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])  
    anim = FuncAnimation(fig, plot_ne, 200, interval=25, blit=False,
            fargs=(ax, 0.5, 0.9, 0.2, 0))
    # plot_ne(0, ax)
    pl.show()

if __name__ == "__main__":
    animate()
