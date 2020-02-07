# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Jan 28 09:37:30 2020)---
runfile('C:/Users/wtjang/.spyder-py3/temp.py', wdir='C:/Users/wtjang/.spyder-py3')
df.head(5)
df_1 = df.loc[:,'Recipe_Step_Number':'S2_VAT_Position'].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경

df_1.Time = pd.to_datetime(df.Time) # 타입 변환
df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_1.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_1 = df_1[cols]
df_1.head(5)
df_1.loc[1,1]
df_1.loc(1,1)
df_1(1,1)
df_1[3,3]
df_1(3,3)

df_1[Recipe_Step_Number]
df_1
df_1[Time]
df_1['Recipe_Step_Number' == 6]
df.loc[:4]
df.loc[2:10]
df_1.S2_N2_FLOW.type()
df_1.S2_N2_FLOW.type
df_1.S2_N2_FLOW
df_1.S2_N2_FLOW[:2]
df_1.S2_N2_FLOW[:1]
df_1.S2_N2_FLOW[:1] +1
df_1['Recipe_Step_Number'] == 6
df_2 = df.loc[df_1['Recipe_Step_Number'] == 6]
df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
Gas_Input = ['S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_2[Gas_Input]
df_3 = df_2[Gas_Input]
Gas_Input = ['S1_SiH4_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_3 = df_2[Gas_Input]
Gas_Input = ['S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_3 = df_2[Gas_Input]
Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_3 = df_2[Gas_Input]
df_3.mean()
df_3.var()
df_3.median()
df_3.std()
master = pd.DataFrame(index=range(0,10), columns=['칼럼이름1', '칼럼이름2'])
temp = df_3.std()
temp.loc[2]
temp.loc[1,1]
temp.name
temp.name()
temp.index
temp
temp[1,2]
temp(1,2)
temp.loc[[2, 3]]
df.loc[:4]
temp.loc[:4]
temp
temp[,2]
temp[:,2]
temp.index
answer = temp.index
answer
master.columns = [answer]
answer[1]
master.columns = [answer[1]
]
answer[1]
answer[2]
answer
master.columns = answer
master = pd.DataFrame(index=range(0,10), columns=[answer])
temp_1 = answer(1) + '_sdv'
answer(1).type
answer(1).type()
answer(1)
answer[1]
answer[1].type
answer[1].type()
answer[1] + '_sdv'
answer + '_sdv'
answer_2 = answer + '_sdv'
answer_2[1]
answer_mean = answer + '_mean'
answer_median = answer + '_median'
answer_sdv = answer + '_sdv'
answer_mean
answer_median
answer_sdv
master = pd.DataFrame(index=range(0,10), columns=[answer_mean, answer_median, answer_sdv])
master = pd.DataFrame(index=range(0,10), columns=[[answer_mean, answer_median, answer_sdv]])
temp.mean()
df_3.mean()
temp
answer_mean = answer + '_mean'
value_mean = df_3.mean()

answer_median = answer + '_median'
value_median = df_3.median()

answer_sdv = answer + '_sdv'
value_sdv = df_3.sdv()
answer_mean = answer + '_mean'
value_median = df_3.median()
value_sdv = df_3.sdv()
value_sdv = df_3.std()
answer_std = answer + '_std'
value_std = df_3.std()
answer_mean
master = pd.DataFrame(index=range(0,10), columns=[answer_mean])
master.columns
master.columns[1]
answer_mean
answer_mean[1]
value_mean
vaule_mean(1)
vaule_mean[1]
value_mean[1]
value_mean.type
value_mean.type()
value_mean.values
temp_100 = master.transpose
master.transpose
master.transpose()
temp_100 = master.transpose()
master.loc[1]
master.loc[1] = value_mean.values
master.loc[0] = value_mean.values
temp_mean = pd.DataFrame(index=range(0,10), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,10), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,10), columns=[answer_std])
temp_std.loc[0] = value_std.values
master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
master
%clear
f = open(r'C:\Users\wtjang\Documents\work\201903080435_754_No_He_SiN__2500.log')
lines = f.readlines()
labels = lines[11].split() # line 11 : Factor
import pandas as pd
df = pd.DataFrame(columns = labels)
for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp

df_1 = df.loc[:,'Recipe_Step_Number':end].apply(pd.to_numeric, errors = 'coerce')
df_1 = df.loc[:,'Recipe_Step_Number':df.iloc[:,-1]].apply(pd.to_numeric, errors = 'coerce')
df.iloc[:,-1]
df.iloc[:,-1].Name
(df.iloc[:,-1]).name
df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
df_1.Time = pd.to_datetime(df.Time) # 타입 변환
df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
cols = df_1.columns.tolist()
df_1 = df_1[cols]
df_1.Time = pd.to_datetime(df.Time) # 타입 변환
df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
cols = df_1.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_1 = df_1[cols]
df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]


#뽑을 Factor들을 이미 정의
Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   


