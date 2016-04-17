import numpy as np
import matplotlib.pyplot as pl
from matplotlib.animation import FuncAnimation

def plot_ne(num, ax, d=0.5,p1=0.9,p2=0.2,q=0):
    q=q+num/10.0
    print d, p1, p2, q
    ax.clear()
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
    ax.plot(x,y1,"black",x,y2,"yellow",x,y3,"blue",x,y4,"black",
            alpha=0)
    ax.fill_between(x,y2,y3,where=y3<=y2,facecolor="yellow",
            lw=0.0)
    ax.fill_between(x,y3,y2,where=y3>y2,facecolor="blue", lw=0.0)
    ax.fill_between(x,y1,y5,facecolor="green", lw=0.0)
    ax.fill_between(x,y6,y4,facecolor="gray", lw=0.0)
    ax.fill_between(x,y1,[0 for i in x],facecolor="pink", lw=0.0)
    pl.xlabel(r'$\gamma$',fontsize=20)
    pl.ylabel(r'$1-c$',fontsize=20)
    return ax



def animate():
    fig, ax = pl.subplots()
    pl.xlabel('test')
    anim = FuncAnimation(fig, plot_ne, 10, interval=50, blit=False,
            fargs=(ax, 0.5, 0.9, 0.2, 0))
    # plot_ne(0, ax)
    pl.show()

if __name__ == "__main__":
    animate()
