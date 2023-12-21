import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

# UI 파일의 정확한 경로를 지정합니다.
ui_file_path = "C:/Users/win10/Downloads/yolov5-master/yolov5-master/pyqtUI.ui"

# loadUiType 함수를 사용하여 UI 파일을 로드합니다.
Ui_MainWindow, QMainWindowBase = loadUiType(ui_file_path)

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