df_3 = df_2[Gas_Input]
df_3.index
kk = df_3.std()
kk
df_3.std().index
answer_mean = answer + '_mean'
value_mean = df_3.mean()

answer_median = answer + '_median'
value_median = df_3.median()

answer_std = answer + '_std'
value_std = df_3.std()
answer = df_3.std().index # Factor들 이름만 가져옴
answer_mean = answer + '_mean'
value_mean = df_3.mean()

answer_median = answer + '_median'
value_median = df_3.median()

answer_std = answer + '_std'
value_std = df_3.std()
value_mean.values
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values

temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values

temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values


master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
master = pd.concat([master, master])
%clear
import os
path_dir = 'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()
file_list[0]
path_dir + file_list[0]
f = open(path_dir + file_list[0])
path_dir + '\' +  file_list[0]
file_list[0]
'\' + file_list[0]
"\" + file_list[0]
"\" + file_list[0];
file_list[1]
path_dir
path_dir + file_list[1]
path_dir +  '\\' +  file_list[1]
f = open(path_dir +  '\\' +  file_list[0])
lines = f.readlines()
file.list.size
file_list.size
file_list.size()
file_list.index
file_list.count
size(file_list)
len(file_list)
path_dir +  '\\' +  file_list[0]
%clear
import os
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()
len(file_list)-1
for k in range(0, len(file_list)-1):
k=0
path_dir +  '\\' +  file_list[k]
f = open(path_dir +  '\\' +  file_list[k])
lines = f.readlines()
labels = lines[11].split() # line 11 : Factor

import pandas as pd

df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_1.Time = pd.to_datetime(df.Time) # 타입 변환
df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_1.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_1 = df_1[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_3 = df_2[Gas_Input]

# Factor들 이름만 가져옴
answer = df_3.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_3.mean()
answer_median = answer + '_median'
value_median = df_3.median()
answer_std = answer + '_std'
value_std = df_3.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
master = pd.concat([master, temp_master])
master = temp_master
master = pd.concat([master, temp_master])
k=1
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor

import pandas as pd

df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_1.Time = pd.to_datetime(df.Time) # 타입 변환
df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_1.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_1 = df_1[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
df_3 = df_2[Gas_Input]

# Factor들 이름만 가져옴
answer = df_3.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_3.mean()
answer_median = answer + '_median'
value_median = df_3.median()
answer_std = answer + '_std'
value_std = df_3.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
master = pd.concat([master, temp_master])
%clear
runfile('C:/Users/wtjang/.spyder-py3/temp.py', wdir='C:/Users/wtjang/.spyder-py3')
%clear
import os

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()


for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    import pandas as pd
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_1.Time = pd.to_datetime(df.Time) # 타입 변환
    df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_1 = df_1[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
    df_3 = df_2[Gas_Input]
    
    # Factor들 이름만 가져옴
    answer = df_3.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_3.mean()
    answer_median = answer + '_median'
    value_median = df_3.median()
    answer_std = answer + '_std'
    value_std = df_3.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master = pd.concat([master, temp_master])






















file_list[k]
file_list[49]
file_list[48]
file_list[50]
f.close()
%clear
import os

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()


for k in range(0, len(file_list)-1):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    import pandas as pd
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_1.Time = pd.to_datetime(df.Time) # 타입 변환
    df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_1 = df_1[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position' ]   
    df_3 = df_2[Gas_Input]
    
    # Factor들 이름만 가져옴
    answer = df_3.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_3.mean()
    answer_median = answer + '_median'
    value_median = df_3.median()
    answer_std = answer + '_std'
    value_std = df_3.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master = pd.concat([master, temp_master])






















len(file_list)-1
%clear
runfile('C:/Users/wtjang/.spyder-py3/temp.py', wdir='C:/Users/wtjang/.spyder-py3')
len(file_list)
f.close()
%clear
runfile('C:/Users/wtjang/.spyder-py3/temp.py', wdir='C:/Users/wtjang/.spyder-py3')

## ---(Wed Jan 29 08:47:22 2020)---
runfile('C:/Users/wtjang/.spyder-py3/L_MOLD.py', wdir='C:/Users/wtjang/.spyder-py3')
df_1.loc[2298,1]
df_1.loc(2298,1)
df_1.loc[2298,3]
df_1.loc[3]
df_1.loc[3,1]
df_1.loc[3,2]
df_1.loc[2]
df_1[2,1]
df_1(2,1)

df_1.iloc[2,2]
df_1.iloc[2,1]
df_1.iloc[1,2]
df_1.iloc[1,1]
df_1.iloc[1,2]
df_1.iloc[1,3]
df_1.iloc[1,4]
df_1.iloc[1,5]
df_1.iloc[3]
df_1.iloc[3,1]
df_1.iloc[2298]
df_1.iloc[2297]
df_1.loc[2297, 'Time']
df_1.loc[2297, 'Time'] - df_1.loc[0, 'Time']
df_1.loc[2297, 'Time'] - df_1.loc[1, 'Time']
df_2.loc[2068, 'Time'] - df_2.loc[1269, 'Time']
result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')
master = pd.concat([master, result['D_R', 'stress']])
master['D_R'] = result['D_R']
result['D_R']
master['D_R'] = result['D_R']
result['D_R', 'stress']
result[['D_R', 'stress']]
master = pd.concat([master, result[['D_R', 'stress']]])
master = pd.concat(master, result[['D_R', 'stress']])
master = pd.concat(master, result[['D_R', 'stress']], axis = 1)
master = pd.concat([master, result[['D_R', 'stress']]], axis = 1)
result[['D_R', 'stress']].type
result[['D_R', 'stress']].type()
result[['D_R', 'stress']]
master = pd.concat([master, result[['D_R', 'stress']],] axis=1)
master = pd.concat([master, result[['D_R', 'stress']]], axis=1)
temp_1 = pd.concat([master, [resutlt['D_R', 'stress']])
)
result['D_R', 'stress']
result('D_R', 'stress')
result[['D_R', 'stress']]
temp_1 = result[['D_R', 'stress']]
master.append(result[['D_R', 'stress']])
pd.concat([master, result[['D_R', 'stress']]],axis=1)
pd.concat([master, temp_1],axis=1)
master
temp_1
master
master.loc[3]
master[3]
master(3)
master.index
master = master.reset_index(drop=True)
master.loc[]3
master.loc[3]
pd.concat([master, result['D_R', 'stress']],axis=1)
pd.concat([master, result('D_R', 'stress')],axis=1)
result[['D_R','stress']]
pd.concat([master, result[['D_R','stress']]],axis = 1)
del master['D_R']
temp_1 = temp_1.reset_index(drop = True)
(result[['D_R', 'stress']]).reset.index
result[['D_R', 'stress']]
result = result.reset_index(drop=True)
pd.concat([master, result[['D_R','stress']]],axis = 1)
master = pd.concat([master, result[['D_R','stress']]],axis = 1)
result = result.reset_index(drop=True)  
result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')
result = result.reset_index(drop=True)  
master = pd.concat([master, result[['D_R','stress']]],axis = 1)
del master['D_R', 'stress']
del master[['D_R', 'stress']]
del master['D_R']
del master['stress']
master = pd.concat([master, result[['D_R','stress']]],axis = 1)
result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')
result = result.reset_index(drop=True)  
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(master, test_size = 0.2, random_state = 123)
print('Shape of trainign data : ', train_data.shape)
del master['stress']
train_data, test_data = train_test_split(master, test_size = 0.2, random_state = 123)
train_x = train_data.drop(columns=['D_R'], axis=1)
train_y = train_data['D_R']
test_x = test_data.drop(columns=['D_R'], axis=1)
test_y = test_data['D_R']
model = KneighborsClassifier()
model = KNeighborsClassifier()
model.fit(train_x, train_y)
rmse_val = []

for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)






from sklearn.neighbors import KNeighborsClassifier
rmse_val = []

for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)







from sklearn.neighbors import KNeighborsRegressor
rmse_val = []

for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)




rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)





