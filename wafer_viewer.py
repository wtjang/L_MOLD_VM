# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:55:41 2020 ~

@author: wtjang
"""

"""
Wafer viewer를 개발 중입니다. 
PyQt5를 사용해서 User가 Interactive하게 사용할 수 있는 프로그램을 개발 중입니다.
http://blog.rcnelson.com/building-a-matplotlib-gui-with-qt-designer-part-2/ 를 참고중
"""
import sys
import os
import pandas as pd 
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt    
from PyQt5.QtWidgets import *    
from PyQt5.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, 
                             QTableWidget, QTableWidgetItem, QAbstractItemView)
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
"""
Data frame 계산 속도 향상 필요, 현재 임의의 Wafer 계측값으로 사용. 추후 보간을 활용해 값 채워 넣는 알고리즘 개발 필요
test = pd.DataFrame(index=range(0,101), columns=range(0,101))     
for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0
test[test == 0] = np.nan    
"""
"""
C.I 이미지 가져오기
아래 오류 해결 - 폴더를 지정하는게 아니라 경로를 지정해야함!
[Errno 13] Permission denied: 'C:\\Users\\wtjang\\Wafer viewer'
from PIL import Image
CI_Path = r"C:\Users\wtjang\Wafer viewer\CI.JPG"
im = Image.open(CI_Path)
"""
"""
PyQt에서 UI파일을 사용하는 방법은 2가지
1. UI파일을 파이썬 코드로 변경해서 사용 -> UI가 변경될 때마다 계속 파이썬 코드로 변경해야하는 번거로움
2. UI파일을 파이썬 코드에서 로드하는 방법 -> loadUiType 사용해서 UI파일을 파이썬 코드에 이벤트로 처리
"""
Ui_MainWindow, QMainWindow = loadUiType(r'C:\Users\wtjang\Wafer viewer\test_file_open.ui')
  
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color : white;")  #Qmainwindow 배경처리
        self.setWindowTitle("Wafer viewer")
        
        self.data_Search.clicked.connect(self.data_SearchClicked)
        
        # 사전에 테이블 row, col 이 정의되어야함.. 흠...;; 정해지지 않으면 출력x row, column 갯수 설정해야만 tablewidget 사용할수있다.


        self.meta_table_view.setRowCount(25)
        self.meta_table_view.setColumnCount(5)
        self.meta_table_view.setHorizontalHeaderLabels(['SLOT', 'LOT ID', 'COLLECTION DATE/TIME', 'RECIPE', 'MATERIAL'])


        
        
        self.stat_table_view.setRowCount(75)
        self.stat_table_view.setColumnCount(10)
        self.stat_table_view.setHorizontalHeaderLabels(['SLOT','RESULT TYPE', 'MEAN', 'MIN', 'MAX', '% STDDEV', 'STDDEV', '3 % STDDEV', '3 STDDEV', 'RANGE'])
        #self.setTableWidgetData()
        
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        
    def addmpl_2(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl_2.addWidget(self.canvas)
        self.canvas.draw() 
    
    def data_SearchClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "",
                                            "All Files(*);; Excel Files(*.xlsx);;Excel Files(*.csv)", '/home')
        
        if fname[0]:
            '''
            f = open(fname[0], 'r')
            flines = f.readlines()
 
            for line in flines:
                print(line)
            '''
            
            f = open(fname[0], 'r')
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
            num_Feature = len(df_Meta) / num_Wafer
            
            df_Meta_final = pd.DataFrame(columns = df_Meta.columns)
            
            for k in range(0, num_Wafer):
                df_Meta_final.loc[k] = df_Meta.loc[k*num_Feature]

            self.path_dir.setText(fname[0])
 
        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
        
        for meta_row in range(0, len(df_Meta_final)):
            for meta_col in range(0,5):
                self.meta_table_view.setItem(meta_row, meta_col, QTableWidgetItem(df_Meta_final.iloc[meta_row,meta_col]))
                
                
        for stat_row in range(0, len(df_Stat)):
            for stat_col in range(0,10):
                
                self.stat_table_view.setItem(stat_row, stat_col, QTableWidgetItem(df_Stat.iloc[stat_row,stat_col]))
             
                
               
                
                
               
                      

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
               
    #fig1 = Figure()
    #ax1f1 = fig1.add_subplot(111) 
    #img = ax1f1.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
    #fig1.colorbar(img)
       
    #fig2 = Figure()
    #ax1f2 = fig2.add_subplot(111) 
    #ax1f2.plot(np.random.rand(5))
        
    main = Main()
    
    #main.addmpl(fig1)
    #main.addmpl_2(fig2)
      
    #model = pandasModel(df_Meta_final)
    #view = QTableView()
    #view.setModel(model)
    #view.resize(800, 600)
    #view.show()
    
    main.show()
    
    sys.exit(app.exec_())
















'''
class pandasModel(QAbstractTableModel):
    
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
        
    def rowCount(self, parent=None):
        return self._data.shape[0]
    
    def columnCount(self,parent=None):
        return self._data.shape[1]
    
    def data(self, index, role = Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
'''





'''

    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111) 
    ax1f1.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
  
  
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 500)
        self.setWindowTitle("test")

        self.pushButton = QPushButton("File Open_test")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "",
                                            "All Files(*);; Excel Files(*.xlsx);;Excel Files(*.csv)", '/home')
        
        #self.label.setText(fname[0])    
        if fname[0]:
            f = open(fname[0], 'r')
            flines = f.readlines()
            
            for line in flines:
                print(line)
                
        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
    
       
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()




# 임의의 Wafer map 생성, 속도는 일단 나중에 생각하기로
import pandas as pd 
test = pd.DataFrame(index=range(0,101), columns=range(0,101))     

for i in range(0,101):
    for j in range(0,101):
        if ((50-i)**2 + (50-j)**2) < 50**2:
            test.loc[i,j] = i*2+i+j
        else:
            test.loc[i,j] = 0



import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
test[test == 0] = np.nan
plt.figure(1)
plt.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
plt.colorbar()    



from PyQt5.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import QtWidgets 

# 경로 주소 삽입
# The loadUiType function requires a single argument, the name of a Designer UI file

Ui_MainWindow, QMainWindow = loadUiType(r'C:\Users\wtjang\Wafer viewer\window.ui')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas) #mplvl
        self.canvas.draw()
 



   
 if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
# error  name 'QtWidgets' is not defined  -> QtGui.QApplication([" "]) ->  QtWidgets.QApplication([" "]) 으로 변경
# 컬러맵 cmap 속성에서 _r붙이면 reverse 효과
    
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111) 
    ax1f1.imshow(test, interpolation = 'hanning', vmin = 0, cmap = 'gist_rainbow_r')
 
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())
       
'''    

    
    