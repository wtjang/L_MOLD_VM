# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:45:44 2020

@author: wtjang
"""

"""
계측 파일 전처리 함수 
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt 

path_dir = r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일'
file_list = os.listdir(path_dir)
file_list.sort()

f = open(path_dir +  '\\' +  file_list[8]) # 25p 가져오기

lines = f.readlines()
labels = lines[0].split(',') # line 0 : Factor  
df = pd.DataFrame(columns = labels)

for i in range(2, len(lines)):
    temp = lines[i]
    temp = temp.split(',')
    
    df.loc[i-2] = temp

del df[df.iloc[:,-1].name] # 제일 마지막 빈 열 삭제
df_Meta = df.loc[:, ['SLOT', 'LOT ID', 'COLLECTION DATE/TIME', 'RECIPE', 'MATERIAL']]
df_Stat = df.loc[:, ['SLOT','RESULT TYPE', 'MEAN', 'MIN', 'MAX', '% STDDEV', 'STDDEV', '3 % STDDEV', '3 STDDEV', 'RANGE']]
df_Point = df.loc[:, 'DATA[1]':(df.iloc[:,-1]).name]

num_first_Wafer = int(df_Meta.loc[0,'SLOT']) 
num_last_Wafer = int(df_Meta.loc[len(df_Meta)-1,'SLOT'])

num_Wafer =num_last_Wafer - num_first_Wafer + 1
num_Feature = len(df_Meta) / num_Wafer #1st Thickness, 1st RI @ 633.0nm, GOF 등의 개수

df_Meta_final = pd.DataFrame(columns = df_Meta.columns)
for k in range(0, num_Wafer):
    df_Meta_final.loc[k] = df_Meta.loc[k*num_Feature]
   
    
'''
df_10 = df_Point.loc[num_Feature*0:num_Feature*1-1,]
df_11 = df_Point.loc[num_Feature*1:num_Feature*2-1,]
df_12 = df_Point.loc[num_Feature*2:num_Feature*3-1,]

dict 사용해서 loop 돌리는 코드

wafer 숫자가 임의로 들어오기 떄문에 임의의 숫자 n(가령 12라던지)가 들어와도 이를 0으로 시작하는 반복문으로 만들 필요가 있음
이를 계산하려면 i-num_first_Wafer 이 값이 1씩 증가하기 때문에 이를 사용
'i/i = 1, 2i/i = 2' 이런 관계로 표현한거임

output : dict의 key 값은 wafer slot과 동일하고 그 안에는 해당 wafer의 좌표 계측 값이 있음.
25p, 49p 확인완료
'''
df_Point_dict={}
for i in range(num_first_Wafer, num_last_Wafer+1):
    df_Point_dict[i] = df_Point.loc[num_Feature*(i-num_first_Wafer):(num_Feature*(i-num_first_Wafer+1))-1,]




'''
dict에 최종형태로 들어감 x,y,feature col 형태로 삽입
df_Point_finial_dict에 접근하면 됨. df_Point_finail_dict[10] : 10번 Wafer로 접근해서 Dataframe 가져온다

Series to list : values.tolist())
    
df_10_final = pd.DataFrame(columns = ['X','Y'] + (df_Stat.loc[0:num_Feature-1,'RESULT TYPE']).values.tolist())
df_10_T = df_10.T

for point_num in range(0,int(len(df_Point.columns)/3)):
    df_10_final.loc[point_num,'X'] = df_10_T.iloc[3*point_num+1,0]
    df_10_final.loc[point_num,'Y'] = df_10_T.iloc[3*point_num+2,0]
    df_10_final.loc[point_num,(df_Stat.loc[0:num_Feature-1,'RESULT TYPE']).values.tolist()] = df_10_T.iloc[3*point_num,].values.tolist()
'''
df_Point_finial_dict = {}

for i in range(num_first_Wafer, num_last_Wafer+1):
    
    df_Point_finial_dict[i] = pd.DataFrame(columns = ['X','Y'] + (df_Stat.loc[0:num_Feature-1,'RESULT TYPE']).values.tolist()) 
    temp = df_Point_dict[i].T
    
    for point_num in range(0,int(len(df_Point.columns)/3)):
        df_Point_finial_dict[i].loc[point_num,'X'] = temp.iloc[3*point_num+1,0]
        df_Point_finial_dict[i].loc[point_num,'Y'] = temp.iloc[3*point_num+2,0]
        df_Point_finial_dict[i].loc[point_num,(df_Stat.loc[0:num_Feature-1,'RESULT TYPE']).values.tolist()] = temp.iloc[3*point_num,].values.tolist()

    temp = None