sqrt(2)
from sklearn import neighbors
import matplotlib.pyplot as plt
%matplotlib inline
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)





from math import sqrt
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)


from sklearn.metrics import mean_squared_error 
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)




from sklearn.model_selection import train_test_split

from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
%matplotlib inline
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val)
curve.plot()
pred
test_y
plot(pred, test_y)
test_y.plot
test_y.plot()
pred
test_y
curve.plot()
import matplotlib.pyplot as plt 
plt.plot(test_y)
plt.plot(test_y.sort_index)
pred
plt.plot(pred)
plt.plot(test_y['D_R'])
test_y['D_R']
test_y
test_y.values
plt.plot(test_y.values)
plt.plot(test_y.values, color='r')
plt.plot(pred, color='b')
plt.plot(test_y.values, color='r')
plt.plot(pred, color='b')
plt.plot(pred, 'pred' ,color = 'b')
plt.plot(test_y.values, color='r')
plt.plot(pred, color='b')
plt.plot(pred, marker = pred,color='b')
plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')
test_y.index
xs = 1:10
xs = [1:10]
xs = [1,2,3,4,5,6,7,8,9,10]
xs
ys = test_y.values
for x, y in zip(xs, ys):
    label = y
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",))

for x, y in zip(xs, ys):
    label = y
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points")

xs = np.arange(0,10,1)
import np from numpy
from np import numpy
import numpy as np
xs = np.arange(0,10,1)
ys
xs
for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')   

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'left')    

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'left')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'left') 

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,10),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'left') 

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,3),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,3),
                 ha = 'left') 

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,3),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-5),
                 ha = 'left') 

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center')    

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center')   

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 col = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center')  

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center') 

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center'
                 color = 'b')    

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-10),
                 ha = 'center',
                 color = 'b')    

plt.plot(test_y.values, color='r')
plt.plot(pred,color='b')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-20),
                 ha = 'center',
                 color = 'b')  

plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,5),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,-20),
                 ha = 'center',
                 color = 'b')    

plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')    

ys
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range(0,1))
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
train_x_scaled = scaler.fit_transform(train_x)
train_x = pd.DataFrame(train_x_scaled)
test_x_scaled = scaler.fit_transform(test_x)
test_x = pd.DataFrame(test_x_scaled)
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val)
curve.plot()
plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')    

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'CHUCK POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
k=1
f = open(path_dir +  '\\' +  file_list[k])
f
lines = f.readlines()
labels = lines[11].split() # line 11 : Factor
df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp

df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
f.close()
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'CHUCK POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'S1_CHUCK POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
K=0
(path_dir +  '\\' +  file_list[k])
k=0
(path_dir +  '\\' +  file_list[k])
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp

df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]
df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]
answer = df_6.std().index 
answer
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()
value_mean
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values
temp_std
temp_master
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
k
if k ==0:
    master_2 = temp_master # 제일 처음에만    

# log 50개를 누적해서 50row로 만드는게 목적
#조건문으로 들어가게 해줘야함
else:
    master_2 = pd.concat([master_2, temp_master])
k=1
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp

df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]

# Factor들 이름만 가져옴
answer = df_6.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values
df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]
df_5 = df_4.loc[df_1['Recipe_Step_Number'] == 6]
df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]

# Factor들 이름만 가져옴
answer = df_6.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
if k ==0:
    master_2 = temp_master # 제일 처음에만    

# log 50개를 누적해서 50row로 만드는게 목적
#조건문으로 들어가게 해줘야함
else:
    master_2 = pd.concat([master_2, temp_master])
k
k=2
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]

# Factor들 이름만 가져옴
answer = df_6.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)


if k ==0:
    master_2 = temp_master # 제일 처음에만    

# log 50개를 누적해서 50row로 만드는게 목적
#조건문으로 들어가게 해줘야함
else:
    master_2 = pd.concat([master_2, temp_master])
k=0
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]
df_6['Impedence'] = sqrt(df['HF_R_A'] * df['HF_R_A'] + df['HF_X_A'] * df['HF_X_A'])
df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])
df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])
df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']
27.397*27.397
sqrt(27.397*27.397)
sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])
sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']
df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'
]
sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])
(sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])).astype(float)
df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A'])
df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']
df_6['Impedence'] = df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']
sqrt(df_6['Impedence'])
df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
sqrt(3.17*3.17 + 27.397*27.5798)
sqrt(3.17*3.17 + 27.397*27.397)
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
del df_6['HF_R_A']
del df_6['HF_X_A']
answer = df_6.std().index
answer
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
k=0
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]

# Impedence 계산
# df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
# sqrt 쓰면 cannot convert the series to <class 'float'> 오류남

df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)

del df_6['HF_R_A']
del df_6['HF_X_A']


# Factor들 이름만 가져옴
answer = df_6.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
if k ==0:
    master_2 = temp_master # 제일 처음에만    

# log 50개를 누적해서 50row로 만드는게 목적
#조건문으로 들어가게 해줘야함
else:
    master_2 = pd.concat([master_2, temp_master])
k=1
f = open(path_dir +  '\\' +  file_list[k])

lines = f.readlines()
labels = lines[11].split() # line 11 : Factor



df = pd.DataFrame(columns = labels)

for i in range(13, len(lines)):
    temp = lines[i]
    temp = temp.split()
    temp_date = temp[0] + ' ' + temp[1]
    
    del temp[0]
    del temp[0]
    
    temp.insert(0, temp_date)
    
    df.loc[i-12] = temp


df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')

#df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
#col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
#제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱

df_4.Time = pd.to_datetime(df.Time) # 타입 변환
df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})

#Dataframe에서 col 순서 바꾸기(end col -> first col으로)
cols = df_4.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_4 = df_4[cols]

#df_1에서 모든 log 분할 완성 

# 2. 특정 Step 값만 가져오기

# 6Step만 선택
df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]

#뽑을 Factor들을 이미 정의
Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
df_6 = df_5[Temp_Input]

# Impedence 계산
# df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
# sqrt 쓰면 cannot convert the series to <class 'float'> 오류남

df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)

del df_6['HF_R_A']
del df_6['HF_X_A']


# Factor들 이름만 가져옴
answer = df_6.std().index 

# 통계량 접미사 만들고 통계량 추출
answer_mean = answer + '_mean'
value_mean = df_6.mean()
answer_median = answer + '_median'
value_median = df_6.median()
answer_std = answer + '_std'
value_std = df_6.std()

# 1줄로 추출
temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
temp_mean.loc[0] = value_mean.values
temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
temp_median.loc[0] = value_median.values
temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
temp_std.loc[0] = value_std.values

# log 한개당 한줄로 추출
temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)


if k ==0:
    master_2 = temp_master # 제일 처음에만    

