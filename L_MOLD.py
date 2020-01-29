###############################################################################
###################### log 파일에서 통계량 추출 ################################
###############################################################################

# 0. 파일 경로에 접근해서 각각 들어갈 파일 리스트화
import os
import pandas as pd

path_dir = r'C:\Users\wtjang\Documents\work\L_MOLD_GAS'
file_list = os.listdir(path_dir)
file_list.sort()

result = pd.read_excel(r'C:\Users\wtjang\Documents\work\L_MOLD_result.xlsx')


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
   
   
    
# re_index 해주기 -> index 맞추는 작업 필요 
master = master.reset_index(drop=True)  
result = result.reset_index(drop=True)  

# col삭제
# del master['stress']

# pd.concat으로 Dataframe 합칠 수 있는데, axis=1이면 col 옆으로 합친다는 뜻
# 열로 붙일때 index 넘버가 같아야댐.. 그래야지 맞춰지더라 그래서 reset_index 쓴거임
master = pd.concat([master, result[['D_R','stress']]],axis = 1)



# 3. KNN - Regression 알고리즘 적용

#import required packages
from sklearn.model_selection import train_test_split

from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
%matplotlib inline

# train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
train_data, test_data = train_test_split(master, test_size = 0.2, random_state = 123)

# seperate the independent and target variable on training data
train_x = train_data.drop(columns=['D_R'], axis=1)
train_y = train_data['D_R']

test_x = test_data.drop(columns=['D_R'], axis=1)
test_y = test_data['D_R']


# preprocessing 안했음...ㅎ..

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



plt.plot(test_y.values, color='r')
plt.plot(pred, color='b')



































