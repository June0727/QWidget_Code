#PySide6를 이용한 가상환경에서 사용할 라이브러리와 모듈을 불러온다.
import PySide6.QtCore
from PySide6.QtWidgets import(QWidget, 
                                QApplication, QLabel)

import sys
#코드실행 시 나올 창
class MW(QWidget):
    def __init__(self):
        super().__init__()        
        self.setGeometry(200, 100, 400, 200)
        self.setWindowTitle("Main Window in PySide")
        #창을 화면에 띄우기 위한 코드
        self.show()
        
if __name__ == "__main__":
    # Event Loop 등을 위한 QApplication instance 생성.
    app = QApplication(sys.argv) #1
    # main window 생성 및 show 호출.
    window = MW() #2
    # Event Loop 시작.
    sys.exit(app.exec()) #3
    # ret_v = app.exec()
    # print(type(ret_v),ret_v)
    # sys.exit(ret_v)
    
    

     
      