'''
df_Point_finial_dict에 접근하면 됨. df_Point_finail_dict[10] : 10번 Wafer로 접근해서 Dataframe 가져온다

1. 좌표를 활용해서 Wafer 위에 안착시켜야함... 
2. Interpolation
3. 이를 시각화
'''

'''
# 22초

test = pd.DataFrame(index=range(0,151), columns=range(0,151))     
for i in range(0,151):
    for j in range(0,151):
        if ((75-i)**2 + (75-j)**2) < 75**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan   
 
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar()   

# 5분정도 걸리는데..  너무 오래걸림.. 축소시켜야댐
test = pd.DataFrame(index=range(0,301), columns=range(0,301))     
for i in range(0,301):
    for j in range(0,301):
        if ((150-i)**2 + (150-j)**2) < 150**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan   
 
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar()   

# 2초
test = pd.DataFrame(index=range(0,51), columns=range(0,51))     
for i in range(0,51):
    for j in range(0,51):
        if ((25-i)**2 + (25-j)**2) < 25**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan   
 
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar()     
'''
import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt

temp_25point = df_Point_finial_dict[20]
temp_25point = temp_25point.loc[:,'X':(temp_25point.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#temp_25point = temp_25point.loc[0:48,]

data = {}

for i in range(0, len(temp_25point)):
    
    data[int(temp_25point.iloc[i,0]),int(temp_25point.iloc[i,1])] = temp_25point.iloc[i,2]

'''
for i in range(0, 49):
    
    data[int(temp_25point.iloc[i,0]),int(temp_25point.iloc[i,1])] = temp_25point.iloc[i,2]
'''    

x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')




'''
2020.05.18 625pt 정합성 테스트
'''

point_625 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\625pt.xlsx', header = 0)

point_625 = point_625[['X','Y','THK']]

data = {}

for i in range(0, len(point_625)):
    
    data[int(point_625.iloc[i,0]),int(point_625.iloc[i,1])] = point_625.iloc[i,2]

x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')


cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 




import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_109 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\new_109.xlsx', header = 0)

point_109 = point_109[['X','Y','THK']]


data = {}

for i in range(0, len(point_109)):
    
    data[int(point_109.iloc[i,0]),int(point_109.iloc[i,1])] = point_109.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

z_ = z_[0:286,]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((143-i)**2 + (143-j)**2) > 143**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')


cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 




'''
25pt
'''

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_25 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\0528_25.xlsx', header = 0)

point_25 = point_25 [['X','Y','THK']]
point_25 = point_25.loc[0:12,]

data = {}

for i in range(0, len(point_25)):
    
    data[int(point_25.iloc[i,0]),int(point_25.iloc[i,1])] = point_25.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

#z_ = z_[0:286,]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')


cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 




matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 147 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 147 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]




'''
73pt
'''

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_73 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\0528_73.xlsx', header = 0)

point_73 = point_73 [['X','Y','THK']]
point_73 = point_73.loc[0:48,]

data = {}

for i in range(0, len(point_73)):
    
    data[int(point_73.iloc[i,0]),int(point_73.iloc[i,1])] = point_73.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

#z_ = z_[0:286,]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((148-i)**2 + (148-j)**2) > 148**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')



matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 147 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 147 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]


'''
313pt
'''

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_313 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\0528_313.xlsx', header = 0)

point_313 = point_313 [['X','Y','THK']]
point_313 = point_313.loc[0:216,]

data = {}

for i in range(0, len(point_313)):
    
    data[int(point_313.iloc[i,0]),int(point_313.iloc[i,1])] = point_313.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

#z_ = z_[0:286,]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((143-i)**2 + (143-j)**2) > 143**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')



matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
#test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 143 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 143 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]













test_1 = point_313.loc[121:168,:]
test_2 = point_313.loc[169:216,:]
test_3 = point_313.loc[217:264,:]
test_4 = point_313.loc[265:312,:]


