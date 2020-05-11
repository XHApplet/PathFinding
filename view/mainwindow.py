# -*- coding:utf-8 -*-
'''
@Description: 主界面
@Author: lamborghini1993
@Date: 2020-05-11 16:26:05
@UpdateDate: 2020-05-11 19:34:17
'''

from ui import mainwindow

from PyQt5 import QtWidgets


class CMainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._init_ui()
        self._init_signal()

    def _init_ui(self):
        self.mapBox.hide()
        self.frame.resize_map(50, 30)

    def _init_signal(self):
        self.create_map.clicked.connect(self.__create_map)

    def __create_map(self):
        h = int(self.spinBoxH.text())
        w = int(self.spinBoxW.text())
        self.frame.resize_map(h, w)