# log 50개를 누적해서 50row로 만드는게 목적
#조건문으로 들어가게 해줘야함
else:
    master_2 = pd.concat([master_2, temp_master])
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_4 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Impedence 계산
    # df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
    # sqrt 쓰면 cannot convert the series to <class 'float'> 오류남
    
    df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
    
    del df_6['HF_R_A']
    del df_6['HF_X_A']
    
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
master_2.reset_index
%clear
import os
import pandas as pd

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):



# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor  
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_1.Time = pd.to_datetime(df.Time) # 타입 변환
    df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_1 = df_1[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 
                 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position','HF_FORWARD_A','HF_REFLECT_A']   
    df_3 = df_2[Gas_Input]
    
    df_3['Delivery_Power'] = df_3['HF_FORWARD_A'] - df_3['HF_REFLECT_A']
    
    del df_3['HF_FORWARD_A']
    del df_3['HF_REFLECT_A']
    
    # Factor들 이름만 가져옴
    answer = df_3.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_3.mean()
    answer_median = answer + '_median'
    value_median = df_3.median()
    answer_std = answer + '_std'
    value_std = df_3.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master = pd.concat([master, temp_master])


path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):


# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    df_temp = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df_temp.loc[i-12] = temp
    
    df_4 = df_temp.loc[:,'Recipe_Step_Number':(df_temp.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df_4.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Impedence 계산
    # df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
    # sqrt 쓰면 cannot convert the series to <class 'float'> 오류남
    
    df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
    
    del df_6['HF_R_A']
    del df_6['HF_X_A']
    
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])
path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):


# 1. log파일 분할시키기

#f = open(r'C:\Users\wtjang\Documents\work\L_MOLD_GAS\201903080435_754_No_He_SiN__2500.log')
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    df_temp = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df_temp.loc[i-12] = temp
    
    df_4 = df_temp.loc[:,'Recipe_Step_Number':(df_temp.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_4.Time = pd.to_datetime(df_temp.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 2. 특정 Step 값만 가져오기
    
    # 6Step만 선택
    df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 이미 정의
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Impedence 계산
    # df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
    # sqrt 쓰면 cannot convert the series to <class 'float'> 오류남
    
    df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
    
    del df_6['HF_R_A']
    del df_6['HF_X_A']
    
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])


# 로그 Table 완성
result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')
master = master.reset_index(drop=True)  
master_2 = master_2.reset_index(drop=True)  
result = result.reset_index(drop=True)  
finial_master = pd.concat([master, master_2, result['D_R']],axis = 1)
finial_master_D_R = pd.concat([master, master_2, result['D_R']],axis = 1)
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
train_data, test_data = train_test_split(final_master_D_R, test_size = 0.2, random_state = 123)
final_master_D_R = pd.concat([master, master_2, result['D_R']],axis = 1)
train_data, test_data = train_test_split(final_master_D_R, test_size = 0.2, random_state = 123)
train_x = train_data.drop(columns=['D_R'], axis=1)
train_y = train_data['D_R']

test_x = test_data.drop(columns=['D_R'], axis=1)
test_y = test_data['D_R']
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

train_x_scaled = scaler.fit_transform(train_x)
train_x = pd.DataFrame(train_x_scaled)

test_x_scaled = scaler.fit_transform(test_x)
test_x = pd.DataFrame(test_x_scaled)
for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)


from sklearn import neighbors
rmse_val = []

for K in range(20):
    K = K+1
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)


rmse_val = []

for K in range(20):
    K = K+1
    from sklearn import neighbors
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

rmse_val = []

for K in range(20):
    K = K+1
    from sklearn import neighbors
    model = sklearn.neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)


rmse_val = []

for K in range(20):
    K = K+1
    
    model = sklearn.neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

rmse_val = []

for K in range(20):
    K = K+1
    
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

import sklearn
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
rmse_val = []

for K in range(20):
    K = K+1
    
    model = KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

rmse_val = []

for K in range(20):
    K = K+1
    
    model = sklearn.neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val)
curve.plot()
plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')    

# plt.title("sin & cos") # 제목

# git test
import xgboost
import csv as csv
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score,KFold
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from scipy.stats import skew
from collections import OrderedDict
import xgboost
anaconda search -t conda xgboost
import xgboost
import csv as csv
from xgboost import plot_importance
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score,KFold
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from scipy.stats import skew
from collections import OrderedDict
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score,KFold
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from scipy.stats import skew
from collections import OrderedDict
import csv as csv
from xgboost import plot_importance
import xgboost
from xgboost import plot_importance
import xgboost
from xgboost import plot_importance
import xgboost
from xgboost import plot_importance
parameters_for_testing = {
    'colsample_bytree':[0.4,0.6,0.8],
    'gamma':[0,0.03,0.1,0.3],
    'min_child_weight':[1.5,6,10],
    'learning_rate':[0.1,0.07],
    'max_depth':[3,5],
    'n_estimators':[10000],
    'reg_alpha':[1e-5, 1e-2,  0.75],
    'reg_lambda':[1e-5, 1e-2, 0.45],
    'subsample':[0.6,0.95]  
}
min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, 
subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=6,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x_scaled,train_y)
gsearch1.fit(train_x,train_y)
gsearch1.fit(train_x_scaled,train_y)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=1,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
print (gsearch1.grid_scores_)
print('best params')
print (gsearch1.best_params_)
print('best score')
print (gsearch1.best_score_)
seed = 42)
best_xgb_model = xgboost.XGBRegressor(colsample_bytree = 0.8,
                                      gamma = 0.3,
                                      learning_rate = 0.1,
                                      max_depth =3,
                                      min_child_wright = 1.5,
                                      n_estimators = 10000,
                                      reg_alpha = 0.75,
                                      reg_lambda = 0.45,
                                      subsample = 0.6,
                                      seed = 42)
