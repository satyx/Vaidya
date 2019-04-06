import numpy as np

def y_points(x_y,x):
    y_pt= np.zeros(len(x))
    for index,pt in enumerate(x):
        y=0
        if pt>x_y[0][0] and pt<x_y[1][0]:
            y = (x_y[1][1]-x_y[0][1])*(pt-x_y[0][0])/(x_y[1][0]-x_y[0][0])
            y_pt[index]=y
        elif pt>=x_y[1][0] and pt<x_y[2][0]:
            y = (x_y[1][1]-x_y[2][1])*(pt-x_y[1][0])/(x_y[2][0]-x_y[1][0])
            if y>1:
                print('x:',pt)
            y_pt[index]=y
    return y_pt

def correl(d,spl,interval=0.1):
    x_min = min(d[0][0],spl[0][0])
    x_max = max(d[2][0],spl[2][0])
    x = np.arange(x_min,x_max,interval)

    y_d = y_points(d,x)
    y_spl = y_points(spl,x)
    
    cor_mat = y_d*y_spl
    return np.sum(cor_mat)