orginal_r = 147
delta_r = 10

import math
temp_data = test_3.copy()
temp_26_49point = temp_data.copy()

for i in range(217,217+len(temp_26_49point)):
    if (int(temp_26_49point.loc[i,'X']) == 0) | (int(temp_26_49point.loc[i,'Y']) == 0):
        
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] + delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] + delta_r
                      
    else:
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
       
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
        
    
test_1_1 = temp_data
test_2_2 = temp_data
test_3_3 = temp_data


temp_ring = pd.concat([test_1_1,test_2_2, test_3_3, test_4], axis = 0)

data = {}

for i in range(0, len(temp_ring)):
    
    data[int(temp_ring.iloc[i,0]),int(temp_ring.iloc[i,1])] = temp_ring.iloc[i,2]


x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

rbfi = Rbf(x, y, z)
z_ = rbfi(grid_x, grid_y) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) < 117**2:
            z_[i,j] = 0       
          
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')








matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 147 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 147 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]
















































'''
136pt
'''

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_136 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\new_136.xlsx', header = 0)

point_136 = point_136 [['X','Y','THK']]

point_76 = point_136.loc[0:76,]

data = {}

for i in range(0, len(point_76)):
    
    data[int(point_76.iloc[i,0]),int(point_76.iloc[i,1])] = point_76.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

z_ = z_[0:272,0:272]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((136-i)**2 + (136-j)**2) > 136**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')



matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 136 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 136 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]










'''
161pt
'''

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_161 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\new_161.xlsx', header = 0)

point_161 = point_161 [['X','Y','THK']]

point_161 = point_161.loc[0:85,]

data = {}

for i in range(0, len(point_161)):
    
    data[int(point_161.iloc[i,0]),int(point_161.iloc[i,1])] = point_161.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

z_ = z_[0:272,0:272]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((136-i)**2 + (136-j)**2) > 136**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')



matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 147 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 147 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]








test_1 = point_161.loc[61:85,:]
test_2 = point_161.loc[86:110,:]
test_3 = point_161.loc[111:137,:]
test_4 = point_161.loc[138:160,:]


orginal_r = 147
delta_r = 10

import math
temp_data = test_3.copy()
temp_26_49point = temp_data.copy()

for i in range(111,111+len(temp_26_49point)):
    if (int(temp_26_49point.loc[i,'X']) == 0) | (int(temp_26_49point.loc[i,'Y']) == 0):
        
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] + delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] + delta_r
                      
    else:
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
       
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
        
    
test_1_1 = temp_data
test_2_2 = temp_data
test_3_3 = temp_data


temp_ring = pd.concat([test_1_1,test_2_2, test_3_3, test_4], axis = 0)

data = {}

for i in range(0, len(temp_ring)):
    
    data[int(temp_ring.iloc[i,0]),int(temp_ring.iloc[i,1])] = temp_ring.iloc[i,2]


x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

rbfi = Rbf(x, y, z)
z_ = rbfi(grid_x, grid_y) #뒤집어!

z_ = z_[0:287,:]

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) < 117**2:
            z_[i,j] = 0       
          
z_[z_ == 0] = np.nan     



        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')








matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)



orginal_r = 148
delta_r = 10

import math
temp_data = matching.copy()
temp_26_49point = temp_data.copy()

for i in range(0,0+len(temp_26_49point)):
    if (int(temp_26_49point.loc[i,'X']) == 0) | (int(temp_26_49point.loc[i,'Y']) == 0):
        
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] + delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] + delta_r
                      
    else:
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
       
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
        


































temp_data

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = temp_data.copy()

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 148 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 148 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]




































###################### 313

import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


point_313 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\new_313.xlsx', header = 0)

point_313 = point_313 [['X','Y','THK']]


data = {}

for i in range(0, len(point_313)):
    
    data[int(point_313.iloc[i,0]),int(point_313.iloc[i,1])] = point_313.iloc[i,2]



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

#z_ = z_[0:286,]
'''
z_ = z_[0:572,]
'''
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')


cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 




    



matching_2 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching_2.xlsx', header = 0)

matching_2 = matching_2.iloc[:,0:2]