best_xgb_model.fit(train_x, train_y)
best_xgb_model.predict(test_x)
test_y
xgb_result = best_xgb_model.fit(train_x, train_y)
xgb_result
xgb_result = best_xgb_model.predict(test_x)
xgb_result
plt.plot(test_y.values, 'ro-')
plt.plot(xgb_result, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = xgb_result

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')  

gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=2,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=20,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
if _name_ == '_main_':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

if __name__=='__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

if __name__ == '__main__'
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

if __name__ == '__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

if __name__ == '__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=5,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

if __name__ == '__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=-1,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=-1,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
from joblib import Parallel, delayed
import multiprocessing
xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
from joblib import Parallel, delayed
if __name__ == '__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

import multiprocessing
from joblib import Parallel, delayed
import joblib
from joblib import Parallel, delayed
import multiprocessing
from joblib import Parallel, delayed
import multiprocessing
if __name__ == '__main__':
    xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
    gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
    gsearch1.fit(train_x, train_y)

xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)
rmse_val
curve
curve.type()
curve.type
plt.plot(test_y.values, 'ro-')
plt.plot(xgb_result, 'bo-')

import numpy as np

xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = xgb_result

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')  


## ---(Mon Feb  3 14:23:15 2020)---
runfile('C:/Users/wtjang/.spyder-py3/test.py', wdir='C:/Users/wtjang/.spyder-py3')
1+1
runfile('C:/Users/wtjang/.spyder-py3/test.py', wdir='C:/Users/wtjang/.spyder-py3')
runfile('C:/Users/wtjang/.spyder-py3/test_ex.py', wdir='C:/Users/wtjang/.spyder-py3')
python example.py
runfile('C:/Users/wtjang/.spyder-py3/test_ex.py', wdir='C:/Users/wtjang/.spyder-py3')
from wafer_map import wm_app
import wm_app
%clear
import wm_app
pip list
import wafer_map
data = [(1,1, 20), 
data = [(1,1, 20), (3,3,10)]
wafer_map.wm_app.WaferMapApp(data)
wafer_map.wm_app.WaferMapApp(data,10,(0,0), 150,2,2)
wm_app.WaferMapApp(data,10,(0,0), 150,2,2)
import wm_app
import numpy
import colour
import wm_app
import wafer_map
import wafer_map.wm_app
wm_app.WaferMapApp(data,10,(0,0), 150,2,2)
import wm)app
import wm_app
from wafer_map import wm_app
data = [(1,1, 20), (3,3,10)]
wm_app.WaferMapApp(data,10,(0,0), 150,2,2)
wm_app.WaferMapApp(data)
wm_app.WaferMapApp(data, (1,1))
(-67.1751,	67.1751,	2014.9639),
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	2014.9639),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
%clear
from wafer_map import wm_app
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	2014.9639),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
wm_app.WaferMapApp(data, (1,1))
wm_app.WaferMapApp(data, (150,150))
wm_app.WaferMapApp(data, (150,150),(0,0),150)
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	1000),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
rMapApp(data, (150,150),(0,0),150)
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	1000),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
wm_app.WaferMapApp(data, (150,150),(0,0),150)
wm_app.WaferMapApp(data, (20,20),(0,0),150)
wm_app.WaferMapApp(data, (1,1),(0,0),150)
wm_app.WaferMapApp(data, (1,1),(0,0),100)
wm_app.WaferMapApp(data, (1,1),(0,0),150)

## ---(Wed Feb  5 16:35:33 2020)---
import os
import pandas as pd

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):    


# log파일 분할시키기
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor  
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    #Step부터 end col factor까지 numeric으로 타입 
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_1.Time = pd.to_datetime(df.Time) # 타입 변환
    df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_1 = df_1[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 특정 Step 값만 가져오기
    
    # 6Step만 선택 - Depo Step
    df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 사전 정의 - based on domain knowledge
    #Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 
    #             'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position','HF_FORWARD_A','HF_REFLECT_A']  
    
    Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 
                  'S1_VAT_Pressure', 'HF_FORWARD_A','HF_REFLECT_A']   
    df_3 = df_2[Gas_Input]
    
    df_3['Delivery_Power'] = df_3['HF_FORWARD_A'] - df_3['HF_REFLECT_A']
    
    del df_3['HF_FORWARD_A']
    del df_3['HF_REFLECT_A']
    
    # Factor들 이름만 가져옴
    answer = df_3.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_3.mean()
    answer_median = answer + '_median'
    value_median = df_3.median()
    answer_std = answer + '_std'
    value_std = df_3.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master = pd.concat([master, temp_master])


