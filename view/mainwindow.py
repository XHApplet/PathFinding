# -*- coding:utf-8 -*-
'''
@Description: 主界面
@Author: lamborghini1993
@Date: 2020-05-11 16:26:05
@UpdateDate: 2020-05-12 16:39:50
'''

from PyQt5 import QtWidgets

from logic import astar
from ui import mainwindow


class CMainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._type = astar.MANHATTAN
        self._init_ui()
        self._init_signal()

    def _init_ui(self):
        self.mapBox.hide()
        self.frame.resize_map(50, 30)

    def _init_signal(self):
        self.create_map.clicked.connect(self.__create_map)
        self.start.clicked.connect(self.__start)
        self.buttonGroup.buttonClicked.connect(self.__type_change)

    def __create_map(self):
        h = int(self.spinBoxH.text())
        w = int(self.spinBoxW.text())
        self.frame.resize_map(w, h)

    def __type_change(self, btn):
        if btn == self.manhattan:
            self._type = astar.MANHATTAN
        elif btn == self.diagonal:
            self._type = astar.DIAGONAL

    def __start(self):
        self._astar = astar.AStar(*self.frame.get_map_info(), self._type, self._astar_call)

    def _astar_call(self, _type, pos):
        self.frame._astar_call(_type, pos)
