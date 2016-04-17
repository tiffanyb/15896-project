import numpy as np
import matplotlib.pyplot as pl

def plot_ne(d,p1,p2,q):
    x = np.arange(0.0, 1.05, 0.05)
    y1 = d*x
    y2 = (d+p1*(2*q-1))*x+p1
    y3 = (d-p2*(2*q-1))*x+p2
    y3 = np.minimum(y3,[1 for i in x])
    y4 = [1 for i in x]
    y5 = np.minimum(y2,y3)
    y6 = np.maximum(y2,y3)
    y6 = np.minimum(y6,[1 for i in x])
    fig, ax = pl.subplots(1, 1)
    pl.ylim(0,1.2)
    ax.plot(x,y1,"black",x,y2,"yellow",x,y3,"blue",x,y4,"black")
    ax.fill_between(x,y2,y3,where=y3<=y2,facecolor="yellow")
    ax.fill_between(x,y3,y2,where=y3>y2,facecolor="blue")
    ax.fill_between(x,y1,y5,facecolor="green")
    ax.fill_between(x,y6,y4,facecolor="gray")
    ax.fill_between(x,y1,[0 for i in x],facecolor="pink")
    pl.show()
    return 0



