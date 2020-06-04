# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:13:34 2020

@author: wtjang
"""

'''
Coding Course
'''



'''
1. Col 이름 변경 {'기존 이름' : '변경 이름'}
'''

df.rename(columns = {'$LOG_ITEM' : 'LOG_ITEM'}, inplace = True) 

'''
2. Col type 변경
'''

df_1 = df.loc[:,'StepNo':(df.iloc[:,-1]).name].apply(pd.to_numeric, errors = 'coerce')
#df의 모든 type을 numeric으로 변경

'''
3. 마지막 col 접근 indexing
'''

df.iloc[:,-1] 
#(df.iloc[:,-1]).name 마지막 col name 접근

'''
4. 조건을 만족하는 row 값
'''

df_5_6step = df_1.loc[(df_1['StepNo'] == 5) | (df_1['StepNo'] == 6)]

'''
5. col 삭제
'''

del df_5_6step["N/A"]

'''
6. line 그래프 
'''
df_5_6step['HFMat2_VDC'].plot(figsize=(8,5)).line()

'''
7. 제곱 계산
'''

x=1
y=2
print(y**y) 

'''
8. 문자열 합치기 쌉가능
'''

print("안녕" + "잘 지내니?")

'''
9. if 구문
'''

if 1 > 2:
    print("hello")

if not 1 > 2:
    print("hello")

if 1>0 and 2>1:
    print("hello")

if 0>0 or 2>1:
    print("hello")

x=3 
if x>5:
    print()    
elif x==3:
    print("Bye")
else:
    print("hi")
    
    
'''
# 10. 함수    
'''

'''
def chat():
    print("철수: 안녕? 넌 몇 살이니?")
    print("영희: 나? 나는 20")

def chat(name1, name2):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 20" % name2)

chat("알렉스", "윤하")
chat("철수", "윤하")
'''
def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age))

chat("알렉스", "윤하", 40)
chat("철수", "윤하", 30)


def dsum(a, b):
    result = a +b
    return result

d=dsum(2,4)
print(d)
    






import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns



base_dir = r'C:\Users\wtjang\Downloads'
excel_file = 'Coin_crack.xlsx'
excel_dir = os.path.join(base_dir, excel_file)


df = pd.read_excel(excel_dir)





plt.rcParams['figure.figsize'] = [10, 8] # setting figure size


sns.scatterplot(x='S_N', y = 'Use_Period(days)', hue = 'Cause', style = 'Cause', s= 100, data=df)
plt.show()


sns.pairplot(x='S_N', y = 'Use_Period(days)', hue = 'Cause', style = 'Cause', s= 100, data=df)
plt.show()


sns.distplot(df[df.Cause == 'Center crack']['Use_Period(days)'], color = 'red', label = 'Center crack')
sns.distplot(df[df.Cause == 'coin crack']['Use_Period(days)'], color = 'green', label = 'coin crack')
sns.distplot(df[df.Cause == '一자 crack']['Use_Period(days)'], color = 'blue', label = ' - shape crack')
plt.legend(title="Cause")
plt.show()


sns.distplot(df[df.S_N >= 307]['Use_Period(days)'], color = 'blue', label = 'S/N > 307')
sns.distplot(df[df.S_N <307]['Use_Period(days)'], color = 'red', label = 'S/N < 307')

plt.legend(title="S/N")
plt.show()






a_1 = df_1[(df_1["Use_Period(days)"] >= 0) & (df_1["Use_Period(days)"] <21)]
a_2 = df_1[(df_1["Use_Period(days)"] >= 21) & (df_1["Use_Period(days)"] <41)]
a_3 = df_1[(df_1["Use_Period(days)"] >= 41) & (df_1["Use_Period(days)"] <61)]
a_4 = df_1[(df_1["Use_Period(days)"] >= 61) & (df_1["Use_Period(days)"] <81)]
a_5 = df_1[(df_1["Use_Period(days)"] >= 81) & (df_1["Use_Period(days)"] <101)]
a_6 = df_1[(df_1["Use_Period(days)"] >= 101) & (df_1["Use_Period(days)"] <121)]
a_7 = df_1[(df_1["Use_Period(days)"] >= 121) & (df_1["Use_Period(days)"] <141)]
a_8 = df_1[(df_1["Use_Period(days)"] >= 141) & (df_1["Use_Period(days)"] <161)]
a_9 = df_1[(df_1["Use_Period(days)"] >= 161) & (df_1["Use_Period(days)"] <181)]
a_10 = df_1[(df_1["Use_Period(days)"] >= 181) & (df_1["Use_Period(days)"] <201)]













































