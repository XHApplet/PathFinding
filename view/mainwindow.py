# -*- coding:utf-8 -*-
'''
@Description: 主界面
@Author: lamborghini1993
@Date: 2020-05-11 16:26:05
@UpdateDate: 2020-05-16 13:42:18
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
        self._astar = None
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
            self.start.setEnabled(True)
            self.debug.setEnabled(True)
            self.clear.setEnabled(True)
        elif self._status == Status.RUNNING:
            self.start.setText("停止")
            self.start.setEnabled(True)
            self.debug.setEnabled(False)
            self.clear.setEnabled(False)
        elif self._status == Status.DEBUG:
            self.start.setText("停止")
            self.debug.setText("下一步")
            self.start.setEnabled(True)
            self.debug.setEnabled(True)
            self.clear.setEnabled(False)

    def _init_ui(self):
        self.frame.resize_map(50, 30)
        self.step_int.setRange(0, 1)
        self.step_int.setDecimals(1)

    def _init_signal(self):
        self.buttonGroup.buttonClicked.connect(self.__type_change)
        self.start.clicked.connect(self.__start)
        self.clear.clicked.connect(self.__clear)
        self.debug.clicked.connect(self.__debug)


    def __type_change(self, btn):
        if btn == self.manhattan:
            self._type = astar.MANHATTAN
        elif btn == self.diagonal:
            self._type = astar.DIAGONAL_STEP
        elif btn == self.diagonal_dis:
            self._type = astar.DIAGONAL_DIS

    def __start(self):
        self.frame.clear()
        if self.status == Status.PENDING:
            self.status = Status.RUNNING
            self._astar = astar.AStar(*self.frame.get_map_info(), self._type, self._astar_call, self.step_int.value())
        else:
            self.status = Status.PENDING
            self._astar.stop()
            self._astar = None

    def __clear(self):
        self.frame.clear(True)

    def __debug(self):
        self.status = Status.DEBUG
        if not self._astar:
            self.frame.clear()
            self._astar = astar.AStar(*self.frame.get_map_info(), self._type, self._astar_call, self.step_int.value(), True)
        else:
            self._astar.next()

    def _astar_call(self, _type, pos):
        self.frame.astar_call(_type, pos)
        if _type == astar.RESULT:
            self.status = Status.PENDING
            self._astar = None
