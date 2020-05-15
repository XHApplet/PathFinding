# -*- coding:utf-8 -*-
'''
@Description: 主界面
@Author: lamborghini1993
@Date: 2020-05-11 16:26:05
@UpdateDate: 2020-05-15 20:57:20
'''

# Standard Library
import asyncio

# PyQt5
from PyQt5 import QtWidgets

# Custom Library
from logic import astar
from logic.define import Status
from ui import mainwindow


class CMainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._type = astar.MANHATTAN
        self._status = Status.PENDING
        self._init_ui()
        self._init_signal()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        if self._status == Status.PENDING:
            self.start.setText("开始")
            self.clear_path.setEnabled(False)
            self.clear_wall.setEnabled(False)
        elif self._status == Status.RUNNING:
            self.start.setText("运行中")
            self.start.setEnabled(False)
            self.clear_path.setEnabled(True)
            self.clear_wall.setEnabled(True)
        elif self._status == Status.END:
            self.start.setText("重新运行")
            self.start.setEnabled(True)
            self.clear_path.setEnabled(True)
            self.clear_wall.setEnabled(True)

    def _init_ui(self):
        self.frame.resize_map(50, 30)
        self.step_int.setRange(0, 1)
        self.step_int.setDecimals(1)

    def _init_signal(self):
        self.buttonGroup.buttonClicked.connect(self.__type_change)
        self.start.clicked.connect(self.__start)
        self.clear_path.clicked.connect(self.__clear_path)
        self.clear_wall.clicked.connect(self.__clear_wall)


    def __type_change(self, btn):
        if btn == self.manhattan:
            self._type = astar.MANHATTAN
        elif btn == self.diagonal:
            self._type = astar.DIAGONAL_STEP
        elif btn == self.diagonal_dis:
            self._type = astar.DIAGONAL_DIS

    def __start(self):
        self.frame.clear()
        self.status = Status.RUNNING
        self._astar = astar.AStar(*self.frame.get_map_info(), self._type, self._astar_call, self.step_int.value())

    def __clear_path(self):
        self.frame.clear()

    def __clear_wall(self):
        self.frame.clear(True)

    def _astar_call(self, _type, pos):
        self.frame._astar_call(_type, pos)
        if _type == astar.RESULT:
            self.status = Status.END
