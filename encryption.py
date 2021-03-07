from PyQt5 import QtWidgets
import sys
import base64
import hashlib
import urllib.parse
import time,datetime

import Ui_untitled

class encryption(QtWidgets.QMainWindow,Ui_untitled.Ui_MainWindow):
    def __init__(self):
        super(encryption,self).__init__()
        self.setupUi(self)

    #加密/解密
    def encr_base64(self):
        if self.radioButton.isChecked():
            print('选中了base64加密')
            str_source = self.textBrowser.toPlainText()
            str_encr = base64.b64encode(str_source.encode('utf-8'))
            self.textBrowser_2.setHtml(str(str_encr,'utf-8'))
        elif self.radioButton_2.isChecked():
            print('选中了base64解密')
            str_source = self.textBrowser.toPlainText()
            str_encr = base64.b64decode(str_source)
            self.textBrowser_2.setHtml(str(str_encr,'utf-8'))
        elif self.radioButton_3.isChecked():
            print('选中了md5加密')
            str_source = self.textBrowser.toPlainText()
            str_encr = hashlib.md5(str_source.encode(encoding='UTF-8')).hexdigest()
            self.textBrowser_2.setHtml(str(str_encr))
        elif self.radioButton_4.isChecked():
            print('选中了urlencode')
            str_source = self.textBrowser.toPlainText()
            str_encr = urllib.parse.quote_plus(str(str_source))
            self.textBrowser_2.setHtml(str(str_encr))
        elif self.radioButton_5.isChecked():
            print('选中了urldecode')
            str_source = self.textBrowser.toPlainText()
            str_encr = urllib.parse.unquote(str(str_source))
            self.textBrowser_2.setHtml(str(str_encr))
        elif self.radioButton_6.isChecked():
            print('选中了日期转化时间戳')
            str_source = self.textBrowser.toPlainText()
            timeArray = time.strptime(str_source, "%Y-%m-%d %H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            str_encr = urllib.parse.unquote(str(timeStamp))
            self.textBrowser_2.setHtml(str(str_encr))
        elif self.radioButton_7.isChecked():
            print('选中了时间戳转化日期')
            str_source = self.textBrowser.toPlainText()
            timeArray = time.localtime(int(str_source))
            str_encr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            self.textBrowser_2.setHtml(str(str_encr))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_untitled.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    window = encryption()
    window.show()
    sys.exit(app.exec_())
