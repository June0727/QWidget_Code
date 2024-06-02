from PySide6.QtWidgets import QWidget, QLabel, QApplication
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

import sys
import os

class main_wnd(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100,100,600,300)
        self.setFixedSize(600,300)
        
        self.ds_set_mw()
        self.show()
        
    def ds_set_mw(self):
        label0 = QLabel('Hello, World!', self)
        label0.setFont(QFont('Arial',20))
        label0.setStyleSheet('background-color: red')
        label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        label0.move(30,30)
        
        self.ds_set_label1()
        
    def ds_set_label1(self):     #파일의 realpath를 알려주는 코드
        
        label1 = QLabel(self)
        
        fstr = os.path.realpath(__file__)
        pstr = os.path.dirname(fstr)
        
        pstr = os.path.realpath(__file__)
        istr = os.path.join(pstr,'D:/visualstudio/image/world.jpg')
        # pixmap = QPixmap('/visualstudio/world.jpg')
        
        print(istr)
        pixmap = QPixmap(istr)
        
        pixmap = pixmap.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio)
        label1.setPixmap(pixmap)
        
        label1.move(30,80)     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    mw = main_wnd()
    
    sys.exit(app.exec())