test_matching_2 = matching_2.copy()
test_matching_2["value"] = 0

for i in range(0, len(matching_2)):
    test_matching_2.iloc[i,0] = 147 - matching_2.iloc[i,1]
    test_matching_2.iloc[i,1] = 147 + matching_2.iloc[i,0]

for i in range(0, len(test_matching_2)):
    if (test_matching_2.iloc[i,0] >= 0 ) & (test_matching_2.iloc[i,1] >= 0 ):
        test_matching_2.loc[i,'value'] = z_[int(test_matching_2.iloc[i,0]),int(test_matching_2.iloc[i,1])]



for i in range(0, len(test_matching_2)):
    




int(test_matching_2.iloc[i,0])
int(test_matching_2.iloc[i,1])



z_[int(test_matching_2.iloc[i,0]), int(test_matching_2.iloc[i,1])]




x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_x, grid_y = np.mgrid[minx:maxx:0.1, miny:maxy:0.1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_y, grid_x) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((1470-i)**2 + (1470-j)**2) > 1470**2:
            z_[i,j] = 0
        
z_[z_ == 0] = np.nan  

# Look at it!
#plt.imshow(z_, origin="lower", extent=extent)
#plt.scatter(x, y, s=2, c='w')

plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')














############################################## 73POINT 영역 나눠서


temp_73point = df_Point_finial_dict[20]
temp_73point = temp_73point.loc[:,'X':(temp_73point.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#temp_25point = temp_25point.loc[0:48,]

temp_1_25point = temp_73point.loc[0:24,:]
temp_26_49point = temp_73point.loc[25:48,:]
temp_50_73point = temp_73point.loc[49:72,:]


test_1 = point_136.loc[47:76,:]
test_2 = point_136.loc[77:106,:]
test_3 = point_136.loc[107:136,:]



orginal_r = 147
delta_r = 15

import math
temp_data = test_2.copy()
temp_26_49point = temp_data.copy()

for i in range(77,77+len(temp_26_49point)):
    if (int(temp_26_49point.loc[i,'X']) == 0) | (int(temp_26_49point.loc[i,'Y']) == 0):
        
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] - delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) == 0):
            temp_data.loc[i,'X'] = temp_26_49point.loc[i,'X'] + delta_r
            
        elif (int(temp_26_49point.loc[i,'X']) == 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            temp_data.loc[i,'Y'] = temp_26_49point.loc[i,'Y'] + delta_r
                      
    else:
        if (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
       
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) > 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) < 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = -x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
            
        elif (int(temp_26_49point.loc[i,'X']) > 0) & (int(temp_26_49point.loc[i,'Y']) < 0):
            x1 =  ((orginal_r-delta_r)**2/(1+(abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))**2))**0.5
            y1 = (abs(temp_26_49point.loc[i,'Y']/temp_26_49point.loc[i,'X']))*x1

            temp_data.loc[i,'X'] = x1
            temp_data.loc[i,'Y'] = -y1
            
            del x1, y1
        
    
test_1_1 = temp_data
test_2_2 = temp_data


temp_ring = pd.concat([test_1_1,test_2_2, test_3], axis = 0)

data = {}

for i in range(0, len(temp_ring)):
    
    data[int(temp_ring.iloc[i,0]),int(temp_ring.iloc[i,1])] = temp_ring.iloc[i,2]


x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

rbfi = Rbf(x, y, z)
z_ = rbfi(grid_x, grid_y) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
            

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) < 117**2:
            z_[i,j] = 0       
          
z_[z_ == 0] = np.nan      
        
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')








matching = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\matching.xlsx', header = 0)

matching = matching.iloc[:,0:2]
#matching = matching.iloc[0:313,]

test_matching = matching.copy()
test_matching["value"] = 0

for i in range(0, len(matching)):
    test_matching.iloc[i,0] = 147 - int(matching.iloc[i,1])
    test_matching.iloc[i,1] = 147 + int(matching.iloc[i,0])

for i in range(0, len(test_matching)):
    if (test_matching.iloc[i,0] >= 0 ) & (test_matching.iloc[i,1] >= 0 ):
        test_matching.loc[i,'value'] = z_[int(test_matching.iloc[i,0]),int(test_matching.iloc[i,1])]