# Temp 추출

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    df_temp = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df_temp.loc[i-12] = temp
    
    df_4 = df_temp.loc[:,'Recipe_Step_Number':(df_temp.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    df_4.Time = pd.to_datetime(df_temp.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    # 6Step만 선택
    df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 사전 정의
    #Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Impedence 계산
    # df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
    # sqrt 쓰면 cannot convert the series to <class 'float'> 오류남
    
    df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
    
    del df_6['HF_R_A']
    del df_6['HF_X_A']
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])

result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')
master = master.reset_index(drop=True)   # Gas
master_2 = master_2.reset_index(drop=True) # Temp 
result = result.reset_index(drop=True)  # Result
final_master_D_R = pd.concat([master, master_2, result['D_R']],axis = 1)
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt

# train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
train_data, test_data = train_test_split(final_master_D_R, test_size = 0.2, random_state = 123)

# seperate the independent and target variable on training data
train_x = train_data.drop(columns=['D_R'], axis=1)
train_y = train_data['D_R']

test_x = test_data.drop(columns=['D_R'], axis=1)
test_y = test_data['D_R']

# Preprocessing 전처리 한게 더 오차율 좋음 RMSE 100감소
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

train_x_scaled = scaler.fit_transform(train_x)
train_x = pd.DataFrame(train_x_scaled)

test_x_scaled = scaler.fit_transform(test_x)
test_x = pd.DataFrame(test_x_scaled)
rmse_val = []

for K in range(20):
    K = K+1
    
    model = sklearn.neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

rmse_val = []
for K in range(20):
    K = K+1
    
    model = sklearn.neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

for K in range(20):
    K = K+1
    
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    error = sqrt(mean_squared_error(test_y, pred))
    rmse_val.append(error)
    print('RMSE value for k = ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val)
curve.plot() # k에 따른 rmse 곡선
plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np
xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')  

K
K=4
model = neighbors.KNeighborsRegressor(n_neighbors = K)
model.fit(train_x, train_y)
pred = model.predict(test_x)
error = sqrt(mean_squared_error(test_y, pred))
error
plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')
plt.plot(test_y.values, 'ro-')
plt.plot(pred, 'bo-')

import numpy as np
xs = np.arange(0,10,1)
ys = test_y.values

for x, y in zip(xs, ys):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'r')


ys_1 = pred

for x, y in zip(xs, ys_1):
    label = "{:.2f}".format(y)
    
    plt.annotate(label,
                 (x,y),
                 textcoords = "offset points",
                 xytext=(0,20),
                 ha = 'center',
                 color = 'b')    

rmse_val
import os
import pandas as pd

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):    


