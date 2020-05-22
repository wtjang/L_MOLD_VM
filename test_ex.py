# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:12:29 2020

@author: wtjang
"""


from wafer_map import wm_app




import pandas as pd
df = pd.read_csv(r'C:\Users\wtjang\Documents\work\aleries.csv')



# dataframe의 row를 list로 변환
data = df.values.tolist() # 49point 

data.append([0,10,3000])
data.append([0,100,3000])
data.append([0,150,3000])


#test

xyz = []
k=20

for i in range(-k,k):
    for j in range(-k,k):
        xyz.append([i,j,j])




wm_app.WaferMapApp(xyz, # data
                    (5,5),#die size (1,1)로 해야지 반지름 150mm 인걸로 만들 수 있음
                   (0,0), # center_xy
                   300, #dia : the wafer diameter
                   edge_excl = 0,
                   flat_excl = 0)


wm_app.WaferMapApp()






import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt


df_2['X']  = df['X'] +150
df_2['Y']  = df['Y'] +150



data_1 = np.array([[ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 1. ,  2. ,  0.1,  2. ,  2. ,  1. ],
       [ 1. ,  2. ,  2. ,  0.1,  2. ,  1. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ]])
    
df = pd.DataFrame(index=range(0,0))     # 빈데이터 프레임

k=300
    
for i in range(0,k):
    for j in range(0,k):
        df.loc[i,j] = i+j
    
    
    



plt.figure(1)
plt.imshow(df ,interpolation='gaussian')
plt.colorbar()



final = pd.concat([df_2, df_2, df_2],axis = 1)





import pylab
pylab.pcolor(v, r, z, cmap='jet')






plt.figure(1)
plt.imshow(final ,interpolation='hanning',cmap = 'seismic')
plt.colorbar()

plt.imshow(final ,interpolation='hanning',cmap = 'seismic')
plt.colorbar()




test = pd.DataFrame(index=range(0,11), columns=range(0,11))     # 빈데이터 프레임


# 제곱할땐 **
for i in range(0,11):
    for j in range(0,11):
        if ((5-i)**2 + (5-j)**2) < 25:
            test.loc[i,j] = 1
        else:
            test.loc[i,j] = 0
            
        
plt.figure(1)
plt.imshow(test ,interpolation='hanning',cmap = 'seismic')
plt.colorbar()       



test = pd.DataFrame(index=range(0,301), columns=range(0,301))     # 빈데이터 프레임



for i in range(0,301):
    for j in range(0,301):
        if ((150-i)**2 + (150-j)**2) < 150**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
            
        
plt.figure(1)
plt.imshow(test ,interpolation='hanning',cmap = 'seismic')
plt.colorbar()       



import numpy as np
test[test == 0] = np.nan
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'seismic')
plt.colorbar() 

# reverse _r 붙이면 쌉가능

plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar() 








from tkinter import *
from tkinter import ttk

root = Tk()

root.title("wtjang")
root.geometry("200x200")




number_entry = ttk.Entry(root, width=20)
number_entry.grid(row=0, columnspan=1)



button1 = ttk.Button(root, text="200")
button1.grid(row=1, column=0)

root.mainloop()