'''
# Make the grid.
import heapq
#heapq.nlargest(2,x)
minx, maxx = heapq.nlargest(2,x)[1], heapq.nlargest(2,x)[0]
miny, maxy = heapq.nlargest(2,y)[1], heapq.nlargest(2,y)[0]
extent = (minx, maxx, miny, maxy)
grid_x, grid_y = np.mgrid[minx:maxx:0.1, miny:maxy:0.1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_y, grid_x) #뒤집어!

for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((1470-i)**2 + (1470-j)**2) > 1470**2:
            z_[i,j] = 0
        
z_[z_ == 0] = np.nan  

plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')

cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')
'''


############################################## 109POINT
point_109 = pd.read_excel(r'C:\Users\wtjang\Desktop\프로젝트\20200207 Wafer map\계측 파일\109pt.xlsx', header = 1)

point_109 = point_109[['X','Y','THK']]


edge_s = 130
data = {}
for i in range(0, len(point_109)):
   if (int(point_109.iloc[i,0])**2 + int(point_109.iloc[i,1])**2 > edge_s**2):
       data[int(point_109.iloc[i,0]),int(point_109.iloc[i,1])] = point_109.iloc[i,2]





'''
data = {}

for i in range(0, len(point_109)):
    
    data[int(point_109.iloc[i,0]),int(point_109.iloc[i,1])] = point_109.iloc[i,2]
'''





x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_y, grid_x = np.mgrid[miny:maxy:1, minx:maxx:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y) #뒤집어!

for i in range(0,z_.shape[0]):
    for j in range(0,z_.shape[1]):
        if ((z_.shape[0]/2-i)**2 + (z_.shape[1]/2-j)**2) > max(z_.shape[0]/2,z_.shape[1]/2)**2:
            z_[i,j] = 0
        
for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((z_.shape[0]/2-i)**2 + (z_.shape[1]/2-j)**2) < edge_s**2:
            z_[i,j] = 0   
        
z_[z_ == 0] = np.nan      
    
    
plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar(boundaries=np.linspace(np.nanmin(z_),np.nanmax(z_),10),cmap = 'gist_rainbow_r') 


plt.scatter(x, y, s=20, c='black')




np.nanmax(z_)
np.nanmin(z_)


x=np.random.rand(100)*100
y=np.random.rand(100)*100

xnew = range(100)
ynew = range(100)

z= x*y

interpolants = np.array([xnew, ynew])

from scipy.interpolate import interp1d

znew = scipy.interpolate.griddata((x, y), z, interpolants) 














for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
        
z_[z_ == 0] = np.nan  


#colorbar에서 bin 개수 설정
cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 


















# 6초 이정도는 되야 함 <-> 22초랑 맵 차이 별반 없음
test = pd.DataFrame(index=range(0,101), columns=range(0,101))     
for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan   
 
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar() 