# log파일 분할시키기
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor  
    
    df = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df.loc[i-12] = temp
    
    df_1 = df.loc[:,'Recipe_Step_Number':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    #Step부터 end col factor까지 numeric으로 타입 
    #df_1 = df.apply(pd.to_numeric, errors = 'coerce') 
    #col값을 numeric으로 변경하는데, numerice으로 변경 안되는건 NaN으로 변경
    #제일 마지막 칼럼 이름을 지정해줘야 하는데 (df.iloc[:,-1]).name 이걸로 인덱싱
    
    df_1.Time = pd.to_datetime(df.Time) # 타입 변환
    df_1['Time'] = pd.DataFrame({'Time' : df_1.Time})
    
    #Dataframe에서 col 순서 바꾸기(end col -> first col으로)
    cols = df_1.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_1 = df_1[cols]
    
    #df_1에서 모든 log 분할 완성 
    
    # 특정 Step 값만 가져오기
    
    # 6Step만 선택 - Depo Step
    df_2 = df_1.loc[df_1['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 사전 정의 - based on domain knowledge
    Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 
                 'S1_P0_PRESS', 'S1_P1_PRESS', 'S1_VAT_Pressure', 'S1_VAT_Position','HF_FORWARD_A','HF_REFLECT_A']  
    
    #Gas_Input = ['Time', 'S1_NH3_FLOW','S1_SiH4_FLOW', 'S1_N2_FLOW', 'S1_Ar_Flow(Teos)', 
    #              'S1_VAT_Pressure', 'HF_FORWARD_A','HF_REFLECT_A']   
    df_3 = df_2[Gas_Input]
    
    df_3['Delivery_Power'] = df_3['HF_FORWARD_A'] - df_3['HF_REFLECT_A']
    
    del df_3['HF_FORWARD_A']
    del df_3['HF_REFLECT_A']
    
    # Factor들 이름만 가져옴
    answer = df_3.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_3.mean()
    answer_median = answer + '_median'
    value_median = df_3.median()
    answer_std = answer + '_std'
    value_std = df_3.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    
    if k ==0:
        master = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master = pd.concat([master, temp_master])


# Temp 추출

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_TEMP'
file_list = os.listdir(path_dir)
file_list.sort()

for k in range(0, len(file_list)):
    
    f = open(path_dir +  '\\' +  file_list[k])
    
    lines = f.readlines()
    labels = lines[11].split() # line 11 : Factor
    
    df_temp = pd.DataFrame(columns = labels)
    
    for i in range(13, len(lines)):
        temp = lines[i]
        temp = temp.split()
        temp_date = temp[0] + ' ' + temp[1]
        
        del temp[0]
        del temp[0]
        
        temp.insert(0, temp_date)
        
        df_temp.loc[i-12] = temp
    
    df_4 = df_temp.loc[:,'Recipe_Step_Number':(df_temp.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
    df_4.Time = pd.to_datetime(df_temp.Time) # 타입 변환
    df_4['Time'] = pd.DataFrame({'Time' : df_4.Time})
    
    cols = df_4.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_4 = df_4[cols]
    
    # 6Step만 선택
    df_5 = df_4.loc[df_4['Recipe_Step_Number'] == 6]
    
    #뽑을 Factor들을 사전 정의
    Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'FORE_BARA_GAUGE','HEAT_EX_TEMP_A' ,'HF_R_A', 'HF_X_A' ]   
    #Temp_Input = ['Time', 'S1_CHUCK_POSITION', 'HF_R_A', 'HF_X_A' ]   
    df_6 = df_5[Temp_Input]
    
    # Impedence 계산
    # df_6['Impedence'] = sqrt(df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) 
    # sqrt 쓰면 cannot convert the series to <class 'float'> 오류남
    
    df_6['Impedence'] = (df_6['HF_R_A'] * df_6['HF_R_A'] + df_6['HF_X_A'] * df_6['HF_X_A']) ** (1/2)
    
    del df_6['HF_R_A']
    del df_6['HF_X_A']
    
    # Factor들 이름만 가져옴
    answer = df_6.std().index 
    
    # 통계량 접미사 만들고 통계량 추출
    answer_mean = answer + '_mean'
    value_mean = df_6.mean()
    answer_median = answer + '_median'
    value_median = df_6.median()
    answer_std = answer + '_std'
    value_std = df_6.std()
    
    # 1줄로 추출
    temp_mean = pd.DataFrame(index=range(0,0), columns=[answer_mean])
    temp_mean.loc[0] = value_mean.values
    temp_median = pd.DataFrame(index=range(0,0), columns=[answer_median])
    temp_median.loc[0] = value_median.values
    temp_std = pd.DataFrame(index=range(0,0), columns=[answer_std])
    temp_std.loc[0] = value_std.values
    
    # log 한개당 한줄로 추출
    temp_master = pd.concat([temp_mean, temp_median, temp_std], axis = 1)
    
    if k ==0:
        master_2 = temp_master # 제일 처음에만    
    # log 50개를 누적해서 50row로 만드는게 목적
    #조건문으로 들어가게 해줘야함
    else:
        master_2 = pd.concat([master_2, temp_master])


## ---(Fri Feb  7 10:45:44 2020)---
from wafer_map import wm_app
wm_app.WaferMapApp(data, 9,(1,1),(0,0),150)
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	1000),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
wm_app.WaferMapApp(data, 9,(1,1),(0,0),150)
wm_app.WaferMapApp(data, (9,9),(1,1),(0,0),150)
wm_app.WaferMapApp(data, (1,1),(0,0),150)
from wafer_map import wm_app
data = [(0,0, 1969.493), 
        (0,95,2014.453),
        (-67.1751,	67.1751,	1000),
        (-95,	0,	2015.6959),
        (-67.1751,	-67.1751,	2014.524),
        (0	,-95,	2014.9785),
        (67.1751,	-67.1751,	2041.684),
        (95,	0,	2043.2437),
        (67.1751,	67.1751,2041.6567)
        ]
wm_app.WaferMapApp(data, (1,1),(0,0),150)
import numpy
data_1 = np.array([[ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 1. ,  2. ,  0.1,  2. ,  2. ,  1. ],
       [ 1. ,  2. ,  2. ,  0.1,  2. ,  1. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ]])
import numpy as np
data_1 = np.array([[ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 1. ,  2. ,  0.1,  2. ,  2. ,  1. ],
       [ 1. ,  2. ,  2. ,  0.1,  2. ,  1. ],
       [ 0. ,  1. ,  1. ,  1. ,  1. ,  0. ],
       [ 0. ,  0. ,  1. ,  1. ,  0. ,  0. ]])
plt.figure(1)
import matplotlib
plt.figure(1)
import matplotlib as mpl
import matplotlib.pylab as plt
plt.figure(1)
plt.imshow(data_1 ,interpolation='none')
plt.colorbar()
plt.figure(1)
plt.colorbar()
plt.imshow(data_1 ,interpolation='gaussian')