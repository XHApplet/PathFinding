# -*- coding:utf-8 -*-
'''
@Description: 主函数
@Author: lamborghini1993
@Date: 2020-05-11 15:47:48
@UpdateDate: 2020-05-11 17:20:16
'''

import sys
from PyQt5 import QtWidgets, QtGui
from view import mainwindow

def Mainwindow():
    app = QtWidgets.QApplication(sys.argv)
    obj = mainwindow.CMainWindow()
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    palette = obj.palette()
    dPaletteInfo = {
        QtGui.QPalette.Base: (60, 58, 56),
        QtGui.QPalette.AlternateBase: (80, 80, 80),
        QtGui.QPalette.Window: (56, 56, 56),
        QtGui.QPalette.Text: (180, 180, 180),
        QtGui.QPalette.WindowText: (180, 180, 180),
        QtGui.QPalette.Button: (80, 80, 80),
        QtGui.QPalette.ButtonText: (180, 180, 180),
        QtGui.QPalette.Light: (80, 80, 80),
        QtGui.QPalette.Inactive: (150, 150, 150),
        QtGui.QPalette.Highlight: (150, 150, 150),
    }
    for oQT, tColor in dPaletteInfo.items():
        palette.setColor(oQT, QtGui.QColor(*tColor))
    obj.setPalette(palette)
    obj.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    Mainwindow()
