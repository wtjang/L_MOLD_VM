###############################################################################

# 목적 : 설비 로그 Factor 값 중 필요한 부분만 가져와서 ML모델을 활용해 값 예측
# 로그 파일은 Gas, Temp와 관련된 인자 각각 50Set임. 즉 100개의 로그파일 존재
# Gas, Temp 각 로그마다 Factor가 달라서 Gas 로그에서 전처리 하는 코드, Temp 로그에서 전처리 하는 코드 따로 돌려야함. 폴더 경로도 다름.

###############################################################################


#########################################################################
################# 1. 파일 경로 접근 후 데이터 필요 데이터 추출##############
#########################################################################


# Gas 추출

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
    

##########################################################################
########################## 2. Master Table 작성 ##########################
##########################################################################
        
        
result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')

# re_index 해주기 -> index 맞추는 작업 필요 
master = master.reset_index(drop=True)   # Gas
master_2 = master_2.reset_index(drop=True) # Temp 
result = result.reset_index(drop=True)  # Result

# col삭제 del master['stress']

# pd.concat으로 Dataframe 합칠 수 있는데, axis=1이면 col 옆으로 합친다는 뜻
# 열로 붙일때 index 넘버가 같아야댐.. 그래야지 맞춰지더라 그래서 reset_index 쓴거임
final_master_D_R = pd.concat([master, master_2, result['D_R']],axis = 1)


###########################################################################
##################### 3. ML 기법 비교 ######################################
###########################################################################

##################### 3.0 Train / Test / Preprocessing ####################

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


##################### 3.1 KNN - Regression 알고리즘 적용 ####################
# KNN-Regression

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
curve.plot() # k에 따른 rmse 곡선

# graph of acvtual vs pred value

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
from matplotlib import pyplot
from sklearn.model_selection import cross_val_score,KFold
from sklearn.cross_validation import  train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV   #Perforing grid search
from scipy.stats import skew
from collections import OrderedDict
import csv as csv

######################## 3.2 xgboosting 알고리즘 적용 ########################

# XG-Boosting
# No module named 'xgboost' 계속 이거나옴 ㅅㅂ
# anaconda prompt에서 pip install xgboost  이걸로 해결
import xgboost
from xgboost import plot_importance

# for tuning parameters
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

# gride search 하는데 2시간 걸림..;; core수 변경하면 실행이 안되던데.. 그 이유??? 돌렸던 컴퓨터는 20core
#[Parallel(n_jobs=1)]: Done 7776 out of 7776 | elapsed: 120.7min finished
#C:\Users\wtjang\AppData\Local\Continuum\anaconda3\lib\site-packages\xgboost\core.py:587: 
#FutureWarning: Series.base is deprecated and will be removed in a future version
#  if getattr(data, 'base', None) is not None and \
#C:\Users\wtjang\AppData\Local\Continuum\anaconda3\lib\site-packages\xgboost\core.py:588: 
#FutureWarning: Series.base is deprecated and will be removed in a future version
#  data.base is not None and isinstance(data, np.ndarray) \


from joblib import Parallel, delayed
import multiprocessing

xgb_model = xgboost.XGBRegressor(learning_rate =0.1, n_estimators=1000, max_depth=5,  min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, nthread=6, scale_pos_weight=1, seed=27)
gsearch1 = GridSearchCV(estimator = xgb_model, param_grid = parameters_for_testing, n_jobs=10,iid=False, verbose=10,scoring='neg_mean_squared_error')
gsearch1.fit(train_x, train_y)

# n_jobs=-1이면 모든 core 사용, 양수이면 해당분만큼의 코어 수를 쓴다는 뜻인데... 어쩌선지 1아니면 코드 실행이 안됨
# ML의 성능을 끌어올리려면 Hyperparameter tuning이 필요해 grid search가 반드시 필요함.. 근데 한번 돌리는데 2시간이면 시간 너무 낭비됨.
# Multi core 사용할 수 있는 병렬 처리 프로그래밍 조건을 만드는 게 반드시 필요.. 어떻게 돌파함?? 
print (gsearch1.grid_scores_)
print('best params')
print (gsearch1.best_params_)
print('best score')
print (gsearch1.best_score_)

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
xgb_result = best_xgb_model.predict(test_x)


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



