#temp_25point = df_Point_finial_dict[10]
temp_25point = df_Point_finial_dict[17]
temp_25point = temp_25point.loc[:,'X':(temp_25point.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')


#temp_25point.iloc[:,2:2+int(num_Feature)]

temp_25point_scale = pd.concat([temp_25point[['X','Y']]/3+50,temp_25point.iloc[:,2:2+int(num_Feature)]], axis=1)
temp_25point_scale.X = temp_25point_scale.X.round()
temp_25point_scale.Y = temp_25point_scale.Y.round()




test = pd.DataFrame(index=range(0,101), columns=range(0,101))     
for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = 0
        else:
            test.loc[i,j] = np.nan



for i in range(0, len(temp_25point_scale)):
    test.iloc[int(temp_25point_scale.iloc[i,0]),int(temp_25point_scale.iloc[i,1])] = temp_25point_scale.iloc[i,2]
    '''
    test.iloc[int(temp_25point_scale.iloc[i,0]),int(temp_25point_scale.iloc[i,1])+1] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0])+1,int(temp_25point_scale.iloc[i,1])] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0]),int(temp_25point_scale.iloc[i,1])-1] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0])-1,int(temp_25point_scale.iloc[i,1])] = temp_25point_scale.iloc[i,2]
    
    test.iloc[int(temp_25point_scale.iloc[i,0])+1,int(temp_25point_scale.iloc[i,1])+1] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0])+1,int(temp_25point_scale.iloc[i,1])-1] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0])-1,int(temp_25point_scale.iloc[i,1])-1] = temp_25point_scale.iloc[i,2]
    test.iloc[int(temp_25point_scale.iloc[i,0])-1,int(temp_25point_scale.iloc[i,1])+1] = temp_25point_scale.iloc[i,2]
    '''

test = test.apply(pd.to_numeric, errors = 'coerce')


test_df = test.interpolate(method = 'values', limit_direction = 'forward',axix=0)



plt.figure(1)
#plt.imshow(test_df, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
#plt.imshow(test, cmap = 'gist_rainbow_r')
plt.colorbar() 














import numpy as np
from scipy.interpolate import Rbf
%matplotlib inline
import matplotlib.pyplot as plt


data = {(1,3):22, (1,3.5):23, (1,4.5):25, (1.5,3.3):19, (4,4):100}



data = {}

for i in range(0, len(temp_25point)):
    
    data[int(temp_25point.iloc[i,0]),int(temp_25point.iloc[i,1])] = temp_25point.iloc[i,2]
    
    



x = np.array([k[0] for k in data.keys()])
y = np.array([k[1] for k in data.keys()])
z = np.array([v for v in data.values()])
 
# Make the grid.
minx, maxx = np.amin(x), np.amax(x)
miny, maxy = np.amin(y), np.amax(y)
extent = (minx, maxx, miny, maxy)
grid_x, grid_y = np.mgrid[minx:maxx:1, miny:maxy:1]

# Make an n-dimensional interpolator.
rbfi = Rbf(x, y, z)

# Predict on the regular grid.
z_ = rbfi(grid_x, grid_y)

# Look at it!
#plt.imshow(z_, origin="lower", extent=extent)
#plt.scatter(x, y, s=2, c='w')

plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 






for i in range(0,len(z_)):
    for j in range(0,len(z_)):
        if ((147-i)**2 + (147-j)**2) > 147**2:
            z_[i,j] = 0
        
z_[z_ == 0] = np.nan  


#colorbar에서 bin 개수 설정
cmap = plt.get_cmap('jet', 10)
plt.imshow(z_, origin="lower", extent=extent,cmap = cmap)
plt.colorbar() 


plt.imshow(z_, origin="lower", extent=extent,cmap = 'gist_rainbow_r')
plt.colorbar() 
plt.scatter(x, y, s=20, c='black')









for i in range(0,51):
    for j in range(0,51):
        if ((25-i)**2 + (25-j)**2) < 25**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan  



plt.imshow(z_,   vmin = 0, cmap = 'gist_rainbow_r')

plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')

























'''
# pd.concat으로 Dataframe 합칠 수 있는데, axis=1이면 col 옆으로 합친다는 뜻
# 열로 붙일때 index 넘버가 같아야댐.. 그래야지 맞춰지더라 그래서 reset_index 쓴거임
final_master_D_R = pd.concat([master, master_2, result['D_R']],axis = 1)
'''



    

'''
사용자가 만약에 19번 Wafer를 호출한다

num_random_Wafer = 19 # 아마도 나중에 사용자 입력받을 값

df_Meta_final['SLOT'] == str(num_random_Wafer) #이거는 그냥 인넥스 판별용이구
df_Meta_final.loc[df_Meta_final['SLOT'] == str(num_random_Wafer)] # 이걸로 해당하는 데이터 프레임 가져옴


통계량 데이터 프레임에서 임의의 Wafer 번호가 주어지면 그에 해당하는 데이터 프레임 가져옴

df_Stat_T = df_Stat.T
df_Stat_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]
가져오는 형식도 Dataframe 형태임.


데이터 포인트 프레임도 마찬가지

df_Point_T = df_Point.T
df_Point_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]

'''

num_random_Wafer = 12

df_Meta_final.loc[df_Meta_final['SLOT'] == str(num_random_Wafer)]

df_Stat_T = df_Stat.T
df_Stat_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]

df_Point_T = df_Point.T
df_Point_T.loc[:,((num_random_Wafer - num_first_Wafer) * num_Feature):((num_random_Wafer - num_first_Wafer) * num_Feature)+2]




